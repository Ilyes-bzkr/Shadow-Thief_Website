@echo off
echo Packaging Shadow-Thief2 Project...
echo =======================================
if not exist "downloads" mkdir downloads
powershell -Command "Compress-Archive -Path '..\Shadow-Thief2\*' -DestinationPath 'downloads\Shadow-Thief2.zip' -Force"
echo.
echo Packaging Complete!
echo You can now find the zip file at: downloads/Shadow-Thief2.zip
pause
