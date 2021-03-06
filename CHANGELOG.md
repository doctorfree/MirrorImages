# Changelog

All notable changes to this project will be documented in this file.

Feb 03, 2022 Version 3.0.1 Release 1
This release update of MirrorImages incorporates changes to improve integration with the MirrorCommand package during downloads. In addition, support is added for models by country in the MirrorImages downloads and in the MirrorCommand default config files. New Google Drive file ids have been used in the download scripts to reflect the MirrorImages distribution changes.

Jan 29, 2022 Version 3.0.0 Release 2
This release of MirrorImages introduces RPM format installation packages.

Jan 16, 2022 Version 3.0.0 Release 1
MirrorImages 3.0.0 release 1 introduced support for both landscape and portrait mode images. Changes to packaging include the implementation of release creation during the Gitlab continuous integration process.

Thu Feb 3 08:34:11 2022 -0800 4469f32 :
   Do not prompt for download in Debian installs as well
Thu Feb 3 08:29:18 2022 -0800 6e5fc80 :
   Add -y argument to Install script
Wed Feb 2 12:56:08 2022 -0800 14a4f43 :
   Add countries packages to Install/Uninstall scripts and release notes
Wed Feb 2 12:37:47 2022 -0800 9a9e86b :
   Add packages for models by country
Sat Jan 29 15:06:30 2022 -0800 af2f040 :
   Update changelog in preparation for v3.0.0r2 release
Sat Jan 29 13:06:55 2022 -0800 74510c4 :
   Set ownership in post install, exclude system dirs
Sat Jan 29 10:03:09 2022 -0800 2bc9e68 :
   Use -i option to get scripts to avoid user interaction, depends on MirrorCommand 3.0.2 or later
Fri Jan 28 16:18:43 2022 -0800 7ab2481 :
   Add support for RPM format package installs
Fri Jan 28 11:31:01 2022 -0800 02f4612 :
   Order release assets Packages
Fri Jan 28 11:18:14 2022 -0800 14db877 :
   Add filename and mode to artifact names
Fri Jan 28 10:56:38 2022 -0800 d470ebc :
   Add G or R rating to artifact names
Fri Jan 28 10:47:44 2022 -0800 4a9bfb0 :
   Use release.md for release description
Thu Jan 20 13:41:29 2022 -0800 3c937de :
   Add landscape images to Uninstall
Sun Jan 16 11:37:13 2022 -0800 6f7e2a5 :
   Automate release creation in Gitlab CI
Sun Jan 16 11:05:05 2022 -0800 ab6539b :
   Fix typos in postinst
Sun Jan 16 07:24:09 2022 -0800 cb5c656 :
   Convenience script to get the IDs from the output of getfolderids
Sat Jan 15 11:24:28 2022 -0800 59240ad :
   Added JAV image packages
Sat Jan 15 08:26:02 2022 -0800 790da96 :
   Add creation of landscape packages
Sat Jan 15 07:44:58 2022 -0800 ca997d0 :
   Reflect package name change in packaging scripts
Sat Jan 15 07:41:47 2022 -0800 62c0a58 :
   Rename repo MirrorImages and base image package ImagesPortrait
Sat Jan 15 07:20:46 2022 -0800 206420d :
   Move portrait format image packages install location to pics-portrait
Tue Dec 28 10:02:37 2021 -0800 c271685 :
   Rename MirrorCommandLine to MirrorCommand
Sat Dec 18 13:59:14 2021 -0800 b6e1a01 :
   Models package was not using release in Debian package file name
Sat Dec 18 13:35:13 2021 -0800 eb8a8a0 :
   Fix TantraTutorial package selection
Sun Dec 5 19:01:23 2021 -0800 44f78ad :
   Add browse-artifacts.txt
Mon Nov 29 13:47:25 2021 -0800 e382c10 :
   Added notes on Tantra Tutorial
Mon Nov 29 09:59:17 2021 -0800 48f13e3 :
   Update changelog in preparation for 2.6 release
Mon Nov 29 08:57:29 2021 -0800 0b5439e :
   Fix version in dist dir
Mon Nov 29 08:49:49 2021 -0800 04ddbac :
   Move pics dir to /usr/local/MirrorCommandLine, add tantra tutorial
Mon Nov 29 08:40:28 2021 -0800 b3a8ca3 :
   Move pics dir to /usr/local/MirrorCommandLine, add tantra tutorial
Sat Nov 27 13:16:38 2021 -0800 023e7f2 :
   Rename install directory to /usr/local/MirrorCommandLine/...
Sat Nov 27 11:43:08 2021 -0800 e85e576 :
   Check for symlink when removing directory
Mon Nov 22 11:35:28 2021 -0800 f0ebe53 :
   Set Architecture to 'all' in control file
Mon Nov 22 11:22:20 2021 -0800 e1b91b2 :
   Set architecture to any, check for dir before removing
Sat Nov 20 14:54:34 2021 -0800 c36d517 :
   Add created subdirs to gitignore
Sat Nov 20 14:22:48 2021 -0800 8dab5ca :
   Add file listing for Neu Ling
Sat Nov 20 14:08:59 2021 -0800 55337b3 :
   Fix comments in maintainer scripts
Sat Nov 20 14:02:26 2021 -0800 157cd52 :
   Fix Uninstall check for installed packages
Sat Nov 20 12:46:10 2021 -0800 47a973f :
   Only run CI pipeline on new tag
Sat Nov 20 12:44:49 2021 -0800 aff2ed3 :
   Enable Gitlab Continuous Integration
Sat Nov 20 12:40:55 2021 -0800 e05ad65 :
   Initialize changelog
Sat Nov 20 12:38:36 2021 -0800 107bc5e :
   Minor formatting
Sat Nov 20 11:54:18 2021 -0800 b03304f :
   Add section on package sizes and content
Sat Nov 20 11:17:40 2021 -0800 d57ee94 :
   No zip or gzip distribution archives for image packages
Sat Nov 20 11:14:13 2021 -0800 db4aba3 :
   Add info on MirrorCommandLine dependency install
Sat Nov 20 11:04:05 2021 -0800 79cb746 :
   Initial MirrorImagesPortrait git repository
