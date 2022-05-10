import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/icps11/scripts/sdl')

import CIE1477
import slash
from base.pytm_base_test import PytmBaseTest

class CIE_1477(PytmBaseTest):

    def test_black_duck_binary_analysis(self):
        with open('/Users/CIE/Documents/latest_build.txt', 'r') as f:
            latest_build = f.readlines()
        slash.logger.info("TESTING FOR BUILD " + str(latest_build))
        slash.logger.info("Full BDBA analysis can be found at bdba001.icloud.intel.com/#/groups/32?search=killer")

        if CIE1477.sdl_results[0] == 1:
            slash.logger.info("Black Duck Binary Analysis (BDBA) has no listed Vulnerabilities")
        else:
            raise Exception(str(CIE1477.sdl_results[1]))
