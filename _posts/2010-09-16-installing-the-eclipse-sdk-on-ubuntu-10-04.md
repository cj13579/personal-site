---
id: 54
title: Android Development with Eclipse SDK on Ubuntu 10.04
date: 2010-09-16T22:05:30+00:00
author: Chris
layout: post
guid: http://104.196.105.206/site/?p=54
permalink: /2010/09/16/installing-the-eclipse-sdk-on-ubuntu-10-04/
tags:
  - Android
  - Eclipse
  - How-To
  - Software
  - Ubuntu
comments: true
---
Up until quite recently (I think) installing the Eclipse SDK has been something of a burden for people. When I first tried to have a stab at writing some “Apps” for my recently purchased HTC Desire I almost stumbled at the first hurdle. I had real trouble installing what was supposed to be the “simplest and fastest” way into Android development.

I had problems from the word go. I downloaded Eclipse and then couldn&#8217;t get it to work because my Java wasn&#8217;t configured correctly. When I configured my Java it turned out to be the wrong version of Eclipse that I had downloaded. Then I couldn&#8217;t for the life of me manage to install the Android Development Tools (ADT) plug-in. All in all, it was a shambles! I finally got it working in the end but I was so angry that I hardly touched it and a few weeks later I deleted everything.

<!--more-->I am delighted to say though that it has become a far, far simpler affair and has therefore given me renewed interest in having another crack at some “App” building. I thought that I would share with you how I got Eclipse installed and working.

Firstly we need to make sure that our system and our repository lists are fully up-to-date. To do this open a Terminal “Applications > Accessories > Terminal” and enter the following:

    sudo apt-get update && sudo apt-get -y upgrade

Once we have done that we need to install the Eclipse SDK. In Ubuntu 10.04 this is available in the repositories and the following command downloads all the necessary Java dependencies -wonderful! To download and install these:

    sudo apt-get install eclipse

Once you have successfully downloaded and installed Eclipse we need to download and install the Android Development Tools (ADT) plug-in. To do this what we need to do fire up Eclipse. If all has gone well you will find it in “Applications > Programming > Eclipse”.

When the software opens we need to navigate to “Help > Install new Software&#8230;” From the window that opens copy the following into the “Work With:” field, then click add. When prompted you should give the plug-in a suitable name, for example: “Android ADT”.

    https://dl-ssl.google.com/android/eclipse/

You should see an item appear in the boxes below called “Developer Tools” &#8211; you should tick the box next to it to include both the sub folders. If you don&#8217;t see anything in the window below you could try removing the “s” from the “https://” at the start of the URL.

Once you have done this click next and make your way through the installation procedure. Once this has finished you will need to restart Eclipse. When Eclipse has restarted you are ready to start developing applications for Android. Wasn&#8217;t that simple?

Hopefully nobody will have to go through what I went through again!

Chris