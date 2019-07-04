# -*- coding: utf-8 -*-
"""A simple python package for easy application settings in JSON format.

Author: Quan Lin
License: MIT

:Example:
>>> import appjsonsettings
>>> settings_file_path = "settings.json"
>>> default_settings = {'a': 0, 'b': 'hello', 'c': []}
>>> # If the file does not exist, it creates a new one with default_settings.
...
>>> settings = appjsonsettings.load(settings_file_path, default_settings)
>>> settings
{u'a': 0, u'c': [], u'b': u'hello'}
>>> settings['a'] += 1
>>> settings['b'] += ' world!'
>>> settings['c'].append(1.23)
>>> appjsonsettings.save(settings_file_path, settings)
>>> settings = appjsonsettings.load(settings_file_path, default_settings)
>>> settings
{u'a': 1, u'c': [1.23], u'b': u'hello world!'}
"""

# Project version
__version__ = '0.1.0'
__all__ = ['load', 'save']

import json

def load(file_path, default_settings={}):
    """Load settings from JSON file.
    
    If the file does not exist, it creates a new one with default_settings.
    
    :param file_path: full file path.
    :type file_path: str.
    :param default_settings: default settings.
    :type default_settings: dict.
    :returns: settings.
    :rtype: dict
    """
    try:
        with open(file_path, "r") as settings_file:
            settings = json.load(settings_file)
    except:
        save(file_path, default_settings)
        with open(file_path, "r") as settings_file:
            settings = json.load(settings_file)
    return settings
    
def save(file_path, settings_to_save):
    """Save settings to JSON file.
    
    :param file_path: full file path.
    :type file_path: str.
    :param settings_to_save: settings to save.
    :type settings_to_save: dict.
    """
    with open(file_path, "w") as settings_file:
        json.dump(settings_to_save, settings_file)
    
    