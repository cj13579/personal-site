---
id: 109
title: Daemonised Transmission! on Ubuntu Server 10.04
date: 2010-10-13T21:14:23+00:00
author: Chris
layout: post
guid: http://104.196.105.206/site/?p=109
permalink: /2010/10/13/daemonised-transmission-on-ubuntu-server-10-04/
tags:
  - Server
  - Torrent
  - Transmission
  - Ubuntu
---
So, this evening I have been trying to configure my new Ubuntu server with a daemon-ised install of transmission for my torrent downloads. I read a number of blogs and articles from various places but struggled quite a bit with it. I could get it to install and to start no worries, but seeing as this server is headless I needed access to the web interface (hence the daemonised version) and I couldn&#8217;t get this working! I kept changing the settings.json file but every time I closed it and fired up transmission it appeared to be overwriting my file and using the default! Anyway, I am there now, but I found that I had to piece bits of blogs, forums and tutorials together in order to get it working.

The solution that I have is no way near perfect. The permission settings that seem to have to be set in order to get it to work are strange and not particularly safe. Needless to say, it works and if it works for someone else and nothing breaks then I shall consider it a success. So what did I do?

<!--more-->Well firstly, updated my repository listings and installed the daemon version of Transmission:

<pre lang="bash">sudo apt-get update && sudo apt-get install transmission-daemon</pre>

Secondly, I checked to make sure that the installer had put a copy of the &#8220;settings.json&#8221; in my ~/.config folder:

<pre lang="bash">ls ~/.config/transmission-daemon</pre>

Mine did, but if yours for some reason doesn&#8217;t you need make sure there is a copy there. You can either create a new file of copy one from the /etc:

<pre lang="bash">sudo cp /etc/transmission-daemon/settings.json ~/.config/transmission-daemon/settings.json</pre>

To make things easier from now on it&#8217;s best to cd into ~/.config/transmission-daemon.

This is where it gets a bit messy.. We need to change the owner and group of the file to be &#8220;debian-transmission&#8221;:

<pre lang="bash">sudo chown debian-transmission:debian-transmission settings.json</pre>

Then we need to set the permissions of &#8220;settings.json&#8221;:

<pre lang="bash">sudo chmod a+rwx settings.json</pre>

Then I had to change the permissions on the download folder that I wanted to use to 777 -not ideal, but hey-ho I&#8217;ll roll with it.

Having done all of this I was then able to fire up nano and make all the changes to my settings file. Just to make sure that everything was working I fired up transmission with an -f switch to run it in the foreground for a couple of times so I could see if anything was going wrong and could make any changes that were necessary:

<pre lang="bash">transmission-daemon -f</pre>

As always, questions and comments are welcome and appreciated.

Chris