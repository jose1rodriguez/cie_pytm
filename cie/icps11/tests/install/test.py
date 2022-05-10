import sys
sys.path.append('/Users/CIE/titan-pytm-tests/testscie/icps11/scripts')

import install
import slash
from base.pytm_base_test import PytmBaseTest


class InstallIcps(PytmBaseTest):

    def test_install_appx(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if install.install_results[0] == 1:
            slash.logger.info("APPX FOR BUILD "+str(latest_build)+" SUCCESSFULLY INSTALLED")
        else:
            raise Exception("APPX INSTALLATION FOR BUILD "+str(latest_build)+" FAILED")

    def test_install_driver_component_file(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if install.install_results[1] == 1:
            slash.logger.info("DRIVER COMPONENT FILE FOR BUILD "+str(latest_build)+" SUCCESSFULLY ADDED")
        else:
            raise Exception("DRIVER COMPONENT FILE FOR BUILD "+str(latest_build)+" FAILED TO BE ADDED")

    def test_install_driver_extension_file(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if install.install_results[2] == 1:
            slash.logger.info("DRIVER EXTENSION FILE FOR BUILD "+str(latest_build)+" SUCCESSFULLY ADDED")
        else:
            raise Exception("DRIVER EXTENSION FILE FOR BUILD "+str(latest_build)+" FAILED TO BE ADDED")
