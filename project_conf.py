# single point for all configuration of the project

# stdlib
from typing import List, Dict
import project_conf_module

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
# travis_pypi_secure_code = '- secure: "<code>"'     # pypi secure password
travis_pypi_secure_code = '- secure: "D0IYa8wbsRaTA6Qu1ZK4umqXyOHhBTEW06aLp6cZhwSsWEF4issnnw+bNv3vOF3j1bAOrgNmRxzMYPeaYawUzslJDXWAYCoEE6f//uSGlU7OJbK5btxbtG03uNRhmwMH9K8h2SP0pGivwWMJpTdjHJk+rL6BSjBye9tyr77HQupBM5l6HKeK+Z/6pJl4SBLZw1PZo+x95w/2LuvJlrWFgJ8STS6MJ1PFSmCave1wEq44g87Yin1eCiyYGojxfjKB9Y2R68NY+vTqGor0ltEZ5zPJ2c2nQ2z4XrtgUjJAeh6Ud0iznTPXnnT9X4ZfKG29O/FXVu/X2pIQ6ESbYJg+9uMFxVbecUw3LKTTqOCgp7BRAadvEq8HCmzoh/pSr1z0p+cKf/cTKxmF8pE6p3/6zkSkh7wloYoPld82uIB0rKFjnL9Tprv80RYex9oak1f1cHOvMwha5fO5a7aEvQkFqaM2s/nJpwMGR/PiG1RYfK0lC5abc0FXPJg017rC3d+kbMBjXcCfU0OzJIdp0la8LVyZjKXGlYMzx4JqgiZM1z826aSOh4s3nMQZ1JVAiUUPxHelX6zJTkYCX/JNB4SWOjx+lEYc+76YT8lcu+zDT+NpJpzJjx3oDCqdnTcZukCIQc444IfCF3OI2e1JP+jm0IOqLaMYuPSgM6L+bUX+J1w="'

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

# #############################################################################################################################################################
# DEFAULT SETTINGS - no need to change usually
# #############################################################################################################################################################

travis_repo_slug = github_account + '/' + package_name


# Entry Points Example :
# need to create __main__.py:
#   from . import <module_name>
#   <module_name>.main()
shell_command = package_name
src_dir = package_name
module_name = package_name
init_config_title = package_name
init_config_name = package_name

# entry_points = {'console_scripts': ['{shell_command} = {src_dir}.{module_name}:main'
#                 .format(shell_command=shell_command, src_dir=src_dir, module_name=module_name)]}  # type: Dict[str, List[str]]

entry_points = dict()  # type: Dict[str, List[str]]

description = package_name  # short description - should be entered here
long_description = package_name  # will be overwritten with the content of README.rst if exists
packages = [package_name]
url = 'https://github.com/{github_account}/{package_name}'.format(github_account=github_account, package_name=package_name)
github_master = 'git+https://github.com/{github_account}/{package_name}.git'.format(github_account=github_account, package_name=package_name)

CLASSIFIERS = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Software Development :: Libraries :: Python Modules']


if __name__ == '__main__':
    project_conf_module.create_init_config_file(src_dir=src_dir, version=version, init_config_title=init_config_title, init_config_name=init_config_name)

    # copy files from template folder to current project
    if not project_conf_module.is_in_project_template_folder():     # we dont want to copy if we run this in the template project itself
        project_conf_module.copy_template_files(badges_with_jupiter=badges_with_jupiter)

    # create travis file
    project_conf_module.create_travis_file(linux_tests=linux_tests, osx_tests=osx_tests, pypy_tests=pypy_tests, windows_tests=windows_tests,
                                           wine_tests=wine_tests, package_name=package_name, cc_test_reporter_id=cc_test_reporter_id,
                                           travis_pypi_secure_code=travis_pypi_secure_code, travis_repo_slug=travis_repo_slug, github_master=github_master)

    # create readme.rst
    import build_docs
    build_docs_args = dict()
    build_docs_args['<TRAVIS_REPO_SLUG>'] = '{}/{}'.format(github_account, package_name)
    build_docs.main(build_docs_args)
