# MirrorImagesPortrait

## Table of contents

1. [Overview](#overview)
1. [Installation](#installation)
	1. [Removal](#removal)
1. [License](#license)

## Overview

The [MirrorCommandLine](https://gitlab.com/doctorfree/MirrorCommandLine) project
creates config files for a [MagicMirror](https://magicmirror.builders/). Many of
these config files are used to display images located in the MirrorCommandLine
installation folders. However, these images are not installed by default in the
base MirrorCommandLine package as they are not required for most of the
functionality of the MagicMirror. In order to enable preconfigured image display
of the MirrorCommandLine config files, install these packages on a MagicMirror
which has the MirrorCommandLine package installed.

The images in these packages have been tailored for a MagicMirror in portrait mode.
For landscape mode images, see the
[MirrorImagesLandscape](https://gitlab.com/doctorfree/MirrorImagesLandscape) project.

## Installation

To install:

[Download the latest Debian package format releases](https://gitlab.com/doctorfree/MirrorImagesPortrait/-/releases)

Install the MirrorImagesPortrait packages by executing the commands:
```bash
sudo apt install MirrorImagesPortrait_<version>.deb
sudo apt install ArtistsPortrait_<version>.deb
sudo apt install ModelsPortrait_<version>.deb
sudo apt install PhotographersPortrait_<version>.deb
```

Alternately, you can clone this repository, create your own packages, and
install from source. To do so, clone the repository:

<code>git clone `https://gitlab.com/doctorfree/MirrorImagesPortrait.git`</code>

Use the `mkpkg` script to create Debian format packages on a system with
the prerequisite packaging development environment. Once packages have been
created in the source repository they can be installed by executing the
`./Install` command. Packages can be removed with `./Uninstall`.

#### Removal

To remove/uninstall the MirrorImagesPortrait packages execute the commands:

```bash
sudo apt remove artists-portrait
sudo apt remove models-portrait
sudo apt remove photographers-portrait
sudo apt remove mirror-images-portrait
```

**Note:** Removal may issue a warning about removing `/usr/local` and other
folders within `/usr/local`. This is an artifact of the Debian packaging system.
If you wish to silence that warning and prevent the Debian packaging system from
trying to remove `/usr/local` then install the
[core-custom-local Debian package](https://gitlab.com/doctorfree/core-custom-local/-/releases).

## License

Copyright: 2021 Ronald Joe Record <ronaldrecord@gmail.com>

License: MIT
