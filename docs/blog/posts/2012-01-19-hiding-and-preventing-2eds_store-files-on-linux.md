---
id: 232
comments: true
title: Hiding and preventing :2eDS_Store files on Linux
date: 2012-01-19 22:31:23
authors:
  - cj13579
tags:
  - apple
  - How-To
  - Linux
  - mac
---
If you have ever accessed your Linux box from a Mac via the finder then you may have seen that when you have subsequently been browsing your linux box via the command line you see that in every folder you visit you find a :2eDS_Store file. These files are created by the finder and store the users preferences for viewing that folder. There are a couple of ways that you can disable/hide the creation of these files.<!-- more -->

### Share Level

By default the finder will create a :2eDS\_Store file. To change this to the creation of a .2eDS\_Store file, thus hiding it from a normal ls listing, we can use the &#8220;usedots&#8221; option on each Netatalk share on the linux box. Modify your /etc/netatalk/AppleVolumes.default file for each share with the following format:

<pre>~/	"Home Directory" 	options:usedots</pre>

After you have done this you will need to restart the Netatalk server

<pre>sudo service netatalk restart</pre>

### On your Mac

You can disable the creation of the :2eDS_Store file on your mac by running opening a terminal and running the following command:

<pre>defaults write com.apple.desktopservices DSDontWriteNetworkStores true</pre>

You will need to logout or restart your computer for this change to take affect. Additionally, this will only affect the user which is logged in at the time. You will need to run the command as each user for it to take global affect.

This option will affect not only AFP shares but also SMB, CIFS, NFS, and WebDAV servers.