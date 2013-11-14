#!/usr/bin/python
import subprocess
try:
    subprocess.check_call(['rm','/usr/bin/ethspeed'] )
except :
    print "error in uninstall"
    exit()
print "Uninstall successfull"
