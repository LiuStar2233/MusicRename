Music Rename (Python version)
============

# Installation
1. Install Python 3
2. Download the main files `newMusicRename.py` and `START.bat` into the same directory
------

# Usage
1. Double-click `START.bat` for the first-time initialization
2. Place your music files into the `renameMusic` folder
3. Double-click `START.bat` to perform the operation
4. Wait for the program to complete
5. You can write your own batch script:
```bat
@echo off
echo Renaming music files...
python newMusicRename.py .\\folder_name_to_be_processed
pause
```
```bat
@echo off
echo Renaming music files...
python musicRename.py .\\folder_name_to_be_processed -d
pause
```
```bat
@echo off
echo Renaming music files...
python musicRename.py .\\folder_name_to_be_processed --dry-run
```
(The last two writings are the same, both simulating the renaming process)

------

# Precautions
1. Ensure your music filenames do not contain Chinese characters, otherwise the program may not work properly
2. Ensure your music filenames do not contain spaces, otherwise the program may not work properly
3. Ensure your music filenames do not contain special characters, otherwise the program may not work properly
4. Ensure your music filenames are not duplicated, otherwise the program may not work properly
5. Ensure your music filenames do not contain illegal characters, otherwise the program may not work properly
------
 
# Update Log
1. 2025-01-21: First commit to GitHub
------
 
# Features
1. Rename music files
2. Multi-threading support
3. Can be run in command-line mode
------

# Future Plans
1. Add a GUI
2. Add categorization