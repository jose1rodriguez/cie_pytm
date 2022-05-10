import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/icps11/scripts/sdl')

import CIE1487
import slash
from base.pytm_base_test import PytmBaseTest

class CIE_1487(PytmBaseTest):

    def test_accesschk_check_(self):
        if CIE1487.sdl_results[0] == 1:
            slash.logger.info("accesschk64.exe found in /Users/CIE/Documents")
        else:
            raise Exception("accesschk64.exe was not found in /Users/CIE/Documents")

    def test_iaps_pipe_permissions(self):
        if CIE1487.sdl_results[1] == 1:
            slash.logger.info("IAPSPipe has the correct permissions: RW NT AUTHORITY\Authenticated Users")
        else:
            raise Exception("IAPSPipe permissions are not RW")

    def test_iaps_n_pipe_permissions(self):
        if CIE1487.sdl_results[2] == 1:
            slash.logger.info("IAPSPPipe_N has the correct permissions: RW NT AUTHORITY\Authenticated Users")
        else:
            raise Exception(" IAPSPPipe_N permissions are not RW")
