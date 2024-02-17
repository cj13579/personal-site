---
id: 511
comments: true
title: Showing Bash script execution time in seconds
date: 2014-08-07 10:58:36
authors:
  - cj13579
wptr_hide_title:
  - "0"
tags:
  - bash
  - code
  - Linux
  - scripting
---
Sometimes you want to know how long your bash script takes to run in seconds and you want to show that at the end of the script. The following is what I currently use to display this. There may well be a much nicer and shorter way of doing this and I'd love to hear it but this works perfectly!<!-- more -->

<pre>#!/bin/bash
START=$(date +%s.%N | sed 's/\.[0-9]*$//')

# do some stuff
sleep 2
sleep 1.5
sleep 0.5

END=$(date +%s.%N | sed 's/\.[0-9]*$//')
DIFF=$((END - START))

echo "Runtime was ${DIFF} seconds."</pre>