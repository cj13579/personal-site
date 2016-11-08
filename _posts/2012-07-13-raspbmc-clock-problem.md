---
id: 384
title: Raspbmc clock problem
date: 2012-07-13T17:51:27+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=384
permalink: /2012/07/13/raspbmc-clock-problem/
tags:
  - raspbmc
---
OS cannot seem to access the hwclock:

<pre>pi@raspbmc:/etc/init.d$ sudo /sbin/hwclock -r --debug
hwclock from util-linux-ng 2.17.2
hwclock: Open of /dev/rtc failed, errno=2: No such file or directory.
No usable clock interface found.
Cannot access the Hardware Clock via any known method.</pre>

<pre><div id="_mcePaste">
  pi@raspbmc:/etc/init.d$ ls -l /dev | grep rtc
  pi@raspbmc:/etc/init.d$
</div></pre>

This is what it looks like from my Ubuntu box:

<pre>chris@q2server:/media/external-ma/Music$ sudo /sbin/hwclock -r --debug
[sudo] password for chris:
hwclock from util-linux-ng 2.17.2
Using /dev interface to clock.
Assuming hardware clock is kept in local time.
Waiting for clock tick...
...got clock tick
Time read from Hardware Clock: 2012/07/13 16:38:50
Hw clock time : 2012/07/13 16:38:50 = 1342193930 seconds since 1969
Fri 13 Jul 2012 16:38:50 BST  -0.236127 seconds</pre>

<pre>chris@q2server:/media/external-ma/Music$ ls -l /dev | grep rtc
lrwxrwxrwx 1 root root           4 2012-02-25 15:38 rtc -&gt; rtc0
crw-rw---- 1 root root    254,   0 2012-02-25 15:38 rtc0
chris@q2server:/media/external-ma/Music$</pre>

I am going to write a small script to check a ntp server (probably a few) for current date/time.