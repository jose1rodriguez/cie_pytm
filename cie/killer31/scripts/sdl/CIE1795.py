import winreg


driver_path='/Windows/System32/drivers/RivetNetworks/Killer/'
service_file=['KillerAnalyticsService.exe','KNDBWMService.exe','KillerNetworkService.exe','KAPSService.exe']
service_name=['Killer Analytics Service','Killer Dynamic Bandwidth Management','Killer Network Service','Killer Smart AP Selection Service']
exe_path=[0,0,0,0]

sdl_results=[1,1,1,1]

reg=winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)

try:
    key = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Services\Killer Analytics Service")
    dummy_n, exe_path[0], dummy_t = winreg.EnumValue(key, 3)
except:
    sdl_results[0]=3

try:
    key = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Services\Killer Network Service")
    dummy_n, exe_path[1], dummy_t = winreg.EnumValue(key, 3)
except:
    sdl_results[1]=3

try:
    key = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Services\KNDBWM")
    dummy_n, exe_path[2], dummy_t = winreg.EnumValue(key, 3)
except:
    sdl_results[2]=3

try:
    key = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Services\KAPSService")
    dummy_n, exe_path[3], dummy_t = winreg.EnumValue(key, 3)
except:
    sdl_results[3]=3

try:
    winreg.CloseKey(key)
    winreg.CloseKey(reg)
except:
    pass


n=0

try:
    for path in exe_path:
        for element in path:
            if element == ' ':
                sdl_results[n]=2
                n=n+1
except:
    pass


print(str(exe_path))
print(str(sdl_results))
