@echo off
chcp 65001
set /p u=要镜像的网址：
wget --mirror -p --convert-links -P ./web %u%
echo .
echo OK,完成了！
echo .
echo .
%0