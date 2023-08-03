import os
import pyotp
import qrcode

key = ""

uri = pyotp.totp.TOTP(key).provisioning_uri(
	name='Folderv2',
	issuer_name='Fredrick')

print(os.listdir())
os.chdir("..")

totp = pyotp.TOTP(key)


if "Locker" in os.listdir():
    if 'y' == input('Do you want to Lock this folder?'):
        os.system('ren Locker "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
        os.system('attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
elif "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" in os.listdir():
    print("Folder is locked")
    while True:
        if (totp.verify(input(("Enter the Code : ")))):
            os.system('attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
            os.system('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Locker')
            print("Unlocked")
            break
        else:
            print("Wrong code try again")
else:
    os.mkdir("Locker")