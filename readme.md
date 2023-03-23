# LibraryTemplate
A Template for creating c++20 LGPL-3 libraries

## About

### Who is this template for

This template is for anyone who wants to quickly set up a library that uses c++.  
The template is meant to be easy to use, and as automated as possible, so that using it is quick and painless.

### What comes with this template

This template comes with a few things for easing the development of libraries.

- A Library folder with src and include directories.
- Automatic naming of the include folder, to the name of the library.
- Auto-generated `api.hpp` file for handling visibility of symbols
- Automatic dependencies detection
- Automatic test detection
- A Client folder for testing the library

### Why make this template

I made this template because I was sick of the usual half hour it took to 
create a library, to set up a client and testing. So I decided that I would 
create this generic template instead, so that I can copy-paste the template 
to get a working project from the get go.


## How to use it

### Creating the project

There are two options for accessing this template.

1. from GitHub
2. from Git

I recommend the GitHub option because it is easier

#### From GitHub

First, you must have a GitHub account. If you don't have one/Don't want one,
you can use the Git method instead.

Second, to clone the template, go to the template's homepage.  
There will be a green button with `Use This Template`, 
select it and follow the instructions to create your GitHub repository.

Finally, to access your repository, you must clone it, for example
``` shell
git clone https://github.com/your-username-here/your-repo-name
```

#### From Git

For this method we will clone the template repository, 
then replace the version control with your own

First, clone the template
``` shell
git clone https://an-inconspicuous-semicolon/LibraryTemplate your-repo-name
```

Second, delete the `.git` folder from the repo.
``` shell
cd your-repo-name
rm -rf .git
```

Finally, create your own repo using whatever method you choose
``` shell
git init .
```

### Writing the library

#### Renaming the project

The template uses CMake as its build system, so standard practice applies.
1. Edit the `CMakeLists.txt` and change the information inside `project()` to your libraries details
2. reconfigure CMake.
3. Move any files from the old `include/` folder to the new one (the new name of the project)
4. build as usual

#### Adding a dependency

The template makes adding dependencies as easy as possibly, 
just simply add any required CMake dependency to the `Dependencies/` folder,
and the template will automatically include it.  
Then all that is needed is to add the dependency to the libraries `target_link_libraries()` option.

#### Adding a test

Much the same with dependencies, Tests are added by creating a folder within `Testing/` 
and adding a `CMakeLists.txt` file that exports an `add_test()` 