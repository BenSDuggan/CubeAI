# DAPT Testing

Testing for DAPT is done using [pytest](pytest.org) and can be installed by entering `pip install pytest` in the terminal.  Travic CI is used for continuous integration and automatically runs the tests whenever code is pushed to the `master` or `dev` branch, or a pull request is made.  Tests should be written for all classes and functions included in the DAPT distribution.  DAPT leverages many APIs, including Google Sheets and Box.  This can make it challenging to test the classes that use the APIs as you don't want your credentials falling into the wrong hands.  Travic CI stores credentials as *Environment Variables* which keeps them secret.  When testing on a local computer, it is best to keep the credentials in a config file outside of ***any*** GitHub repo and pass that file to tests.  This will ensure that your credentials are kept safe and all features of DAPT are tested.

## Running the tests

There are a couple ways you can run the tests.

The first is to run `pytest` in the root directory of the project.  This is the simplest way to run the tests but requires that you have the GitHub repo downloaded.  Thus, this method works well if you are trying to add on to DAPT.  The other disadvantage to this method is that my need to make sure pytest is point to the correct version of Python.

The second way to run the tests is by open a python session in the terminal: `python3`.  Then type:
```
import dapt
dapt.test()
```

This will work if you have installed DAPT using the `pip` or if you downloaded the GitHub repo (assuming you're in the root directory).

By default, this will run the tests that do not require API credentials or logging in information.  

## Pytest command line arguments

| arg | options | usage |
| ---- |:----:| ----:|
| --color | [yes, no] | Turn terminal coloring on or off |
| --test_creds | None | Run the tests that require credentials but not logging in
| --test_login | None | Run the tests that require users to login
| --all | None| Run all the tests


## Other notes

* `env_to_config.py`: Finds variables from the environment and creates a config file to use.  This is useful when using Travis CI as it allows API keys to be passed.
* `escape_json.py`: Takes a JSON config file and escapes it for use in Travis CI.

## ToDo
- `Delimited_file`
    - Add tests that make class fail like trying to write to invalid row
- Make tests clean up better (remove files that are created)
- Add test to check `Box`
- Add test to check `tools`