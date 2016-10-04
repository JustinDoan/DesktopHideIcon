import struct
import ctypes
import subprocess
import winreg
import os
from time import sleep



SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'C:\\Users\\Justin2\\Desktop\\Desktop Modifications\\background.jpg'


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())



def hide_icons():

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",0,winreg.KEY_ALL_ACCESS)
    
    winreg.SetValueEx(key, "HideIcons", 0, winreg.REG_DWORD, 0x00000001)

def show_icons():

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced",0,winreg.KEY_ALL_ACCESS)
    
    winreg.SetValueEx(key, "HideIcons", 0, winreg.REG_DWORD, 0x00000000)

def restart_explorer():
    filepath="C:\\Users\\Justin2\\Desktop\\DesktopModifications\\restart.bat"
    p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

    stdout, stderr = p.communicate()









    


show_icons()







#change_wallpaper()

