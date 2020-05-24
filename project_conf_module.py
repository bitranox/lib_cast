# stdlib
import pathlib
import shutil


def create_init_config_file(src_dir: str, version: str, init_config_title: str, init_config_name: str) -> None:
    path_version_py = pathlib.Path(__file__).parent / src_dir / 'init_config.py'
    with open(str(path_version_py), 'w') as f_version_py:
        lines = ["version = '{}'\n".format(version),
                 "title = '{}'\n".format(init_config_title),
                 "name = '{}'\n".format(init_config_name)]
        f_version_py.writelines(lines)


def is_in_project_template_folder() -> bool:
    if pathlib.Path(__file__).parts[-2] == 'lib_travis_python_project_template':
        return True
    else:
        return False


def get_path_template_dir_local() -> pathlib.Path:
    path_current_dir = pathlib.Path(__file__).parent.resolve()
    while True:
        path_current_dir = path_current_dir.parent
        path_current_subdirs = path_current_dir.glob('**/')
        for subdir in path_current_subdirs:
            if subdir.parts[-1] == 'lib_travis_python_project_template':
                return subdir


def copy_template_files(badges_with_jupiter: bool) -> None:
    """
    copy the template files to the current project on the local development machine
    we dont overwrite some files, see code
    """
    files_not_to_copy = ['requirements.txt', 'project_conf.py', 'usage.rst', '.travis.yml', 'README.rst']
    path_source_dir = get_path_template_dir_local()
    path_target_dir = pathlib.Path(__file__).parent.resolve()
    s_path_source_dir = str(path_source_dir)
    s_path_target_dir = str(path_target_dir)
    l_path_sourcefiles = sorted(path_source_dir.glob('**/*'))
    for path_sourcefile in l_path_sourcefiles:
        s_path_sourcefile = str(path_sourcefile)
        s_path_targetfile = s_path_sourcefile.replace(s_path_source_dir, s_path_target_dir, 1)
        if path_sourcefile.is_dir():
            if '/.git' in s_path_targetfile:
                continue
            else:
                pathlib.Path(s_path_targetfile).mkdir(exist_ok=True)
        elif (path_sourcefile.name not in files_not_to_copy) and ('/.git/' not in s_path_sourcefile):
            shutil.copy(s_path_sourcefile, s_path_targetfile)
    if badges_with_jupiter:
        s_path_sourcefile = s_path_source_dir + '/.docs/badges_with_jupyter.rst'
    else:
        s_path_sourcefile = s_path_source_dir + '/.docs/badges_without_jupyter.rst'
    shutil.copy(s_path_sourcefile, s_path_target_dir + '/.docs/badges_project.rst')


def replace_marker(text: str, marker: str, src_filename: str, replace_marker_with_src_file: bool = True) -> str:
    if replace_marker_with_src_file:
        path_base_dir = pathlib.Path(__file__).parent
        path_src_filename = path_base_dir / src_filename
        with open(str(path_src_filename), 'r') as f_src_filename:
            s_src = f_src_filename.read()
            text = text.replace(marker, s_src)
    else:
        text = text.replace(marker, '')
    return text


def create_travis_file(linux_tests: bool, osx_tests: bool, pypy_tests: bool, windows_tests: bool, wine_tests: bool,
                       package_name: str, cc_test_reporter_id: str, travis_pypi_secure_code: str, travis_repo_slug: str, github_master: str) -> None:
    path_base_dir = pathlib.Path(__file__).parent
    text = '{travis_template}\n'
    text = replace_marker(text=text, marker='{travis_template}', src_filename='.travis_template.yml')
    text = replace_marker(text=text, marker='{travis_template_linux_addon}',
                          src_filename='.travis_template_linux_addon.yml', replace_marker_with_src_file=linux_tests)
    text = replace_marker(text=text, marker='{travis_template_osx_addon}',
                          src_filename='.travis_template_osx_addon.yml', replace_marker_with_src_file=osx_tests)
    text = replace_marker(text=text, marker='{travis_template_pypy_addon}',
                          src_filename='.travis_template_pypy_addon.yml', replace_marker_with_src_file=pypy_tests)
    text = replace_marker(text=text, marker='{travis_template_windows_addon}',
                          src_filename='.travis_template_windows_addon.yml', replace_marker_with_src_file=windows_tests)
    text = replace_marker(text=text, marker='{travis_template_wine_addon}',
                          src_filename='.travis_template_wine_addon.yml', replace_marker_with_src_file=wine_tests)
    text = text.replace('{package_name}', package_name)
    text = text.replace('{cc_test_reporter_id}', cc_test_reporter_id)
    text = text.replace('{travis_pypi_secure_code}', travis_pypi_secure_code)
    text = text.replace('{travis_repo_slug}', travis_repo_slug)
    text = text.replace('{github_master}', github_master)
    target_file = path_base_dir / '.travis.yml'
    with open(str(target_file), 'w') as f_target_file:
        f_target_file.write(text)
