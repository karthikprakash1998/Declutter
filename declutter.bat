@echo off
set path=%cd%
cd C:\Declutter
D:
C:\Python\Python37-32\python.exe declutter.py %path%
cd %path%
