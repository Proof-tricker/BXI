import os,platform
os.system('xdg-open https://www.facebook.com/profile.php?id=100091356190977')
BXI=platform.architecture()[0]
if BXI=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif BXI=="64bit":
    __import__("Proof64")
