from os.path import isfile
from time import sleep
from shutil import copyfile

if not isfile("/etc/hosts_backup"):
	copyfile("/etc/hosts","/etc/hosts_backup")

block_website=input("website to block?")
block_period=float(input("duration to block? (in minutes)"))

with open("/etc/hosts","a") as f:
	f.write("\n"+"127.0.0.1\t"+block_website+"\n")

print("blocking starts")
sleep(block_period*60)
print("blocking ends")
copyfile("/etc/hosts_backup","/etc/hosts")
print("done")
