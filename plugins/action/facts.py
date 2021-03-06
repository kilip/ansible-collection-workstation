from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

display = Display()


class ActionModule(ActionBase):
    def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
        super(ActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)

    def run(self, tmp=None, task_vars=None):
        super(ActionModule, self).run(tmp, task_vars)

        user_gpg_keys = list()
        for key, value in task_vars.items():
            if key == 'user_gpg_keys':
                user_gpg_keys = value

        for gpg in user_gpg_keys:
            if 'id' not in gpg.keys():
                filename = gpg['file']
                gpg['id'] = filename.replace('gpg-', '').replace('.key', '').replace('gpg/', '')

        return dict(ansible_facts=dict(user_gpg_keys=user_gpg_keys))
