import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/scripts')

import sw_services
import slash
from base.pytm_base_test import PytmBaseTest

class ServicesKiller(PytmBaseTest):

    def test_KNDBWM_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[0] == 1:
            slash.logger.info("KNDBWM SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("KNDBWM SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")

    def test_killer_analytics_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[1] == 1:
            slash.logger.info("KILLER ANALYTICS SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("KILLER ANALYTICS SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")

    def test_killer_network_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[2] == 1:
            slash.logger.info("KILLER NETWORK SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("KILLER NETWORK SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")

    def test_KAPS_service(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        if sw_services.state[3] == 1:
            slash.logger.info("KAPS SERVICE FOR BUILD " + str(latest_build) + " IS RUNNING")
        else:
            raise Exception("KAPS SERVICE FOR BUILD " + str(latest_build) + " NOT RUNNING")
