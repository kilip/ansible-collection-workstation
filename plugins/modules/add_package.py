# Copyright: (c) 2022, Anthonius Munthi <me@itstoni.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type



DOCUMENTATION = '''
---
module: add_package
short_description: Adding package to install
description: This module will add package to install in.
author:
  - Anthonius Munthi (@kilip)
options:
  package:
    description:
      - Package name
      - Syntax varies with package manager. For example C(name-1.0) or C(name=1.0).
      - Package names also vary with package manager; this module will not "translate" them per distro. For example C(libyaml-dev), C(libyaml-devel).
    required: false
  brew:
    description:
      - Brew package name
    required: false
'''

EXAMPLES = r'''
# Pass in a message
- name: Add one package
    kilip.workstation.add_package:
    package: git
# Add brew package
- name: Add brew package
    kilip.workstation.add_package:
        package: direnv
# Adding a list of package
- name: Add brew and os package
  kilip.workstation.add_package:
    package:
      - git
      - gnupg
    brew:
      - direnv
      - chezmoi
      - phpbrew
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
ansible_facts:
  description: The original name param that was passed in.
  type: dict
  returned: always
'''
