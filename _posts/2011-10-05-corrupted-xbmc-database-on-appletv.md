---
id: 146
title: Corrupted XBMC Database on AppleTV
date: 2011-10-05T10:25:40+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=146
permalink: /2011/10/05/corrupted-xbmc-database-on-appletv/
tags:
  - apple-tv
  - How-To
  - xbmc
---
## Error: XBMC exited with Status: 6

Well, what a pain this is! Fortunately there is an easy fix but it does mean that you will have to set-up your XBMC system again and if you have made a load of changes or have got lots of media Sources configured then this could take you a while.<!--more-->

To resolve the problem all you need to do is, via a shell, login to your AppleTV using the credentials: frontrow/frontrow. Once you are in you need to navigate to &#8220;/Users/Libraries/Application Support/&#8221;.

Within this directory you will find a folder called XBMC. All you need to do is delete or rename this folder and then start XBMC again.

Commands:

<pre>ssh <a href="mailto:frontrow@AppleTV.local">frontrow@AppleTV.local</a>
cd /Users/Libraries/Appplication Support/
rm -r XBMC
exit</pre>