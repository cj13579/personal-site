---
id: 162
title: Time to tee off
date: 2011-10-26T11:47:52+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=162
permalink: /2011/10/26/time-to-tee-off/
tags:
  - howto
  - Linux
---
This is as much for my benefit as anyone elses but someone else may find it useful as well. It has come in hand for me many times at work and at play. The reason for using it is if you are running a command or a script that dumps a load of stuff to the terminal. You may wish to keep this output for debugging purposed later or you may be using PuTTy and there is so much output that it gets pushed out the measly buffer. Well no longer, the &#8220;tee&#8221; command is a really good way of piping everything to a file.<!--more-->

<div id="_mcePaste">
  Usage:
</div>

<pre>$ ./myscript.sh 2&gt;&1 | tee -a mylog.txt</pre>

You can move the 2>&1 and change the order of it to just get StdOut, StdErr etc. You can also change the tee options to get more of less to the file. I will post updates to this once I play with it some more.