import os
import re
import time
import zipfile
from urllib import request
import shutil
import threading
import ctypes, sys



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_os_command(command, dict_datatype = True, split_char = ':'):

    global result

    if is_admin():
        #print('RUNNING AS ADMIN')
        out_put = os.popen(command)

        if split_char == '=':
            out_put = re.sub(r'\s{2,}',"", out_put.read().replace('\n', ':'))
            return dict(text.split('=') for text in out_put.split(':') if len(text.split("=")) > 1 )

        if split_char == '{':
            out_put = re.sub(r'\s{2,}',"", out_put.read().replace('{', '').replace('}','').replace('"','').replace(',',''))
            dict_result = {}
            after_split =  out_put.split('=')
            if len(after_split) > 1:
                dict_result[after_split[0]] = after_split[1]
            return dict_result

        out_put = re.sub(r'\s{2,}',"", out_put.read().replace('\n', ','))
        if len(re.findall('failed', out_put, re.I)) > 0 or not dict_datatype:
            return out_put

                        #print(out_put)
        result = {}
        for text in out_put.split(','):
            if len(text) > 0 and ':' in text:
                split_text = text.split(':')
                result[split_text[0].strip()] = split_text[1].strip()

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

    return result



def remove_appx(appx_name):
    command = '''powershell -command "remove-appxpackage -package ''' + appx_name + '''"'''
    print(command)
    return run_os_command(command)

def remove_driver(driver_oem_name):
    command = 'pnputil /delete-driver {} /uninstall /force'
    return run_os_command(command.format(driver_oem_name))


def get_all_oem(original_name):
    pipe = os.popen('pnputil /enum-drivers')
    out_put = pipe.read().split('\n')
    oem_files = []
    for index, element in enumerate(out_put):
        #print(element)
        if ':' in element and element.strip() and element.split(':')[1].lower().strip() == original_name:
            oem_files.append(out_put[index-1].split(':')[1].strip())
    pipe.close()
    return oem_files

def get_appx_details(appx_name='RivetNetworks.KillerControlCenter'):
    command = '''powershell -command "Get-appxpackage -name ''' + appx_name + '''"'''
    return run_os_command(command)

def get_driver_details(driver_name='Killer Networking Software'):
    command = '''powershell -command "get-wmiobject win32_pnpsigneddriver|select DeviceName, DriverVersion, InfName| where {$_.DeviceName -like '*''' + driver_name + '''*'}|format-list"'''
    return run_os_command(command)


def get_driver_details(driver_name='Killer Networking Software'):                                                           ####### Jose
    command = '''powershell -command "get-wmiobject win32_pnpsigneddriver|select DeviceName, DriverVersion, InfName| where {$_.DeviceName -like '*''' + driver_name + '''*'}|format-list"'''
    return run_os_command(command)

def install_driver(driver_inf_path, reboot=False):
    if reboot:
        command = r'pnputil /add-driver {} /install /reboot'
    else:
        command = r'pnputil /add-driver {} /install '
    return run_os_command(command.format(driver_inf_path), False)

def install_appx(appx_package_path):
    command = '''powershell -command "add-appxpackage -path ''' + appx_package_path + '''"'''
    return run_os_command(command, False)

def get_service_details(service_name):
    command = 'sc queryex "{}" '
    result = run_os_command(command.format(service_name))
    #print(result)
    try:
        if result.get('STATE').lower().find('stopped') == 1:
            return 2
        elif result.get('STATE').lower().find('running') == 1:
            return 1
    except:
        return 0
