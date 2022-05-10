import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/utilities')

import os
import re
import time
import zipfile
from urllib import request
import shutil
import threading
import ctypes
import product
import helper


print(helper.get_appx_details(product.product['Killer_3.1']['get_details']['appx_name']))
print(helper.get_all_oem(product.product['Killer_3.1']['get_details']['component_file']))
print(helper.get_all_oem(product.product['Killer_3.1']['get_details']['extension_file']))

if product.product['Killer_3.1']['get_details'].get('appx_name', None):
    appx_details = helper.get_appx_details(product.product['Killer_3.1']['get_details']['appx_name'])
    if appx_details:
        print(helper.remove_appx(appx_details['PackageFullName']))

if product.product['Killer_3.1']['get_details'].get('component_file', None):
    driver_details = helper.get_all_oem(product.product['Killer_3.1']['get_details']['component_file'])
    for each_oem in driver_details:
        print(helper.remove_driver(each_oem))

if product.product['Killer_3.1']['get_details'].get('extension_file', None):
    driver_details = helper.get_all_oem(product.product['Killer_3.1']['get_details']['extension_file'])
    for each_oem in driver_details:
        print(helper.remove_driver(each_oem))

print(helper.get_appx_details(product.product['Killer_3.1']['get_details']['appx_name']))
print(helper.get_all_oem(product.product['Killer_3.1']['get_details']['component_file']))
print(helper.get_all_oem(product.product['Killer_3.1']['get_details']['extension_file']))

uninstall_results=[2,2,2]

if len(helper.get_appx_details(product.product['Killer_3.1']['get_details']['appx_name'])) == 0:
    print('Appx Unistall Passed')
    uninstall_results[0]=1
else:
    print('Appx Unistall Failed')

if len(helper.get_all_oem(product.product['Killer_3.1']['get_details']['component_file'])) ==0:
    print('Driver component file Unistall Passed')
    uninstall_results[1]=1
else:
    print('Driver component file Unistall Failed')

if len(helper.get_all_oem(product.product['Killer_3.1']['get_details']['extension_file'])) ==0:
    print('Driver extension file Unistall Passed')
    uninstall_results[2]=1
else:
    print('Driver extension file Unistall Failed')
