# Proxy Switcher 🔄

A lightweight, blazing-fast Windows system tray utility built with Python that instantly toggles your system proxy settings. 

## 🚀 The Problem
While developing at the Sabaragamuwa University of Sri Lanka hostels, I constantly needed to switch between the university proxy Wi-Fi (for general internet access) and a direct mobile hotspot (for proxy-unfriendly developer tools like GitHub and Vercel). Manually navigating through Windows Network settings multiple times a day became a massive workflow bottleneck. 

**Proxy Switcher** solves this by providing a one-click desktop toggle and a visual system tray indicator to manage the Windows proxy state instantly.

## ✨ Features
* **One-Click Toggle:** Instantly switch between Proxy ON and Proxy OFF using a dedicated desktop shortcut or system tray menu.
* **Visual Status Indicator:** The system tray icon dynamically updates so you always know your network state at a glance:
  * 🟢 **Green:** Proxy ON (University Network)
  * 🔴 **Red:** Proxy OFF (Mobile Data/Direct Connection)
* **Zero Latency & No Restarts:** Utilizes the Windows API (`InternetSetOptionW`) to instantly refresh network settings system-wide. No need to restart your browser or terminal.
* **Seamless Boot:** Runs silently in the background on Windows startup.

## 🛠️ Tech Stack
* **Python** - Core logic
* **Windows API (`winreg` & `ctypes`)** - Registry manipulation and system network refresh
* **pystray & Pillow** - System tray UI and dynamic icon generation
* **PyInstaller** - Standalone executable compilation
* **Inno Setup** - Professional Windows installer packaging

## 📦 Installation
If you just want to use the app without compiling the code yourself:
1. Go to the [Releases](../../releases) tab on the right side of this repository.
2. Download the latest **`ProxySwitcher_Setup.exe`**.
3. Run the installer. (If Windows SmartScreen warns you about an "Unknown Publisher", click *More Info* -> *Run anyway*).
4. Check the box to add it to your Startup folder during installation.

## 💻 Building from Source
If you want to modify the code or build the `.exe` yourself:

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/ProxySwitcher.git](https://github.com/yourusername/ProxySwitcher.git)
   cd ProxySwitcher
