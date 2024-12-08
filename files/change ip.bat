@echo off
setlocal

:menu
cls
echo Choose an option:
echo 1. Enter custom IP address
echo 2. Use predefined IP address

set /p choice="Enter your choice: "
if "%choice%"=="1" goto custom
if "%choice%"=="2" goto predefined

:custom
set /p ip_address="Enter the custom IP address: "
netsh interface ipv4 set address name="Ethernet" static %ip_address% 255.255.255.0
goto end

:predefined
cls
echo Choose a predefined IP address:
echo 1. 192.168.0.100
echo 2. 192.168.0.101

set /p ip_choice="Enter your choice: "
if "%ip_choice%"=="1" (
    set ip_address=192.168.0.100
) else if "%ip_choice%"=="2" (
    set ip_address=192.168.0.101
) else (
    echo Invalid choice
    pause
    goto menu
)

netsh interface ipv4 set address name="Ethernet" static %ip_address% 255.255.255.0
goto end

:end
echo IP address set successfully.
pause
