import os,platform
#os.system('xdg-open https://chat.whatsapp.com/LB2ucS3nw2z31ENTQnUCZq')
BXI=platform.architecture()[0]
if BXI=="32bit":
    print('\33[1;32mSorry 32 Bit Not Supported...')
elif BXI=="64bit":
    __import__("Proof64")
