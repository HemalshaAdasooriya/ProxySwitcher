import winreg
import pystray
from PIL import Image, ImageDraw
import ctypes

# Gets the current proxy status from Windows Registry
def get_proxy_status():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(registry_key, "ProxyEnable")
        winreg.CloseKey(registry_key)
        return value == 1
    except Exception:
        return False

# Toggles the registry value and forces Windows to refresh network settings
def toggle_proxy(icon, item):
    is_on = get_proxy_status()
    new_status = 0 if is_on else 1
    
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, "ProxyEnable", 0, winreg.REG_DWORD, new_status)
        winreg.CloseKey(registry_key)
        
        # This is the secret sauce: tells Windows to apply the registry change immediately
        internet_set_option = ctypes.windll.wininet.InternetSetOptionW
        internet_set_option(0, 39, 0, 0) # INTERNET_OPTION_SETTINGS_CHANGED
        internet_set_option(0, 37, 0, 0) # INTERNET_OPTION_REFRESH

        update_icon(icon)
    except Exception as e:
        print(f"Error toggling proxy: {e}")

# Draws a simple colored circle for the tray icon
def create_image(is_on):
    color = 'green' if is_on else 'red'
    image = Image.new('RGB', (64, 64), color=(255, 255, 255, 0)) # Transparent background
    dc = ImageDraw.Draw(image)
    dc.ellipse((8, 8, 56, 56), fill=color)
    return image

# Updates the hover text and icon color
def update_icon(icon):
    is_on = get_proxy_status()
    icon.icon = create_image(is_on)
    icon.title = "Proxy: ON (University)" if is_on else "Proxy: OFF (Mobile Data)"

def exit_app(icon, item):
    icon.stop()

# Build the right-click menu
menu = pystray.Menu(
    pystray.MenuItem('Toggle Proxy', toggle_proxy, default=True), # default=True allows double-click to toggle
    pystray.MenuItem('Exit', exit_app)
)

# Start the system tray app
initial_status = get_proxy_status()
tray_icon = pystray.Icon("ProxySwitcher", create_image(initial_status), "Proxy Switcher", menu)
update_icon(tray_icon)
tray_icon.run()