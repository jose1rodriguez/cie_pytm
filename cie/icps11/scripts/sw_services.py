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
import product
import helper


state=[]

for service in product.product['ICPS_1.1']['confirm_status']['services']:
    state.append(helper.get_service_details(service))

service=product.product['ICPS_1.1']['confirm_status']['services']

print(service)
print(state)
print('2=STOPPED')
print('1=RUNNING')
