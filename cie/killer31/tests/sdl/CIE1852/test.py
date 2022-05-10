import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/scripts/sdl')

import CIE1852
import slash
from base.pytm_base_test import PytmBaseTest

class CIE_1852(PytmBaseTest):

    def test_build_version_check(self):

        slash.logger.info("LATEST BUILD WAS PULLED FROM "+str(CIE1852.sdl_results[2]))

        if CIE1852.sdl_results[0] == 1:
            slash.logger.info("INSTALL VERSION IS THE CORRECT FORMAT: "+str(CIE1852.sdl_results[1]))
        else:
            raise Exception("INSTALL VERSION IS THE DEBUG FORMAT: "+str(CIE1852.sdl_results[1]))
