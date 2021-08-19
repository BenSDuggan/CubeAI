# Changes

## 1.0.1a

CubeAI is finally going to be updated from the version made at the end of 2018. The goal of this version is to update the project structure and get an early version on PyPI.  The next goal will be to reorganize the modules so they are easier to understand.

### cubeguy

The [cubeguy](/cubeguy) directory will hold the main Python code and will be uploaded to PyPI.


### tests

* Added unit tests using pytest
* The [AI_Test_Base](/tests/base.py) class contains the unit tests that should be ran for each AI 
    * Each AI unit test must inherit the AI_Test_Base class and implement the `preflight()` method for this unit testing to work
    * The advantage of applying this class based testing scheme is that a general suite of tests can be applied to test the AIs

