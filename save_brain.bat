@echo off
chcp 65001 > nul
cd /d %~dp0

echo ==========================================
echo       SECOND BRAIN AUTO-SAVE SYSTEM       
echo ==========================================

echo [1/3] Staging files...
git add .

echo [2/3] Committing...
set NOW=%date% %time%
git commit -m "Save: %NOW%"

echo [3/3] Uploading to GitHub...
git push origin main

echo.
echo ==========================================
echo          SAVE COMPLETE! ( ^_^)b           
echo ==========================================
pause
