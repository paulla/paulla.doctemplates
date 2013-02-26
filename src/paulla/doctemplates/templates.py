#/usr/bin/env/python

import os
from shutil import rmtree, copy
from distutils.dir_util import copy_tree

from paste.script.templates import var
from base import HostBaseTemplate, getdefaults



class HostBsdBaseTemplate(HostBaseTemplate):
    def post(self, command, output_dir, vars):
        HostBaseTemplate.post(self, command, output_dir, vars)
        if not vars['conf_is_versioned']:
            copy_tree(os.path.join(os.path.dirname(__file__), 'tmpl/base/bsd_etc_base/etc'),
                      os.path.join(output_dir, 'files/etc'))

class HostLinuxBaseTemplate(HostBaseTemplate):
    def post(self, command, output_dir, vars):
        HostBaseTemplate.post(self, command, output_dir, vars)
        if not vars['has_vm']:
            path = os.path.join(output_dir, 'vms')
            if os.path.exists(path):
                rmtree(path)


class HostDebianLikeBaseTemplate(HostLinuxBaseTemplate):
    def post(self, command, output_dir, vars):
        HostLinuxBaseTemplate.post(self, command, output_dir, vars)
        if not vars['conf_is_versioned']:
            copy_tree(os.path.join(os.path.dirname(__file__), 'tmpl/base/gnu-linux-debian-base/etc'),
                      os.path.join(output_dir, 'files/etc'))


class FreeBsdTemplate(HostBsdBaseTemplate):
    """."""
    _template_dir = 'tmpl/BSD/FreeBSD'
    defaults = getdefaults('FreeBSD')
    summary = "A FreeBSD doc template."

    vars = HostBsdBaseTemplate.vars + \
           [var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        HostBsdBaseTemplate.pre(self, command, output_dir, vars)
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']

    def post(self, command, output_dir, vars):
        HostBsdBaseTemplate.post(self, command, output_dir, vars)
        if not vars['has_vm']:
            path = os.path.join(output_dir, 'jails')
            if os.path.exists(path):
                rmtree(path)
        if not vars['conf_is_versioned']:
            usr_local_path = os.path.join(output_dir, 'files/usr/local/etc/')
            if not os.path.exists(usr_local_path):
                os.makedirs(usr_local_path)
            fstab_file = os.path.join(output_dir, 'files/etc/fstab')
            if os.path.exists(fstab_file):
                os.remove(fstab_file)
        if not vars['runs_sshd']:
            path = os.path.join(output_dir, 'files', 'etc', 'ssh')
            if os.path.exists(path):
                rmtree(path)



class FreeBsdJailTemplate(FreeBsdTemplate):
    """."""
    _template_dir = 'tmpl/BSD/FreeBSD-jail'
    defaults = getdefaults('FreeBSD-jail')
    summary = "A FreeBSD  Jail doc template."

    vars = HostBsdBaseTemplate.vars + \
           [var('runs_sshd', 'runs sshd',
                default=defaults['runs_sshd']),
           ]

    def pre(self, command, output_dir, vars):
        """."""
        HostBsdBaseTemplate.pre(self, command, output_dir, vars)
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']


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
        HostDebianLikeBaseTemplate.pre(self, command, output_dir, vars)
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']


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
        HostDebianLikeBaseTemplate.pre(self, command, output_dir, vars)
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']


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
        HostBsdBaseTemplate.pre(self, command, output_dir, vars)
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']

    def post(self, command, output_dir, vars):
        HostBsdBaseTemplate.post(self, command, output_dir, vars)
        if not vars['conf_is_versioned']:
            rc_conf_file = os.path.join(output_dir, 'files/etc/rc.conf')
            if os.path.exists(rc_conf_file):
                os.remove(rc_conf_file)
#            copy(os.path.join(os.path.dirname(__file__),
#                             'tmpl/base/bsd_etc_base/openbsd_etc/rc.conf.local'),
#                 os.path.join(output_dir, 'files/etc/rc.conf.local'))

            copy_tree(os.path.join(os.path.dirname(__file__), 'tmpl/base/bsd_etc_base/openbsd_etc/'),
                      os.path.join(output_dir, 'files/etc'))

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
        HostBsdBaseTemplate.pre(self, command, output_dir, vars)
        if not 'os' in vars.keys():
            vars['os'] = self.defaults['os']

# vim:set et sts=4 ts=4 tw=80:
