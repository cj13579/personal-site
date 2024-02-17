---
id: 196
comments: true
title: Terminal / Cron Environment differences
date: 2011-11-26 00:33:49 
authors:
  - cj13579
---
I have been going through some logs for my Flexget instance and saw that I was getting a number of these messages coming up:

<pre>Your cron environment has different filesystem encoding (ANSI_X3.4-1968) 
compared to your terminal environment (UTF-8).</pre>

Oh dear, well sure enough, it is different but there is a really easy way to sort it:<!-- more -->

Firstly, let's take a look at how it is different:

Terminal:

<pre>chris@q2server:~$ locale
LANG=en_GB.UTF-8
LC_CTYPE="en_GB.UTF-8"
LC_NUMERIC="en_GB.UTF-8"
LC_TIME="en_GB.UTF-8"
LC_COLLATE="en_GB.UTF-8"
LC_MONETARY="en_GB.UTF-8"
LC_MESSAGES="en_GB.UTF-8"
LC_PAPER="en_GB.UTF-8"
LC_NAME="en_GB.UTF-8"
LC_ADDRESS="en_GB.UTF-8"
LC_TELEPHONE="en_GB.UTF-8"
LC_MEASUREMENT="en_GB.UTF-8"
LC_IDENTIFICATION="en_GB.UTF-8"
LC_ALL=</pre>

Cron:

<pre>LANG="POSIX"
LC_CTYPE="POSIX"
LC_NUMERIC="POSIX"
LC_TIME="POSIX"
LC_COLLATE="POSIX"
LC_MONETARY="POSIX"
"LC_MESSAGES="POSIX"
LC_PAPER="POSIX"
LC_NAME="POSIX"
LC_ADDRESS="POSIX"
LC_TELEPHONE="POSIX"
LC_MEASUREMENT="POSIX"
LC_IDENTIFICATION="POSIX"
LC_ALL=</pre>

Thank fully there is an odd, but easy solution. Even though apparently the /etc/environment file is now redundant this is where the solution goes. Simply add the following line to the file:

<pre>LANG=en_GB.UTF-8</pre>

Once you have done that then all you need to do is restart your cron process:

<pre>sudo service cron restart</pre>

Then you get messages that look like this:

<pre>2011-11-26 00:00 INFO     log_once
Good! Your crontab environment seems to be same as terminal.</pre>

Much better!