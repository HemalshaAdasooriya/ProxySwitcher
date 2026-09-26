[Setup]
AppName=Proxy Switcher
AppVersion=1.0
; Installs into the user's AppData folder so it doesn't require Admin rights
DefaultDirName={userappdata}\Proxy Switcher
DefaultGroupName=Proxy Switcher
; Saves the final setup.exe in your project folder
OutputDir=.\
OutputBaseFilename=ProxySwitcher_Setup
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked
Name: "startup"; Description: "Run automatically when Windows starts"; GroupDescription: "Additional icons:"

[Files]
; This looks for your compiled Python app inside the "dist" folder
Source: "dist\ProxyTrayApp.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Proxy Switcher"; Filename: "{app}\ProxyTrayApp.exe"
Name: "{autodesktop}\Proxy Switcher"; Filename: "{app}\ProxyTrayApp.exe"; Tasks: desktopicon
; This creates the startup shortcut if the user checked the box
Name: "{userstartup}\Proxy Switcher"; Filename: "{app}\ProxyTrayApp.exe"; Tasks: startup