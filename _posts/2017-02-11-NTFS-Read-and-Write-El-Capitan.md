---
title: Read & Write to NTFS on Mac OS 10.11
date: 2017-02-11
author: Chris
layout: post
tags:
  - Apple
  - mac
  - OSX
  - NTFS
comments: true
---
I have [previously written](http://cjblake.net/2015/01/25/native-ntfs-writes-on-mac-os-x/) about enabling write access to NTFS devices on Mac OS but the methods used within that post have been made redundant due to some changes in the latest version of Mac OS.

This post looks to update those instructions for the latest version of Mac OS so that you (and mostly I) can use NTFS formatted drives on your Mac OS device. The main reason for this post is that I haven't found a single place which has complete instructions for setting this up. For anyone reading these instructions who isn't familiar with the command line these notes will look a little technical, but they aren't too difficult and I'll explain what each one does.

In order for this to work we need to download a couple of pieces of free software. The first one is called osxfuse and you can download it [here](https://github.com/osxfuse/osxfuse/releases/download/osxfuse-3.5.5/osxfuse-3.5.5.dmg). This will add some stuff we need for using NTFS. You can read more about it [here](https://osxfuse.github.io/).

Secondly, we are going to install [Homebrew](http://brew.sh) which is a package manager. Homebrew allows you to install the things you need that Apple don't install for you. To install it, open Terminal.app which you can find in your Utilities folder within Applications. Copy and paste the below into it:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Next, using our newly installed package manager we can install a new version of the program that handles the control of our NTFS devices:

```bash
brew install homebrew/fuse/ntfs-3g
```

**You'll get a message saying that bew has been unable to link the newly installed backed. Don't worry about that message, we are going to take care of that a little later on.**

Now, the next part of this post comes with a security disclaimer:

> NTFS-3G's mount tool will be executed with root permissions. Due to the way Homebrew installs software packages, NTFS-3G's mount tool is not protected from being tampered with by unprivileged attackers, essentially giving those attackers root access to your Mac. You have been warned.

When Mac OS tries to mount a drive it looks for a mount tool in a particular place. That particular folder contains the Apple default mount tool which we know mounts NTFS drives in read-only mode. What we want to do then, is make Mac OS use our newly installed mount tool which will mount our device in read-write mode. However, on OS X El Capitan files in the `/sbin` directory (where Mac OS looks for the mount tool) are protected from being tampered with by a new security feature called System Integrity Protection [(SIP)](https://support.apple.com/en-us/HT204899).

To replace `/sbin/mount_ntfs` with the version provided by NTFS-3G you will need to reboot your Mac in recovery mode. 

1. Reboot the Mac and hold down Command + R keys simultaneously after you hear the startup chime, this will boot OS X into Recovery Mode
1. When the “OS X Utilities” screen appears, pull down the ‘Utilities’ menu at the top of the screen instead, and choose “Terminal” and enter the following command pressing Enter at the end. This will turn off SIP protection and restart your computer in _normal_ mode.

```bash
csrutil disable; reboot
```

Once your machine has rebooted we can then open up Terminal again, and run the following commands to make Mac OS use the new mount tool we installed. The below commands will rename the Apple default mount tool (so that we keep it but Mac OS can't find it) and create what's called a symbolic link to the new version we installed. This is like a copy but we aren't moving the original file to the new folder, just telling the operating system to look in a new location for the file it wants. 

**Note: You'll be prompted to enter your normal logon password to run these commands.**

```bash
sudo mv /sbin/mount_ntfs /sbin/mount_ntfs.orig
sudo ln /usr/local/Cellar/ntfs-3g/2016.2.22/sbin/mount_ntfs /sbin/mount_ntfs
```

Once we've done that we are going to turn the SIP protection back on so that nothing else can edit files in that location. Using the instructions above, boot your machine into recovery mode and then run the following command from the Terminal:

```bash
csrutil enable; reboot
```

Once your machine has booted back up, plug in a drive and try creating a folder. You should see that you can now write to your drive. Hazaar!