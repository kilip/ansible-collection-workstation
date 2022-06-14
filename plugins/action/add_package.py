from __future__ import (absolute_import, division, print_function)
from dis import dis
from struct import pack
from tokenize import String
__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()


class ActionModule(ActionBase):
    def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
        super(ActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)

    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args.copy()
        ws_packages = list()
        for key, value in task_vars.items():
            if key == 'ws_packages':
                ws_packages = value

        package = module_args['package']
        if isinstance(package,str):
            ws_packages.append(package)
        elif isinstance(package, list):
            for pkg in package:
                ws_packages.append(pkg)

        ws_packages.sort()
        return dict(ansible_facts=dict(ws_packages=ws_packages))
