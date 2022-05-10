import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/scripts')

import uninstall
import slash
from base.pytm_base_test import PytmBaseTest

class UninstallKiller(PytmBaseTest):

    def test_uninstall_appx(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if uninstall.uninstall_results[0] == 1:
            slash.logger.info("APPX FOR BUILD " + str(latest_build) + " SUCCESSFULLY UNINSTALL")
        else:
            raise Exception("APPX UNINSTALLATION FOR BUILD " + str(latest_build) + " FAILED")

    def test_remove_driver_component_file(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if uninstall.uninstall_results[1] == 1:
            slash.logger.info("DRIVER COMPONENT FILE FOR BUILD "+str(latest_build)+" SUCCESSFULLY REMOVED")
        else:
            raise Exception("DRIVER COMPONENT FILE FOR BUILD "+str(latest_build)+" FAILED TO BE REMOVED")

    def test_remove_driver_extension_file(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if uninstall.uninstall_results[2] == 1:
            slash.logger.info("DRIVER EXTENSION FILE FOR BUILD "+str(latest_build)+" SUCCESSFULLY REMOVED")
        else:
            raise Exception("DRIVER EXTENSION FILE FOR BUILD "+str(latest_build)+" FAILED TO BE REMOVED")
