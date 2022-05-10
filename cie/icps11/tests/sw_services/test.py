import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/icps11/scripts')

import sw_services
import slash
from base.pytm_base_test import PytmBaseTest

class ServicesIcps(PytmBaseTest):

    def test_IDBWM_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[0] == 1:
            slash.logger.info("IDBWM SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("IDBWM SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")

    def test_intel_analytics_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[1] == 1:
            slash.logger.info("INTEL ANALYTICS SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("INTEL ANALYTICS SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")

    def test_intel_connectivity_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[2] == 1:
            slash.logger.info("INTEL CONNECTIVITY SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("INTEL CONNECTIVITY SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")

    def test_IntelConnectService_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[3] == 1:
            slash.logger.info("IntelConnectService SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("IntelConnectService SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")
