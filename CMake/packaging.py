# argument 1: the name of the target
# argument 2: the absolute path to the binaries from the target
# argument 3: the absolute path to the root directory of the project
# argument 4: the version of the target
import datetime
import os
import sys
import shutil
import platform
import re
import subprocess


class Packager:
    name: str
    version: str
    library_file_path: str
    binary_path: str
    package_path: str
    packaged_src_path: str
    root_path: str

    def __init__(self, name, version, lib_path, bin_path, pkg_path, root_path):
        self.name = name
        self.version = version
        self.library_file_path = lib_path
        self.binary_path = bin_path
        self.package_path = pkg_path
        self.packaged_src_path = f"{self.package_path}/{self.name}/"
        self.root_path = root_path
        self.create_directory("")

    def format_string(self, string):
        return string.replace("//", "/")

    def create_directory(self, path_from_pkg, delete_if_exists=True):
        final_dir = self.format_string(f"{self.package_path}/{path_from_pkg}")
        try:

            if os.path.exists(final_dir) and delete_if_exists:
                shutil.rmtree(final_dir)

            os.mkdir(final_dir)
        except BaseException as e:
            print(f"Failed to create directory {final_dir}: {e}")

    def read_file(self, path_from_root) -> str:
        final_file = self.format_string(f"{self.root_path}/{path_from_root}")
        try:
            handle = open(final_file, 'r')
            contents = handle.read()
            handle.close()
            return contents

        except BaseException as e:
            print(f"Failed to read file {final_file}: {e}")

    def read_bin_file(self, path_from_root) -> str:
        final_file = self.format_string(f"{self.binary_path}/{path_from_root}")
        try:
            handle = open(final_file, 'r')
            contents = handle.read()
            handle.close()
            return contents

        except BaseException as e:
            print(f"Failed to read file {final_file}: {e}")

    def write_file(self, path_from_pkg, contents):
        final_file = self.format_string(f"{self.package_path}/{path_from_pkg}")
        try:
            handle = open(final_file, 'w')
            handle.write(contents)
            handle.close()

        except BaseException as e:
            print(f"Failed to write file {final_file}: {e}")

    def install_file(self, path_from_root, path_from_pkg):
        file_to_read = self.format_string(f"{self.root_path}/{path_from_root}")
        final_file = self.format_string(f"{self.package_path}/{path_from_pkg}")

        try:
            shutil.copy2(file_to_read, final_file)
        except BaseException as e:
            print(f"Failed to install {file_to_read} to {final_file}: {e}")

    def install_directory(self, path_from_root, path_from_pkg):
        read_dir = self.format_string(f"{self.root_path}/{path_from_root}")
        final_dir = self.format_string(f"{self.package_path}/{path_from_pkg}")

        try:
            shutil.copytree(read_dir, final_dir)
        except BaseException as e:
            print(f"Failed to install {read_dir} to {final_dir}: {e}")

    def delete_file(self, path_from_pkg):
        final_file = self.format_string(f"{self.package_path}/{path_from_pkg}")
        try:
            os.remove(final_file)
        except BaseException as e:
            print(f"Failed to remove file {final_file}: {e}")

    def delete_src_file(self, path_from_pkg_src):
        final_file = self.format_string(f"{self.packaged_src_path}/{path_from_pkg_src}")
        try:
            os.remove(final_file)
        except BaseException as e:
            print(f"Failed to remove file {final_file}: {e}")

    def install_src_directory(self, path_from_root, path_from_pkg_src):
        read_dir = self.format_string(f"{self.root_path}/{path_from_root}")
        final_dir = self.format_string(f"{self.packaged_src_path}/{path_from_pkg_src}")

        try:
            shutil.copytree(read_dir, final_dir)
        except BaseException as e:
            print(f"Failed to install {read_dir} to {final_dir}: {e}")

    def install_src_file(self, path_from_root, path_from_pkg_src):
        file_to_read = self.format_string(f"{self.root_path}/{path_from_root}")
        final_file = self.format_string(f"{self.packaged_src_path}/{path_from_pkg_src}")

        try:
            shutil.copy2(file_to_read, final_file)
        except BaseException as e:
            print(f"Failed to install {file_to_read} to {final_file}: {e}")

    def write_src_file(self, path_from_pkg_src, contents):
        final_file = self.format_string(f"{self.packaged_src_path}/{path_from_pkg_src}")
        try:
            handle = open(final_file, 'w')
            handle.write(contents)
            handle.close()

        except BaseException as e:
            print(f"Failed to write file {final_file}: {e}")

    def package(self):
        shutil.make_archive(f"{self.binary_path}/{self.name}", 'zip', self.package_path)


class DoxygenInstance:
    def __init__(self, doxyfile_path):
        self.doxygen_executable = self.find_doxygen_executable()
        self.config = self.load_doxyfile(doxyfile_path)

    def find_doxygen_executable(self):
        try:
            result = subprocess.run(["doxygen.exe", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True)
            if result.returncode == 0:
                return "doxygen"
        except FileNotFoundError:
            print("Error: Doxygen executable not found. Please install Doxygen or ensure it is in the system's PATH.")
            exit(1)

    def load_doxyfile(self, doxyfile_path):
        try:
            with open(doxyfile_path, 'r') as file:
                doxyfile_content = file.read()
        except FileNotFoundError:
            print(f"Error: Doxyfile not found at '{doxyfile_path}'.")
            exit(1)

        # Parse the Doxyfile content into a dictionary (simple key-value pairs)
        config = doxyfile_content

        return config

    def build(self, output_path, pkger):
        # Create a temporary Doxyfile with the modified configuration

        handle = open(pkger.binary_path + "/Doxyfile.in", 'w')
        lines_found = [False, False, False, False]

        for line in self.config.splitlines():
            if "OUTPUT_DIRECTORY" in line:
                lines_found[0] = True
                handle.write(f"OUTPUT_DIRECTORY       = {output_path}\n")
                continue
            elif "PROJECT_NAME" in line:
                lines_found[1] = True
                handle.write(f"PROJECT_NAME           = {pkger.name}\n")
                continue
            elif "PROJECT_NUMBER" in line:
                lines_found[2] = True
                handle.write(f"PROJECT_NUMBER         = {pkger.version}\n")
                continue
            elif "INPUT " in line:
                lines_found[3] = True
                handle.write(
                    f"INPUT = {pkger.root_path}/README.md {pkger.root_path}/Documentation {pkger.root_path}/Library\n")
                continue
            else:
                handle.write(line + "\n")

        if not lines_found[0]:
            handle.write(f"OUTPUT_DIRECTORY       = {output_path}\n")
        if not lines_found[1]:
            handle.write(f"PROJECT_NAME           = {pkger.name}\n")
        if not lines_found[2]:
            handle.write(f"PROJECT_NUMBER         = {pkger.version}\n")
        if not lines_found[3]:
            handle.write(
                f"INPUT = {pkger.root_path}/README.md {pkger.root_path}/Documentation {pkger.root_path}/Library\n")

        handle.close()
        # Run Doxygen with the temporary Doxyfile
        try:
            subprocess.run([self.doxygen_executable, pkger.binary_path + '/Doxyfile.in'], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error: Doxygen failed to build. {e}")


class CMakeCacheReader:
    def __init__(self, cmake_cache_file):
        self.cmake_cache_file = cmake_cache_file
        self.cache_data = self._read_cache_file()

    def _read_cache_file(self):
        try:
            with open(self.cmake_cache_file, 'r') as f:
                content = f.read()
                cache_data = dict(re.findall(r'(\w+):\w+=([^\n]+)', content))
                return cache_data
        except Exception as e:
            print(f"Error reading CMakeCache.txt: {e}")
            return {}

    def get_variable(self, variable_name):
        return self.cache_data.get(variable_name, None)

    def get_cmake_args(self):
        return os.environ.get('CMAKE_CACHE_ARGS', '').split(';')


def get_git_info():
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
        name = subprocess.check_output(['git', 'config', '--global', 'user.email']).strip().decode('utf-8')
        return commit_hash, branch, name
    except Exception as e:
        print(f"Error getting Git information: {e}")
        return None, None, None


print(f"-- Packaging {sys.argv[1]}")

binary_file = sys.argv[2]
binary_dir = os.path.dirname(binary_file)
packager = Packager(sys.argv[1], sys.argv[4], binary_file, binary_dir, binary_dir + "/package", sys.argv[3])

print("--- Creating temporary directories")
packager.create_directory(packager.name)

print("--- Installing Libraries")
packager.install_src_directory("Libraries", "Libraries")

print("--- Installing Sources")
packager.install_src_directory("Library", "Library")

print("--- Installing CMakeLists.txt")
lists_contents = packager.read_file("CMakeLists.txt")
lists_contents = lists_contents.replace("include(CMake/packaging.cmake)", "# Packaging Removed")
lists_contents = lists_contents.replace("prepare_for_packaging(${PROJECT_NAME})", "# Packaging Removed")
lists_contents = lists_contents.replace("include(CMake/client.cmake)", "# Client Removed")
packager.write_src_file("CMakeLists.txt", lists_contents)

print("--- Installing CMake Utilities")
packager.install_src_directory("CMake", "CMake")
packager.delete_src_file("CMake/packaging.cmake")
packager.delete_src_file("CMake/packaging.py")

print("--- Generating Documentation")
packager.install_src_directory("Documentation", "Documentation")
doxyfile_path = packager.format_string(packager.root_path + "/Documentation/Doxyfile.in")
doxygen_output_path = packager.format_string(packager.package_path + "/Documentation")

doxygen_instance = DoxygenInstance(doxyfile_path)
doxygen_instance.build(doxygen_output_path, packager)

print("--- Installing License")
packager.install_file("LICENSE", "LICENSE")

print("--- Generating tag file")

toolchain = packager.read_bin_file(f"__{packager.name}_toolchain.txt").splitlines()

cmake_cache_file = binary_dir + "/CMakeCache.txt"
cmake_cache_reader = CMakeCacheReader(cmake_cache_file)

current_date = datetime.date.today()
compiler_info = f"{os.environ.get('CXX', 'Unknown compiler')} {os.environ.get('CXX_VERSION', 'Unknown version')}"
git_commit_hash, git_branch, git_user = get_git_info()

build_type = cmake_cache_reader.get_variable("CMAKE_BUILD_TYPE")

cmake_version_output = subprocess.check_output(['cmake', '--version'], universal_newlines=True)
version_lines = cmake_version_output.strip().split('\n')
cmake_version = version_lines[0].split()[-1]

cmake_options = cmake_cache_reader.get_cmake_args()

platform_name = platform.system()
platform_arch = platform.architecture()[0]

tag_file = f"""\
---------------------------------------------------
Library Name: {packager.name}
Library Version: {packager.version}

Build Information:
    Date: {current_date.strftime("%d/%m/%y")}
    Builder: {git_user}
    Compiler: {toolchain[0]} {toolchain[1]}
    Type: {build_type}
    
Git Information:
    Commit Hash: {git_commit_hash}
    Branch: {git_branch}
    
CMake Information:
    Version: {cmake_version}
    Options: {cmake_options}
    
Platform Information:
    OS: {platform_name}
    Architecture: {platform_arch}
---------------------------------------------------
"""

packager.write_file("build_info.txt", tag_file)

print("--- Writing Package")
packager.package()

print("-- Packaged project")
