from __future__ import (absolute_import, division, print_function)
from struct import pack
__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display
display = Display


class ActionModule(ActionBase):

    def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
        super(ActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
        self.packages = list()
        self.brew_packages = list()

    def _add_package(self, pkg_stat, args_pkg):
        package = list()

        # normalize arguments
        if isinstance(args_pkg, str):
            package.append(args_pkg)
        elif isinstance(args_pkg, list):
            package = args_pkg

        for pkg in package:
            if pkg not in pkg_stat:
                pkg_stat.append(pkg)
        pkg_stat.sort()
        return pkg_stat


    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = True
        result = super(ActionModule, self).run(tmp, task_vars)

        module_args = self._task.args.copy()
        packages = list()
        brew_packages = list()
        omf_packages = list()

        for key, value in task_vars.items():
            if key == 'packages':
                packages = value
            if key == 'brew_packages':
                brew_packages = value
            if key == 'omf_packages':
                omf_packages = value

        if 'package' in module_args:
            packages = self._add_package(packages, module_args['package'])
        if 'brew' in module_args:
            brew_packages = self._add_package(brew_packages, module_args['brew'])
        if 'omf' in module_args:
            omf_packages = self._add_package(omf_packages, module_args['omf'])

        result['ansible_facts'] = dict(
            packages=packages,
            brew_packages=brew_packages,
            omf_packages=omf_packages
        )
        return result
