# LibraryTemplate

## Overview

This CMake Library Template serves as a foundation for writing libraries with the added convenience of automatic
features. The template includes support for automatic precompiled headers, documentation generation using Doxygen, and
easy packaging for distribution.

## Features

### Automatic Precompiled Headers

The CMake configuration scans the library source code, identifying includes with angled brackets, and generates a
precompiled header for improved compilation efficiency.

### Automatic Documentation

The template automates documentation generation using Doxygen. This ensures that your library's documentation is always
up-to-date and easily accessible.

### Automatic Packaging

When instructed to install, CMake packages the library into a zip file. The packaged file includes documentation and all
necessary components for building the code. However, it excludes the packaging logic and testing, ensuring a clean
distribution.

## Usage

The library is designed to be automatic, so just configure and build as you would any other project. Add any code to the
CMake lists in [client_prepare.cmake](CMake/client/client_prepare.cmake)
and [client_post_library.cmake](CMake/client/client_post_library.cmake).

## Installation

### Using GitHub Template

1. Visit the [GitHub Repository](https://github.com/an-inconspicuous-semicolon/LibraryTemplate).
2. Click on the "Use this template" button to create a new repository based on this template.
3. Clone your new repository to your local machine.
4. Follow the usage instructions provided in the template.

### Cloning Directly

1. Clone this repository to your local machine:

    ```shell
    git clone https://github.com/an-inconspicuous-semicolon/LibraryTemplate
    ```

2. Follow the usage instructions provided in the template.

## Contributing

We appreciate your interest in this project. While we have a specific vision for this template and, as such, do not
actively seek feature requests, we welcome bug reports and pull requests.

### Bug Reports

If you encounter any issues or unexpected behavior while using the template, please submit a detailed bug report.
Include information such as steps to reproduce the issue, expected behavior, and your environment details. This helps us
address and resolve the problem efficiently.

### Pull Requests

We accept pull requests that address bugs or enhance the template's stability. Before submitting a pull request, ensure
that your changes align with the project's goals and do not introduce new features. Clearly describe the problem your
pull request solves and provide steps for testing.

### Feature Requests

We do not currently accept feature requests, as the template is intentionally designed to meet specific requirements. We
appreciate your understanding in this matter.

We value the community's involvement in maintaining the template's integrity and appreciate any contributions aligned
with the outlined guidelines.

# Licensing

This project is licensed under the Unlicense. See the [LICENSE](LICENSE) file for details.