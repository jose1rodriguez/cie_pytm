with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
    latest_build = f.readlines()

str(latest_build)
latest_build=latest_build[0]
zip_url=r'https://af01p-fm.devtools.intel.com/artifactory/ciebuildrepo-fm-local/nightly/Killer_REL_3.1/wsg-cit/ABI-Integration/Killer_Release_3.1/'+str(latest_build)+'/Release.zip'

sdl_results=[2,'UKNOWN',zip_url]

if latest_build[0] == '3' and latest_build[1] == '.' and latest_build[2] == '1' and latest_build[3] == '1':
    sdl_results[0]=1
    sdl_results[1]='3.11XX.XXX.x'

if latest_build[0] == '2' and latest_build[1] == '5' and latest_build[2] == '.':
    sdl_results[1]='25.xxx.xxx'

if latest_build[0] == '9' and latest_build[1] == '9' and latest_build[2] == '.':
    sdl_results[1]='99.xxx.xxx'

print(sdl_results)
