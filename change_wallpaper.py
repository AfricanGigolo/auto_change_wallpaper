import ctypes
import os.path


def change_wallpaper(path):
    if not os.path.exists(path):
        return False
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path
                                               , 0)
    return True
