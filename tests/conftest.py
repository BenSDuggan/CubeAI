"""
Settings for pytest
"""

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--test_creds", action="store_true", default=False,
        help="Run the tests that require credentials but not logging in"
    )
    parser.addoption(
        "--test_login", action="store_true", default=False,
        help="Run the tests that require users to login"
    )
    parser.addoption(
        "--all", action="store_true", default=False, help="Run all of the tests"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "test_creds: mark test as requiring credentials")
    config.addinivalue_line("markers", "test_login: mark test as requireing login")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--all"):
        # Want to run all tests, so let them
        return
    
    skip_creds = pytest.mark.skip(reason="need --test_creds option to run")
    skip_login = pytest.mark.skip(reason="need --test_login option to run")

    for item in items:
        if "test_creds" in item.keywords and not config.getoption("--test_creds"):
            item.add_marker(skip_creds)
        if "test_login" in item.keywords and not config.getoption("--test_login"):
            item.add_marker(skip_login)
        