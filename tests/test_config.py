"""
    Test if config.py is working correctly
"""

import os

import dapt

SAMPLE_CONFIG = {"last-test":None, "performed-by":None, "sheets-spreedsheet-id":None, "sheets-creds-path":None, "sheets-worksheet-id":None, "sheets-worksheet-title":None, "num-of-runs":None, "computer-strength":None, "box" : {"client_id" : None, "client_secret" : None, "access_token" : None, "refresh_token" : None, "refresh_time" : None}}

# Test creation of new config file
def test_config_create():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')
	expected = {"last-test":None, "performed-by":None, "sheets-spreedsheet-id":None, "sheets-creds-path":None, "sheets-worksheet-id":None, "sheets-worksheet-title":None, "num-of-runs":None, "computer-strength":None, "box" : {"client_id" : None, "client_secret" : None, "access_token" : None, "refresh_token" : None, "refresh_time" : None}}

	os.remove('config.json')

	assert conf.config == dapt.config.DEFAULT_CONFIG, "The Config.create() method that creates a new and empty config file returned wrong."

# Test changing a value in Config
def test_config_file_change():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	expected = conf.config
	expected["performed-by"] = 'Clifford'

	conf.config["performed-by"] = 'Clifford'
	conf.update()

	os.remove('config.json')

	assert conf.config == expected, "Config did not change the value correctly."

# Test adding a key,value pair in Config
def test_config_file_add():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	expected = conf.config
	expected["abc"] = 123

	conf.config["abc"] = 123
	conf.update()

	os.remove('config.json')

	assert conf.config == expected, "Config did not add the key,value pair correctly."

# Test adding a key,value pair in Config
def test_config_get_value_str():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.config["abc"] = 123
	conf.update()

	os.remove('config.json')

	assert conf.get_value("abc") == 123, "Config.get_value(\"abc\",recursive=False): Config did not find the correct value."

def test_config_get_value_arr():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.config["abc"] = {"a":1, "b":2, "c":{"aa":11, "bb":22}}
	conf.update()

	os.remove('config.json')

	assert conf.get_value(["abc", "c", "aa"]) == 11, 'Config.get_value(["abc", "c", "aa"],recursive=False): Config did not find the correct value.'

def test_config_get_value_recursive():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.config["abc"] = {"a":1, "b":2, "c":{"aa":11, "bb":22}}
	conf.update()

	os.remove('config.json')

	assert conf.get_value("aa", recursive=True) == 11, 'Config.get_value("aa",recursive=True): Config did not find the correct value.'

# Test making config file safe for uploading publicly
def test_config_safe():
	dapt.Config.create('config.json')
	conf = dapt.Config('config.json')

	expected = conf.config
	expected["access-token"] = ''
	expected["refresh-token"] = ''

	dapt.Config.safe('config.json')

	os.remove('config.json')

	assert conf.config == expected, "Conf did not make the config file safe."

# Test the update_value method when no key is given
def test_config_update_value_none():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.config["abc"] = 123
	conf.update()
	actual = conf.read()

	os.remove('config.json')

	expected = dapt.config.DEFAULT_CONFIG.copy()
	expected["abc"] = 123

	assert actual == expected, "Config.update_value(): Config did not save the config properly when no arguments were provided to `update_value()`."

# Test the update_value method when a str key is given
def test_config_update_value_str():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.update(key="abc", value=123, recursive=False)
	actual = conf.read()

	os.remove('config.json')

	expected = dapt.config.DEFAULT_CONFIG.copy()
	expected["abc"] = 123

	assert actual == expected, "Config.update_value(key=\"abc\", value=123): Config did not save the config properly when str arguments were provided to `update_value()`."

# Test the update_value method when an arr key is given
def test_config_update_value_arr():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.update(key=["a", "b"], value=123, recursive=False)
	actual = conf.read()

	os.remove('config.json')

	expected = dapt.config.DEFAULT_CONFIG.copy()
	expected["a"] = {"b": 123}

	assert actual == expected, "Config.update_value(key=[\"a\", \"b\"], value=123): Config did not save the config properly when str arguments were provided to `update_value()`."

# Test the update_value method when recursive and only one element in the array is given
def test_config_update_value_recursive_parent():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.update(key="big-swag", value=123, recursive=True)
	actual = conf.read()

	os.remove('config.json')

	expected = dapt.config.DEFAULT_CONFIG.copy()
	expected["big-swag"] = 123

	assert actual == expected, "Config.update_value(key=\"big-swag\", value=123): Config did not save the config properly when str not in dict and recursive arguments were provided to `update_value()`."

# Test the update_value method when recursive is given
def test_config_update_value_recursive():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	conf.update(key="access_token", value=123, recursive=True)
	actual = conf.read()

	os.remove('config.json')

	expected = dapt.config.DEFAULT_CONFIG.copy()
	expected["box"]["access_token"] = 123

	assert actual == expected, "Config.update_value(key=\"access_token\", value=123): Config did not save the config properly when str and recursive arguments were provided to `update_value()`."


# Test the has_value method when the key is not in the config
def test_config_has_value_null():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	os.remove('config.json')

	assert conf.has_value('fried-chicken') == False, "Config.has_value() should return False when key is not in the config"

# Test the has_value method when the key has a value of None
def test_config_has_value_None():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')

	os.remove('config.json')

	assert conf.has_value('last-test') == False, "Config.has_value() should return False when key has a value of None"

# Test the has_value method when the key is an str has a value
def test_config_has_value_str():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')
	conf.update(key='last-test', value='3a')

	os.remove('config.json')

	assert conf.has_value('last-test') == True, "Config.has_value() should return True when str key has a value"

# Test the has_value method when the key is an arr has a value
def test_config_has_value_arr():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')
	conf.update(key=['big','swag'], value='sup', recursive=False)

	os.remove('config.json')

	assert conf.has_value(key=['big','swag']) == True, "Config.has_value() should return True when str key has a value"

# Test the has_value method when the key is nested
def test_config_has_value_recursive():
	dapt.Config.create('config.json')

	conf = dapt.Config('config.json')
	conf.update(key=['big','swag'], value='sup', recursive=False)
	
	os.remove('config.json')

	assert conf.has_value(key='swag', recursive=True) == True, "Config.has_value() should return True when key is nested and recursive is True"
