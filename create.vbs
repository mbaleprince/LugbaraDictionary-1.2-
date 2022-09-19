Set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c create.bat"
oShell.Run strArgs,0,false