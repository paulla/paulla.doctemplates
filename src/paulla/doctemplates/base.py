#/usr/bin/env/python

import ConfigParser
import os.path
from shutil import rmtree
from paste.script.templates import Template, var

_dir, _f = os.path.split(os.path.abspath(__file__))
DEFAULT_CONFIG_FILE = os.path.join(_dir, 'etc', 'defaults.cfg')
BOOLEANS = ['False', 'True', '1', '0']


def getdefaults(section, cfg=DEFAULT_CONFIG_FILE):
    """Get default values for template vars."""
    Config = ConfigParser.ConfigParser()
    Config.read(cfg)
    options = Config.items(section)
    settings = dict(options)

    # sets real bool values in settings
    for option in options:
        if option[1] in BOOLEANS:
            settings[option[0]] = Config.getboolean(section, option[0])
    return settings


class HostBaseTemplate(Template):
    """Base template."""
    use_cheetah = True
    defaults = getdefaults('General')

    vars = Template.vars + \
           [var('desc', 'Host description', default=''),
            var('domain', 'Domaine', default=defaults['domain']),
            var('group', 'group', default=defaults['group']),
            var('location', 'location', default=defaults['location']),
            var('inet0', 'Ipv4 1', default=''),
            var('inet1', 'Ipv4 2', default=''),
           ]

    def boolify(self, vars):
        """."""
        unset = ['none', 'false', '0', 'n']
        for key in vars.keys():
            if isinstance(vars[key], basestring):
                if vars[key].lower() in unset:
                    vars[key] = False

    def pre(self, command, output_dir, vars):
        """."""
        if not 'group' in vars.keys():
            vars['group'] = self.defaults['group']
        if not 'location' in vars.keys():
            vars['location'] = self.defaults['location']
        self.boolify(vars)

    def post(self, command, output_dir, vars):
        if not vars['runs_sshd']:
            path = os.path.join(output_dir, 'files', 'etc', 'ssh')
            if os.path.exists(path):
                rmtree(path)

# vim:set et sts=4 ts=4 tw=80:
