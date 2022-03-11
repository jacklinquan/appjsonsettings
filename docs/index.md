# appjsonsettings
A Python module for easy application settings in JSON format.

## Installation
`pip install appjsonsettings`

## Usage
``` python
>>> import appjsonsettings
>>> settings_file_path = "settings.json"
>>> default_settings = {'a': 0, 'b': 'hello', 'c': []}
>>> # In case the file does not exist, it creates a new one with default_settings.
>>> settings = appjsonsettings.load(settings_file_path, default_settings)
>>> settings
{'a': 0, 'b': 'hello', 'c': []}
>>> settings['a'] += 1
>>> settings['b'] += ' world!'
>>> settings['c'].append(1.23)
>>> appjsonsettings.save(settings_file_path, settings)
>>> settings = appjsonsettings.load(settings_file_path, default_settings)
>>> settings
{'a': 1, 'b': 'hello world!', 'c': [1.23]}
```
