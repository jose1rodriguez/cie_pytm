import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/scripts/sdl')

import CIE1717
import slash
from base.pytm_base_test import PytmBaseTest

class CIE_1717(PytmBaseTest):

    def test_check_db_file(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD "+str(latest_build))
        if CIE1717.sdl_results[2] == 1:
            slash.logger.info("ActivityLog.db FOUND IN "+str(CIE1717.db_path))
        else:
            raise Exception("ActivityLog.db NOT FOUND IN 'C:\ProgramData")

    def test_db_file_permissions(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD "+str(latest_build))
        if CIE1717.sdl_results[0] == 1:
            slash.logger.info("ActivityLog.db FILE HAS "+str(CIE1717.sdl_results[1])+ " PERMISSIONS")
        else:
            raise Exception("ActivityLog.db FILE HAS "+str(CIE1717.sdl_results[1])+ " PERMISSIONS")
