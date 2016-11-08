---
id: 511
title: Showing Bash script execution time in seconds
date: 2014-08-07T10:58:36+00:00
author: Chris
layout: post
guid: http://104.196.105.206/?p=511
permalink: /2014/08/07/showing-bash-script-execution-in-seconds/
wptr_hide_title:
  - "0"
tags:
  - bash
  - code
  - Linux
  - scripting
---
Sometimes you want to know how long your bash script takes to run in seconds and you want to show that at the end of the script. The following is what I currently use to display this. There may well be a much nicer and shorter way of doing this and I&#8217;d love to hear it but this works perfectly!

<pre>#!/bin/bash
START=$(date +%s.%N | sed 's/\.[0-9]*$//')

# do some stuff
sleep 2
sleep 1.5
sleep 0.5

END=$(date +%s.%N | sed 's/\.[0-9]*$//')
DIFF=$((END - START))

echo "Runtime was ${DIFF} seconds."</pre>