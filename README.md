# README - recon-ng-maltego v1.0

Author: J. David Bressler (@bostonlink), GuidePoint Security, LLC.<br />
Demo Video: http://youtu.be/bDnONoFJdQg

## 1.0 About

12/10/2013 - Currently integrating to new version of recon-ng, have to change all path locations to reference workspaces.  Be patient.

recon-ng-maltego is a local maltego transform pack built with the Canari Framework that integrates recon-ng data into maltego graphs.  It also enables you to launch module categories such as hosts, contacts, and pushpin modules directly from Maltego and query the results to create a graph.

Directory Structure:

* `src/recon-ng-maltego` directory is where all the magic stuff goes and happens.
* `src/recon-ng-maltego/transforms` directory is where all the transform modules are located.
* `src/recon-ng-maltego/transforms/common` directory is where common code for all transforms are stored.
* `src/recon-ng-maltego/transforms/common/entities.py` is where custom entities are defined.
* `maltego/` is where the Maltego entity exports are stored.
* `src/recon-ng-maltego/resources/maltego` directory is where the `entities.mtz` and `*.machine` files are stored for auto install and uninstall.

## 2.0 - Installation

### 2.1 - Supported Platforms
nextego has currently been tested on Mac OS X and Linux.

### 2.2 - Requirements
nextego is supported and tested on Python 2.7.3

The canari framework must be installed to use this package
See: https://github.com/allfro/canari

### 2.3 - How to install
Once you have the Canari framework installed and working, follow the directions below to install recon-ng-maltego

Install the package:

```bash
$ git clone [repo]
$ cd recon-ng-maltego
$ python setup.py install
```
Then install the recon-ng-maltego package by issuing the following command:

```bash
$ canari create-profile recon-ng-maltego
```
Then do the following (thanks to Nadeem Douba @ndouba):

INSTRUCTIONS:

1. Open Maltego.
2. Click on the home button (Maltego icon, top-left corner).
3. Click on 'Import'.
4. Click on 'Import Configuration'.
5. Follow prompts.
6. Enjoy!

Once installed you must edit the recon-ng-maltego.conf configuration file.

```bash
$ vim ~/.canari/recon-ng-maltego.conf
```
All Done!!  Happy Hunting!
