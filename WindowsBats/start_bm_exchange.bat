::文件编码: ANSI
@echo off
:: https://manga.bilibili.com/eden/credits-exchange.html?auto=true&cp_id=1938&refreshing=500&retry_range=1200-2500&end_min=4
echo 10s后打开浏览器BM自动兑换
echo 即将打开chrome
timeout 1

set AUTO=true
set CP_ID=1938
set REFRESHING=500
set RETRY_RANGE=1200-2500
set END_MIN=4

:: 如果 & 在变量中，需要在赋值时转义: (注意set 后的内容用引号包含)
set "URL=https://manga.bilibili.com/eden/credits-exchange.html?auto=%AUTO%^&cp_id=%CP_ID%^&refreshing=%REFRESHING%^&retry_range=%RETRY_RANGE%^&end_min=%END_MIN%"

echo %URL%

set BROWSER=chrome

:: /a 允许右侧数学运算
set DAY=%date:~8,2%
set /a "REMAIN=DAY %% 2"
echo %REMAIN%
if %REMAIN%==1 set BROWSER=msedge
start %BROWSER% %URL%

:: pause

