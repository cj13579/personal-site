---
id: 77
title: How open are you?
date: 2010-09-17 18:30:05
authors:
  - cj13579
tags:
  - Fun
  - open-source
  - Richard M Stallman
  - Software
  - Ubuntu
comments: true
---
So, I was browsing about the net today and stumbled upon this blog <a title="Ed Robinson" href="http://www.earobinson.org/2009/09/12/vrms-16-non-free-packages-0-9-of-1712-installed-packages/" target="_self">post</a>. A neat little trick I thought, I wonder how well I will score? It appears that I am 99.6% open! In my opinion, I think that makes me pretty open!
  
<!-- more -->

<pre lang="apt_sources"><a href="mailto:chris@queens:~$">chris@queens:~$</a> vrms
           Non-free packages installed on queens-server

nvidia-71-modaliases      Modaliases for the NVIDIA binary X.Org driver
tangerine-icon-theme      Tangerine Icon theme
unrar                     Unarchiver for .rar files (non-free version)

Non-free packages with status other than installed on queens-server

fglrx                     ( dei)  Video driver for the ATI graphics accelerators
sun-java6-bin             ( dei)  Sun Java(TM) Runtime Environment (JRE) 6 (arch
sun-java6-fonts           ( dei)  Lucida TrueType fonts (from the Sun JRE)
sun-java6-jre             ( dei)  Sun Java(TM) Runtime Environment (JRE) 6 (arch

            Contrib packages installed on queens-server

gstreamer0.10-pitfdll     GStreamer plugin for using MS Windows binary codecs
nvidia-common             Find obsolete NVIDIA drivers
ttf-mscorefonts-installer Installer for Microsoft TrueType core fonts

  7 non-free packages, 0.4% of 1948 installed packages.
  3 contrib packages, 0.2% of 1948 installed packages.</pre>

The test can be run on any Debian based system. If you are running Ubuntu and want to run this test for yourself all you need to do is:

Update your repository list:

<pre lang="apt_sources">sudo apt-get update</pre>

Install the vrms package:

<pre lang="apt_sources">sudo apt-get install vrms</pre>

Then you are ready to run it:

<pre lang="apt_sources">vrms</pre>

Enjoy,

Chris