::文件编码: ANSI
@echo off
:: https://manga.bilibili.com/eden/credits-exchange.html?auto_sign=true
echo 10s后打开浏览器BM自动签到
echo 即将打开chrome
timeout 10

start chrome "https://manga.bilibili.com/eden/credits-exchange.html?auto_sign=true"

echo 即将打开edge
timeout 5
start msedge "https://manga.bilibili.com/eden/credits-exchange.html?auto_sign=true"