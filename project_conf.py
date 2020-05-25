# single point for all configuration of the project

# stdlib
from typing import List, Dict


package_name = 'lib_cast'  # type: str
version = '0.1.0'
codeclimate_link_hash = '7fa21a0ced3820c5faa9'                                                  # for lib_programname
cc_test_reporter_id = '0f951d4827f32d0835249263a1d4aaab93528cd3987ee0c54db11ee534dc78b1'        # codeclimate coverage id for lib_programname

# pypi_password
# to create the secret :
# cd /<repository>
# travis encrypt -r bitranox/lib_parameter pypi_password=*****
# copy and paste the encrypted password here
# replace with:
# travis_pypi_secure_code = '<code>'     # pypi secure password, without '"'
travis_pypi_secure_code = 'D0IYa8wbsRaTA6Qu1ZK4umqXyOHhBTEW06aLp6cZhwSsWEF4issnnw+bNv3vOF3j1bAOrgNmRxzMYPeaYawUzslJDXWAYCoEE6f//uSGlU7OJbK5btxbtG03uN'\
                          'RhmwMH9K8h2SP0pGivwWMJpTdjHJk+rL6BSjBye9tyr77HQupBM5l6HKeK+Z/6pJl4SBLZw1PZo+x95w/2LuvJlrWFgJ8STS6MJ1PFSmCave1wEq44g87Yin1e'\
                          'CiyYGojxfjKB9Y2R68NY+vTqGor0ltEZ5zPJ2c2nQ2z4XrtgUjJAeh6Ud0iznTPXnnT9X4ZfKG29O/FXVu/X2pIQ6ESbYJg+9uMFxVbecUw3LKTTqOCgp7BRAa'\
                          'dvEq8HCmzoh/pSr1z0p+cKf/cTKxmF8pE6p3/6zkSkh7wloYoPld82uIB0rKFjnL9Tprv80RYex9oak1f1cHOvMwha5fO5a7aEvQkFqaM2s/nJpwMGR/PiG1RY'\
                          'fK0lC5abc0FXPJg017rC3d+kbMBjXcCfU0OzJIdp0la8LVyZjKXGlYMzx4JqgiZM1z826aSOh4s3nMQZ1JVAiUUPxHelX6zJTkYCX/JNB4SWOjx+lEYc+76YT8'\
                          'lcu+zDT+NpJpzJjx3oDCqdnTcZukCIQc444IfCF3OI2e1JP+jm0IOqLaMYuPSgM6L+bUX+J1w='

# include package data files
# package_data = {package_name: ['some_file_to_include.txt']}
package_data = dict()       # type: Dict[str, List[str]]

author = 'Robert Nowotny'
author_email = 'rnowotny1966@gmail.com'
github_account = 'bitranox'

linux_tests = True
osx_tests = True
pypy_tests = True
windows_tests = True
wine_tests = False
badges_with_jupiter = False

# a short description of the Package - especially if You deploy on PyPi !
description = 'cast float, int, time, sizes etc. to human readable text with SI Prefixes and more'

# #############################################################################################################################################################
# DEFAULT SETTINGS - no need to change usually, but can be adopted
# #############################################################################################################################################################

shell_command = package_name
src_dir = package_name
module_name = package_name
init_config_title = description
init_config_name = package_name

# we ned to have a function main_commandline in module module_name - see examples
entry_points = {'console_scripts': ['{shell_command} = {src_dir}.{module_name}:main_commandline'
                .format(shell_command=shell_command, src_dir=src_dir, module_name=module_name)]}  # type: Dict[str, List[str]]

long_description = package_name  # will be overwritten with the content of README.rst if exists
packages = [package_name]
url = 'https://github.com/{github_account}/{package_name}'.format(github_account=github_account, package_name=package_name)
github_master = 'git+https://github.com/{github_account}/{package_name}.git'.format(github_account=github_account, package_name=package_name)
travis_repo_slug = github_account + '/' + package_name

CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Libraries :: Python Modules']
