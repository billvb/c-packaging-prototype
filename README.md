# cpak - An approach toward C library package management


## Description

This is a prototype/proof-of-concept for a C package manager.



## Motivation and Intention

The existing ecosystem of C packages and libraries is far too heterogenous to be centralized in one package management framework. 
However, organizations that must maintain a large set of internal libraries or utilities to use across their applications in a consistent manner may benefit from such a centralized package management system.

This prototype package manager simplifies the task of fetching dependencies for a local project (similar to Python's *virtualenv*).
It separately compiles each library from source such that conflicts in coding standards will not inihibit the overall build of the host application.

This repository simply contains a brief proof-of-concept of this package management system: a prototype utility written in python `cpak.py` and two sample package.
The sample packages include a basic (dependency-free) library as well as one depending on another.


## Getting the demo up-and-running

Adding the package manager to your system path (bash)...

    $ pushd .
    $ cd sample-repo/packager/
    $ export PATH=${PATH}:`pwd`
    $ popd

    $ pushd .
    $ cd sim-repository
    $ export CPAK_REPO_ROOT=`pwd`
    $ popd


## Usage of cpak in a sample project

The sample contained here shows a host application *your-project* depending on two other packages: *sample* and *extender*.
The *sample* project simply contains a "hello world" function, and the *extender* package is an example of a package with dependencies (in this case depending on *sample*).

Both *sample* and *extender* are compiled with the strictest possible flags for ANSI C, whereas the host application is much more permissive.

Using the package manager in a new project...

    # Intializing the package manager environment
    $ cd your-project/
    $ cpak.py init
    
    # Checking out the sample project
    $ cpak.py install sample
    ...
    $ cpak.py install extender
    ...
    $ make
    ...
    $ ./your-project.bin ARGS
    ...
    $ make clean
    

## Future Development

Among future development features:

* A package-details file describing the library's coding standard (e.g., ANSI, C99, GNU, etc..).
* Recursive dependency fetching.
* Better approach toward structuring, storing, and fetching the packages.
* Package version numbering.
* Many others...
