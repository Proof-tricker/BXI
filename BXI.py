import os,platform
BXI=platform.architecture()[0]
if BXI=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif BXI=="64bit":
    __import__("Proof64")
os.system('xdg-open https://chat.whatsapp.com/LB2ucS3nw2z31ENTQnUCZq')

