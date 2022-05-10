import os
from pathlib import Path

db_path='C:\ProgramData\Intel\Connectivity\ActivityLog\ActivityLog.db'
py_db_path='/ProgramData/Intel/Connectivity/ActivityLog/ActivityLog.db'
py_db_path=Path(py_db_path)

sdl_results=[2,'UKNOWN',2]

if py_db_path.exists():
    sdl_results[2]=1

db_permissions=os.popen('icacls '+db_path).read()


if 'Users:(RX)' in db_permissions:
    sdl_results[0]=1
    sdl_results[1]='Read (RX)'

if 'Users:(RWXD)' in db_permissions:
    sdl_results[1]='Change (RWXD)'

if 'Users:(F)' in db_permissions:
    sdl_results[1]='Full (F)'

if 'Users:(RWXDPO)' in db_permissions:
    sdl_results[1]='Full (RWXDPO)'

if 'Users:(None)' in db_permissions:
    sdl_results[1]='None'

print(sdl_results)
