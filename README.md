# appjsonsettings

A simple python package for easy application settings in JSON format.

Please consider [![Paypal Donate](https://github.com/jacklinquan/images/blob/master/paypal_donate_button_200x80.png)](https://www.paypal.me/jacklinquan) to support me.

## Installation
`pip install appjsonsettings`

## Usage
```
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
```
