import os
import re
import time
import zipfile
from urllib import request
import requests


release_url = r'curl https://af01p-fm.devtools.intel.com/artifactory/ciebuildrepo-fm-local/nightly/Killer_REL_3.1/wsg-cit/ABI-Integration/Killer_Release_3.1/ --ssl-no-revoke'
text = os.popen(release_url).read()
out_put = re.findall('href="(.*?)/">',text,re.DOTALL)
builds=[]

for element in out_put:
    if element.startswith("3.1") is True:
        builds.append(element)
builds.sort(reverse=True)
latest_build=builds[0]
print("LATEST BUILD IS "+str(latest_build))
with open('/Users/CIE/Documents/latest_build.txt', 'w') as f:
    f.write(str(latest_build))
zip_url=r'https://af01p-fm.devtools.intel.com/artifactory/ciebuildrepo-fm-local/nightly/Killer_REL_3.1/wsg-cit/ABI-Integration/Killer_Release_3.1/'+str(latest_build)+'/Packages/Killer-'+str(latest_build)+'-x64-Release.zip'
response=requests.get(zip_url)

build_results=0

if (response.status_code == 200):
    build_file=os.path.join('/Users/CIE/Documents', 'Killer-'+str(latest_build)+'-x64-Release.zip')
    request.urlretrieve(zip_url,build_file)
    with open('/Users/CIE/Documents/latest_build_status.txt', 'w') as f:
        f.write('passed')
        print("DOWNLOADED")
    with zipfile.ZipFile(build_file) as z:
        z.extractall('/Users/CIE/Documents')
    print("UNZIPED")
    print('BUILD PASSED')
    build_results=1
else:
    print('LATEST BUILD '+str(latest_build)+' FAILED')
    with open('/Users/CIE/Documents/latest_build_status.txt', 'w') as f:
        f.write('failed')

print('...END...')
