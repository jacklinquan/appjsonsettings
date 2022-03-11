# -*- coding: utf-8 -*-
"""A Python module for easy application settings in JSON format.

- Author: Quan Lin
- License: MIT
"""

# Project version
__version__ = "0.2.0"
__all__ = ["load", "save"]

import json


def load(file_path, default_settings=None):
    """Load settings from JSON file.

    In case the file does not exist, it creates a new one with default_settings.

    Parameters
    ----------
    file_path : str
        The full file path to the settings file in JSON format.
    default_settings : dict, optional
        The default settings dictionary.
        (default is `None`)

    Returns
    -------
    dict
        The settings dictionary.
    """
    try:
        with open(file_path, "r") as settings_file:
            settings = json.load(settings_file)
    except:
        save(file_path, default_settings or {})
        with open(file_path, "r") as settings_file:
            settings = json.load(settings_file)
    return settings


def save(file_path, settings_to_save):
    """Save settings to JSON file.

    Parameters
    ----------
    file_path : str
        The full file path to the settings file in JSON format.
    settings_to_save : dict
        The settings dictionary to save.
    """
    with open(file_path, "w") as settings_file:
        json.dump(settings_to_save, settings_file)
