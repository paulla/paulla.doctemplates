#/usr/bin/env/python

import os
from shutil import rmtree

from paste.script.templates import var
from base import HostBaseTemplate, getdefaults



class HostBsdBaseTemplate(HostBaseTemplate):
    pass


class HostLinuxBaseTemplate(HostBaseTemplate):
    pass


class HostDebianLikeBaseTemplate(HostLinuxBaseTemplate):
    pass


class FreeBsdTemplate(HostBsdBaseTemplate):
    """."""
    _template_dir = 'tmpl/BSD/FreeBSD'
    defaults = getdefaults('FreeBSD')
    summary = "A FreeBSD doc template."

    vars = HostBsdBaseTemplate.vars + \
           [var('has_jails', 'This host runs jails',
                default=defaults['has_jails']),
            var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']
        self.boolify(vars)

    def post(self, command, output_dir, vars):
        HostBsdBaseTemplate.post(self, command, output_dir, vars)
        if not vars['has_jails']:
            path = os.path.join(output_dir, 'jails')
            if os.path.exists(path):
                rmtree(path)


class DebianTemplate(HostDebianLikeBaseTemplate):
    """."""
    _template_dir = 'tmpl/GNU-Linux/Debian'
    defaults = getdefaults('Debian')
    summary = "A Debian doc template."

    vars = HostDebianLikeBaseTemplate.vars + \
           [ var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']
        self.boolify(vars)


class UbuntuTemplate(HostDebianLikeBaseTemplate):
    """."""
    _template_dir = 'tmpl/GNU-Linux/Ubuntu'
    defaults = getdefaults('Ubuntu')
    summary = "An Ubuntu doc template."

    vars = HostDebianLikeBaseTemplate.vars + \
           [ var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']
        self.boolify(vars)


class OpenBsdTemplate(HostBsdBaseTemplate):
    """."""
    _template_dir = 'tmpl/BSD/OpenBSD'
    defaults = getdefaults('OpenBSD')
    summary = "A OpenBSD doc template."

    vars = HostBsdBaseTemplate.vars + \
           [ var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']
        self.boolify(vars)


class NetBsdTemplate(HostBsdBaseTemplate):
    """."""
    _template_dir = 'tmpl/BSD/NetBSD'
    defaults = getdefaults('NetBSD')
    summary = "A NetBSD doc template."

    vars = HostBsdBaseTemplate.vars + \
           [ var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']
        self.boolify(vars)

# vim:set et sts=4 ts=4 tw=80:
