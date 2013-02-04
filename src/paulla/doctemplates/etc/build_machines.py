#!/usr/bin/env python
# -*- coding: utf-8 -*-

__docformat__ = 'restructuredtext en'

"""Doc here.
"""
import csv
import os

cur_dir = os.getcwd()
cmd_tmpl = cur_dir + '/bin/paster create %s --no-interactive'
base_args_tmpl = """-t %(os)s %(hostname)s """
base_path = os.path.join(cur_dir, 'source', 'machines')


def get_hosts(filename='hosts.csv'):
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        return [row for row in reader]


def write_file(lines, filename='build_doc.sh'):
    with open(filename, 'w') as sh_file:
        sh_file.writelines(lines)


def build_sh(hosts):
    lines = []
    cd_path = 'cd %s'
    mk_dir_path = 'mkdir -p %s'

    for host in hosts:
        host_path = os.path.join(base_path, host['group'])
        if host['parent']:
            vm_path = 'jails' if host['os'] == 'freebsd-jail' else 'vms'
            host_path = os.path.join(base_path, host['group'], host['parent'],
                vm_path)
        lines.append(mk_dir_path % host_path)
        lines.append(cd_path % host_path)
        args = ['%s="%%(%s)s" ' % (key, key) for key in host.keys()]
        host_args = (base_args_tmpl + ''.join(args)) % host
        lines.append(cmd_tmpl % host_args)

    write_file('\n'.join(lines))

if __name__ == '__main__':

    hosts = get_hosts()
    build_sh(hosts)

# vim:set et sts=4 ts=4 tw=80:
