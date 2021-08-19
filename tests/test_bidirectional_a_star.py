"""
Test if cubeguy.ai.bfs.py is working correctly.
"""

import cubeguy
from cubeguy.ai.bidirectional_a_star import Bidirectional_A_star

from tests.base import AI_Test_Base

Cube_Class = cubeguy.Cube

class Test_AI_BFS(AI_Test_Base):

	def preflight(self, n=2):
		"""
        Testing items that should be ran before tests are ran.  This method returns a new
        class method for the test.

        Returns:
            The class instance which will be used for the unit test.
        """
	
		return Bidirectional_A_star(Cube_Class(n=n))

	def postflight (self):
		"""
        Clean up after tests are ran.
        """

		pass