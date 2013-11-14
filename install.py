#!/usr/bin/python
import subprocess

try:
    subprocess.check_call(['chmod','755','./ethspeed'] )
    subprocess.check_call(['cp','./ethspeed','/usr/bin/ethspeed'] )
except subprocess.CalledProcessError:
    print "error in installation"
    exit()
print "Installation successfull"
