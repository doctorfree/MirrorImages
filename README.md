# MirrorImages

## Table of contents

1. [Overview](#overview)
1. [Installation](#installation)
	1. [Package Sizes](#package-sizes)
	1. [Removal](#removal)
1. [License](#license)

## Overview

The [MirrorCommand](https://gitlab.com/doctorfree/MirrorCommand) project
creates config files for a [MagicMirror](https://magicmirror.builders/). Many of
these config files are used to display images located in the MirrorCommand
installation folders. However, these images are not installed by default in the
base MirrorCommand package as they are not required for most of the
functionality of the MagicMirror. In order to enable preconfigured image display
of the MirrorCommand config files, install these packages on a MagicMirror
which has the MirrorCommand package installed.

The images in these packages have been tailored for use by a MagicMirror
with the MirrorCommand package installed. MirrorImages packages are provided
in both portrait and landscape mode. Select the MirrorImages package(s)
suitable for the orientation of your MagicMirror.

## Installation

These packages all depend upon the
[MirrorCommand](https://gitlab.com/doctorfree/MirrorCommand)
package which must be previously installed.

To install MirrorCommand:

[Download the latest Debian package format release](https://gitlab.com/doctorfree/MirrorCommand/-/releases)

Install the base MirrorCommand package by executing the command

```bash
sudo apt install MirrorCommand_<version>-<release>.deb
```

To install the MirrorImage packages:

[Download the latest Debian package format releases](https://gitlab.com/doctorfree/MirrorImages/-/releases)

Install the MirrorImages packages by executing the commands:

```bash
sudo apt install ImagesPortrait_<version>-<release>.deb
sudo apt install ArtistsPortrait_<version>-<release>.deb
sudo apt install JavPortrait_<version>-<release>.deb
sudo apt install ModelsPortrait_<version>-<release>.deb
sudo apt install PhotographersPortrait_<version>-<release>.deb
sudo apt install TantraTutorial_<version>-<release>.deb
```

or

```bash
sudo apt install ImagesLandscape_<version>-<release>.deb
sudo apt install ArtistsLandscape_<version>-<release>.deb
sudo apt install JavLandscape_<version>-<release>.deb
sudo apt install ModelsLandscape_<version>-<release>.deb
sudo apt install PhotographersLandscape_<version>-<release>.deb
sudo apt install TantraTutorial_<version>-<release>.deb
```

Alternately, you can clone this repository, create your own packages, and
install from source.

To do so, clone the repository:

<code>git clone `https://gitlab.com/doctorfree/MirrorImages.git`</code>

Use the [./mkpkg](mkpkg) script to create Debian format packages on a system with
the prerequisite packaging development environment. Once packages have been
created in the source repository they can be installed by executing the
[./Install](Install) command. Packages can be removed with [./Uninstall](Uninstall).

**Note:** The Artists, Models, TantraTutorial, and Photographers image archives
include images of artistic nudity. If you wish to avoid the display of artistic
nudes, only install the ImagesPortrait or ImagesLandscape package.

#### Package Sizes

No image files are included in these packages. Rather, each package downloads
image archives and extracts them into the appropriate locations. Some of these
downloads are relatively large and require sufficient available disk space.

In order to minimize disk space requirements, all packages pipe their downloads
to stdout and extract the compressed archives via that pipe. This results in the
following disk space requirements:

- ArtistsLandscape       5.4G
- JavLandscape           5.0G
- ModelsLandscape        4.7G
- PhotographersLandscape 500M
- ImagesLandscape        375M
- ArtistsPortrait        5.4G
- JavPortrait            5.0G
- ModelsPortrait         4.7G
- PhotographersPortrait  500M
- TantraTutorial         387M
- ImagesPortrait         375M

Prior to downloading and extracting the image archives the installation script
will provide a prompt allowing the installer to skip larger downloads if desired.

All image archives are extracted into `/usr/local/MirrorCommand/pics-landscape/`,
`/usr/local/MirrorCommand/pics-portrait/`, and `/usr/local/MirrorCommand/movies/`

It is possible to configure your system so that those directories reside
on a larger external drive if necessary.

#### Removal

To remove/uninstall the MirrorImages packages execute the commands:

```bash
sudo apt remove artists-portrait
sudo apt remove jav-portrait
sudo apt remove models-portrait
sudo apt remove photographers-portrait
sudo apt remove tantra-tutorial
sudo apt remove images-portrait
```

or

```bash
sudo apt remove artists-landscape
sudo apt remove jav-landscape
sudo apt remove models-landscape
sudo apt remove photographers-landscape
sudo apt remove tantra-tutorial
sudo apt remove images-landscape
```

**Note:** Removal may issue a warning about removing `/usr/local` and other
folders within `/usr/local`. This is an artifact of the Debian packaging system.
If you wish to silence that warning and prevent the Debian packaging system from
trying to remove `/usr/local` then install the
[core-custom-local Debian package](https://gitlab.com/doctorfree/core-custom-local/-/releases).

## License

Copyright: 2021 Ronald Joe Record <ronaldrecord@gmail.com>

License: MIT
