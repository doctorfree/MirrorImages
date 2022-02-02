## Release Notes

This release of MirrorImages introduces RPM format installation packages.

MirrorImages 3.0.0 release 1 introduced support for both landscape and portrait mode images. Changes to packaging include the implementation of release creation during the Gitlab continuous integration process.

The MirrorImages project provides several Debian format installation packages that download image archives for use in conjunction with the [MirrorCommand project](https://gitlab.com/doctorfree/MirrorCommand). These packages all depend upon the prior installation of [MirrorCommand version 3.0.1](https://gitlab.com/doctorfree/MirrorCommand/-/releases) or later.

### Installation

To install:

[Download the latest Debian or RPM format packages](https://gitlab.com/doctorfree/MirrorImages/-/releases)

If your system(s) have only landscape mode displays then only the landscape mode packages need be installed. Similarly, the portrait mode packages are intended for installation on systems with portrait mode displays. On systems with multiple displays including both landscape and portrait mode displays, both the landscape and portrait mode packages can be installed and will not conflict with each other. The TantraTutorial package is not display mode dependent and can be installed on systems with either display type.

#### Debian based Linux systems

Install the desired packages on Debian based systems by executing the command
```bash
sudo apt install ./<PackageName>_3.0.0-2.deb
```

Where `<PackageName>` can be any of:

- ArtistsLandscape
- ArtistsPortrait
- CountriesLandscape
- CountriesPortrait
- ImagesLandscape
- ImagesPortrait
- JavLandscape
- JavPortrait
- ModelsLandscape
- ModelsPortrait
- PhotographersLandscape
- PhotographersPortrait
- TantraTutorial

Removal of the package on Debian based systems can be accomplished by issuing the command:

```bash
sudo apt remove <package-name>
```

Where `<package-name>` can be any of:

- images-portrait
- images-landscape
- artists-portrait
- artists-landscape
- countries-portrait
- countries-landscape
- jav-portrait
- jav-landscape
- models-portrait
- models-landscape
- photographers-portrait
- photographers-landscape
- tantra-tutorial

#### RPM based Linux systems

Install the desired packages on RPM based systems by executing the command
```bash
sudo yum install ./<PackageName>_3.0.0-2.rpm
```

Where `<PackageName>` can be any of:

- ArtistsLandscape
- ArtistsPortrait
- CountriesLandscape
- CountriesPortrait
- ImagesLandscape
- ImagesPortrait
- JavLandscape
- JavPortrait
- ModelsLandscape
- ModelsPortrait
- PhotographersLandscape
- PhotographersPortrait
- TantraTutorial

Removal of the package on RPM based systems can be accomplished by issuing the command:

```bash
sudo yum remove <package-name>
```

### Artistic Note

**Note:** The Artists, Countries, Jav, Models, TantraTutorial, and Photographers image archives include images of artistic nudity. If you wish to avoid the display of artistic nudes, only install the ImagesPortrait or ImagesLandscape package.
