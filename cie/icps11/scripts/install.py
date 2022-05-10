import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/icps11/utilities')

import os
import re
import time
import zipfile
from urllib import request
import shutil
import threading
import glob
import subprocess
import ctypes
import helper
import product


print(os.system(r'C:\Windows\system32\pnputil -i -a C:\Users\CIE\Documents\UWD\Win64\Drivers\ICPSComponent\ICPSComponent.inf'))
time.sleep(5)
print(os.system(r'C:\Windows\system32\pnputil -i -a C:\Users\CIE\Documents\UWD\Win64\Drivers\ICPSExtension\ICPSExtension.inf'))
time.sleep(5)

appx_path= glob.glob('/Users/CIE/Documents/UWD/Win64/App/ICPS*.appx')[-1]
print(helper.install_appx(appx_path))
time.sleep(5)

install_results=[2,2,2]

if len(helper.get_appx_details(product.product['ICPS_1.1']['get_details']['appx_name'])) == 0:
    print('Appx Install Failed')
else:
    print('Appx Install Passed')
    install_results[0]=1

if len(helper.get_all_oem(product.product['ICPS_1.1']['get_details']['component_file'])) ==0:
    print('Driver component file Install Failed')
else:
    print('Driver component file Install Passed')
    install_results[1]=1

if len(helper.get_all_oem(product.product['ICPS_1.1']['get_details']['extension_file'])) ==0:
    print('Driver extension file Install Failed')
else:
    print('Driver extension file Install Passed')
    install_results[2]=1

print('...END...')
