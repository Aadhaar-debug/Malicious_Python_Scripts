Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "%appdata%\Win-Wallpaper\wallpaper.py" & Chr(34), 0
Set WinScriptHost = Nothing
