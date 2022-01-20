This major release of MirrorImages introduces support for both landscape and portrait mode images. Changes to packaging include the implementation of release creation during the Gitlab continuous integration process.

The MirrorImages project provides several Debian format installation packages that download image archives for use in conjunction with the [MirrorCommand project](https://gitlab.com/doctorfree/MirrorCommand). These packages all depend upon the prior installation of [MirrorCommand version 3.0.0 release 2](https://gitlab.com/doctorfree/MirrorCommand/-/releases/v3.0.0r2) or later.

To install:

[Download the latest Debian format packages](https://gitlab.com/doctorfree/MirrorImages/-/releases)

If your system(s) have only landscape mode displays then only the landscape mode packages need be installed. Similarly, the portrait mode packages are intended for installation on systems with portrait mode displays. On systems with multiple displays including both landscape and portrait mode displays, both the landscape and portrait mode packages can be installed and will not conflict with each other. The TantraTutorial package is not display mode dependent and can be installed on systems with either display type.

Install the desired packages on Debian based systems by executing the command
```bash
sudo apt install ./<PackageName>_3.0.0-1.deb
```

Where `<PackageName>` can be any of:

- ArtistsLandscape
- ArtistsPortrait
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
- jav-portrait
- jav-landscape
- models-portrait
- models-landscape
- photographers-portrait
- photographers-landscape
- tantra-tutorial

**Note:** The Artists, Jav, Models, TantraTutorial, and Photographers image archives include images of artistic nudity. If you wish to avoid the display of artistic nudes, only install the ImagesPortrait or ImagesLandscape package.
