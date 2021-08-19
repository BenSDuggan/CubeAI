"""
Base classes for testing.  These classes make it easy to add tests for a new AI class.
Each test class that inherits a testing class must implement the ``preflight()`` method.
This method sets up the testing environment and resets it from past tests.  The 
``postflight()`` method cleans up after the test.  Class specific tests can also be created.
"""

import cubeguy

class AI_Test_Base:
    def preflight(self, n=2):
        """
        Testing items that should be ran before tests are ran.  This method returns a new
        class method for the test.

        Returns:
            The class instance which will be used for the unit test.
        """

        pass

    def postflight(self):
        """
        Clean up after tests are ran.
        """

        pass

    def test_already_solved(self):

        ai_cube = self.preflight()
        ai_cube.solve()

        assert ai_cube.cube.isSolved(), "The cube is not solved"
    
    def test_2x2_t1(self):

        ai_cube = self.preflight(n=2)
        ai_cube.solve()

        assert ai_cube.cube.isSolved(), "The cube is not solved"

