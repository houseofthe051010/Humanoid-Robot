@echo off
setlocal
cd /d "%~dp0.."
node "%~dp0server.cjs"
if errorlevel 1 pause
