import sys
sys.path.append('/Users/CIE/titan-pytm-tests/tests/cie/killer31/scripts')

import get_build
import slash
from base.pytm_base_test import PytmBaseTest

class GuetKillerBuild(PytmBaseTest):

    def test_get_build(self):
        if get_build.build_results == 1:
            slash.logger.info("BUILD "+str(get_build.latest_build)+" PASSED")
            slash.logger.info("BUILD DOWNLOADED IN /Users/CIE/Documents")
        else:
            raise Exception("BUILD "+str(get_build.latest_build)+" FAILED")
