import subprocess
from urllib import request
import zipfile
import os.path

sdl_results=[2,2,2]

accessch_path='/Users/CIE/Documents/accesschk64.exe'

if os.path.exists(accessch_path) == True:
    sdl_results[0]=1
    accessch_path=r'C:\Users\CIE\Documents\accesschk64.exe'
    print('accesschk64.exe found in '+str(accessch_path))
else:
    try:
        zip_url=r'https://download.sysinternals.com/files/AccessChk.zip'
        file=os.path.join('/Users/CIE/Documents', 'AccessChk.zip')
        proxy = request.ProxyHandler({"https":"http://proxy-dmz.intel.com:911"})
        opener = request.build_opener(proxy)
        request.install_opener(opener)
        request.urlretrieve(zip_url,file)
        with zipfile.ZipFile(file) as z:
            z.extractall('/Users/CIE/Documents')
            sdl_results[0]=1
            print('accesschk64.exe downloaded in '+str(accessch_path))
    except:
        print('accesschk64.exe could not be downloaded')


iaps_pipe_permissions = str (subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', accessch_path+'  \pipe\IAPSPipe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True))
iaps_pipe_n_permissions = str (subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', accessch_path+'  \pipe\IAPSPipe_N'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True))

if iaps_pipe_permissions.count("RW") >= 2:
    sdl_results[1]=1

if iaps_pipe_n_permissions.count("RW") >= 2:
    sdl_results[2]=1

print(sdl_results)
if sdl_results == [1,1,1]:
    print(" Pipes have the correct permissions: RW NT AUTHORITY\Authenticated Users, RW BUILTIN\Administrators")
