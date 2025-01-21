Music Rename (python version)
============

# 安装
1. 安装python3
2. 下载主要文件文件`newMusicRename.py`和`START.bat`到同一目录下
------

# 使用
1. 双击`START.bat`进行第一步初始化
2. 将你的音乐放进renameMusic文件夹中
3. 双击`START.bat`进行操作
4. 等待程序运行完成
5. 你可以自己编写一个bat脚本：
```bat
@echo off
echo Renaming music files...
python newMusicRename.py .\\待处理的文件夹名字
pause
```
```bat
@echo off
echo Renaming music files...
python musicRename.py .\\待处理的文件夹名字 -d
pause
```
```bat
@echo off
echo Renaming music files...
python musicRename.py .\\待处理的文件夹名字 --dry-run
```
(后两种写法时一样的，都是模拟重命名的过程)

-----

# 注意事项
1. 请确保你的音乐文件名没有中文，否则程序可能无法正常工作
2. 请确保你的音乐文件名没有空格，否则程序可能无法正常工作
3. 请确保你的音乐文件名没有特殊字符，否则程序可能无法正常工作
4. 请确保你的音乐文件名没有重复，否则程序可能无法正常工作
5. 请确保你的音乐文件名没有非法字符，否则程序可能无法正常工作
------

# 更新日志
1. 2025-01-21: 第一次提交到GitHub
------

# 功能
1. 对音乐进行重命名
2. 有多线程
3. 支持以命令行形式运行
------

# 将来
1. 添加GUI
2. 添加分类