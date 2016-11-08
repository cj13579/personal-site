---
id: 536
title: Native NTFS writes on Mac OS X
date: 2015-01-25T15:56:38+00:00
author: Chris
layout: post
guid: http://104.196.105.206/?p=536
permalink: /2015/01/25/native-ntfs-writes-on-mac-os-x/
wptr_hide_title:
  - "0"
tags:
  - apple
  - bash
  - code
  - mac
  - OSX
---
By default, OS X does not support native writing to NFTS formatted file systems. It is possible to configure though. This is especially useful if you are sharing media and files with others using externally USB drives that are NTFS formatted. This is a short little guide on how to configure it.

The first thing that you will need is the UUID of the drive that you want to write to. The easiest way to get this is to open Terminal and run the following command (where &#8220;volume_name&#8221; is the name of the volume as it appears on your desktop*):

* If you have a space in the name such as &#8220;My Passport&#8221; Then you will need backslashes in the &#8220;volume_name&#8221; at the end of the word before the space. E.g &#8220;/Volumes/My\ Passport&#8221;

<pre>sudo diskutil info /Volumes/volume_name</pre>

You&#8217;ll want to copy out the Volume UUID from the information that is printed to the screen. At this point, eject the device from the machine.

Secondly, we are going to edit the way that the drive is mounted on the machine. Here we are going to override the default options set by OS X. We do this by editing the fstab file. This is done on Yosemite by using the vifs program:

<pre>sudo vifs</pre>

press i (to enter insert mode)

* You&#8217;ll need to be an administrator and enter your password.

Using the arrow keys navigate to the bottom of the file and create a new line containing the following

<pre>UUID=123456-123-412241 none ntfs rw,auto,nobrowse</pre>

Press ESC (to exit insert mode)

Press :wq <enter> (to save the file and quit)

Plug the device back into the compute. You&#8217;ll notice that it doesn&#8217;t come up on your desktop. You can check that it has mounted by running the following command:

<pre>df -k</pre>

If you can see something like the following then it has mounted correctly:

<pre>/dev/disk1s1    976728060 855949812 120778248    88%    42950 120778256    0%   /Volumes/My Passport</pre>

To open it with Finder so that you can write to it, run the following command:

<pre>open /Volumes/My\ Passport</pre>

Now you should have a finder window open which will allow you to copy and past, create new folders and create new files. All without having to install any third party products full of spyware!

<p style="color: #f5f5f5;">
  <p style="color: #f5f5f5;">
    /dev/disk1s1    976728060 855949812 120778248    88%    42950 120778256    0%   /Volumes/My Passport
  </p>
  
  <p style="color: #f5f5f5;">
    ]sadVolume UUID:              7E254578-2038-45BD-A481-21DCED48B3B4
  </p>