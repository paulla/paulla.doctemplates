#/usr/bin/env/python

import ConfigParser
import os.path
from shutil import rmtree
from distutils.dir_util import copy_tree
from paste.script.templates import Template, var
from IPy import IP

_dir, _f = os.path.split(os.path.abspath(__file__))
DEFAULT_CONFIG_FILE = os.path.join(_dir, 'etc', 'defaults.cfg')
BOOLEANS = ['False', 'True', '1', '0']


idx_summary = """
%s
=========================

Content:

.. toctree::
   :maxdepth: 2\n  \n"""



versioned_conf_cfg_tmpl = """
[buildout]
extensions =
    mr.developer

auto-checkout =


[sources]

"""


def append_lines(filename, text):
    with open(filename, 'a') as idx_file:
        idx_file.writelines(text)


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
    gen_defaults = getdefaults('General')

    vars = Template.vars + \
           [var('desc', 'Host description', default=''),
            var('domain', 'Domaine', default=gen_defaults['domain']),
            var('group', 'group', default=gen_defaults['group']),
            var('location', 'location', default=gen_defaults['location']),
            var('ip4s', 'inet-ip1, inet-ip2, ...', default=""),
            var('ip6s', 'inet6-ip1, inet6-ip2, ...', default=""),
            var('parent', 'parent, hosted on dom0 : parent name',
                default=''),
            var('vm_list', 'VM | jail list:"hostname1, hostname2 ..."',
                default=''),
           ]

    def boolify(self, vars):
        """."""
        unset = ['none', 'false', '0', 'n']
        for key in vars.keys():
            if isinstance(vars[key], basestring):
                if vars[key].lower() in unset:
                    vars[key] = False

    def check_ip(self, vars):
        """."""
        if vars['ip4s']:
            vars['ip4s'] = [str(IP(net.strip())) for net
                            in vars['ip4s'].split(',')]

        if vars['ip6s']:
            vars['ip6s'] = [str(IP(net.strip())) for net
                            in vars['ip6s'].split(',')]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'group' in vars.keys():
            vars['group'] = self.gen_defaults['group']
        if not 'location' in vars.keys():
            vars['location'] = self.gen_defaults['location']
        if not 'versioned_conf_cfg_file' in vars.keys():
            vars['versioned_conf_cfg_file'] = self.gen_defaults['versioned_conf_cfg_file']
        if not 'conf_is_versioned' in vars.keys():
            vars['conf_is_versioned'] = self.gen_defaults['conf_is_versioned']
        if not 'default_dcvs_url' in vars.keys():
            vars['default_dcvs_url'] = self.gen_defaults['default_dcvs_url']
        if not 'default_dcvs' in vars.keys():
            vars['default_dcvs'] = self.gen_defaults['default_dcvs']

        self.boolify(vars)
        self.check_ip(vars)
        vars['has_vm']= bool(vars['vm_list'])

    def post(self, command, output_dir, vars):
        if not vars['runs_sshd']:
            path = os.path.join(output_dir, 'files', 'etc', 'ssh')
            if os.path.exists(path):
                rmtree(path)

        txt = '   %s/index.rst\n' % vars['project']
        if not os.path.exists(os.path.join(os.getcwd(), 'index.rst')):
            direc = os.getcwd().split(os.sep)[-1]
            txt = (idx_summary % direc)+ txt
        append_lines(os.path.join(os.getcwd(), 'index.rst'), txt)

        if not vars['conf_is_versioned']:
            copy_tree(os.path.join(os.path.dirname(__file__), 'tmpl/base/common_base/etc'),
                      os.path.join(output_dir, 'files/etc'))

        else:
            versioned_conf_cfg_file = os.path.join(os.getcwd(),
            vars['versioned_conf_cfg_file'])
            if not os.path.exists(versioned_conf_cfg_file):
                append_lines(versioned_conf_cfg_file, versioned_conf_cfg_tmpl)


# vim:set et sts=4 ts=4 tw=80:
