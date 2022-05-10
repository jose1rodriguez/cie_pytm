import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/scripts/sdl')

import CIE1795
import slash
from base.pytm_base_test import PytmBaseTest

class CIE_1795(PytmBaseTest):

    def test_KillerAnalyticsService_exe_path(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD " + str(latest_build))
        slash.logger.info("PATH TO EXECUTABLE: " + str(CIE1795.exe_path))
        if CIE1795.sdl_results[0] == 1:
            slash.logger.info(str(CIE1795.service_name[0])+" PATH TO EXECUTABLE HAS NO BLANK SPACES")
        else:
            raise Exception(str(CIE1795.service_name[0])+" PATH TO EXECUTABLE HAS BLANK SPACES")

    def test_KNDBWMService_exe_path(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD " + str(latest_build))
        slash.logger.info("PATH TO EXECUTABLE: " + str(CIE1795.exe_path))
        if CIE1795.sdl_results[1] == 1:
            slash.logger.info(str(CIE1795.service_name[1])+" PATH TO EXECUTABLE HAS NO BLANK SPACES")
        else:
            raise Exception(str(CIE1795.service_name[1])+" PATH TO EXECUTABLE HAS BLANK SPACES")

    def test_KillerNetworkService_exe_path(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD " + str(latest_build))
        slash.logger.info("PATH TO EXECUTABLE: " + str(CIE1795.exe_path))
        if CIE1795.sdl_results[2] == 1:
            slash.logger.info(str(CIE1795.service_name[2])+" PATH TO EXECUTABLE HAS NO BLANK SPACES")
        else:
            raise Exception(str(CIE1795.service_name[2])+" PATH TO EXECUTABLE HAS BLANK SPACES")

    def test_KAPSService_exe_path(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD " + str(latest_build))
        slash.logger.info("PATH TO EXECUTABLE: " + str(CIE1795.exe_path))
        if CIE1795.sdl_results[3] == 1:
            slash.logger.info(str(CIE1795.service_name[3])+" PATH TO EXECUTABLE HAS NO BLANK SPACES")
        else:
            raise Exception(str(CIE1795.service_name[3])+" PATH TO EXECUTABLE HAS BLANK SPACES")
