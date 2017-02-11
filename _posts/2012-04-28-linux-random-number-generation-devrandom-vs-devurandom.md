---
id: 361
comments: true
title: 'Linux random number generation: /dev/random vs /dev/urandom'
date: 2012-04-28T16:39:01+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=361
permalink: /2012/04/28/linux-random-number-generation-devrandom-vs-devurandom/
tags:
  - Linux
  - SAS
  - Unix
  - work
---
I had a problem at work a while ago which appeared again last week where some stuff was taking ages to run through. I found a useful note which explained that the reason for this slowness is because of the encryption type that I was using and the fact that this was using /dev/random for its random number generation and it suggested instead to use /dev/./urandom. This helped resolve the problem but I had no clue why. In this post I&#8217;ll explain why /dev/urandom is faster than /dev/random, but not as secure.

<!--more-->Firstly, open up a terminal and submit the command:

<pre> $ cat /proc/sys/kernel/random/entropy_avail</pre>

This is the [entropy](http://en.wikipedia.org/wiki/Entropy_(information_theory)) that is available for the kernel at any time.  The concept behind an entropy pool is that it is a count of random bits that are assumed to be unknown to a potential attacker. New randomness is added whenever available; for example, when the user hits a key or moves a mouse.

Now, fire off the following command:

<pre> $ hexdump /dev/random</pre>

You will probably get like 1 or 2 random numbers out of the system depending on your starting entropy and how many other things you have going on in the box. The /dev/random device works by requesting random bits from the entropy pool, once it has taken its required amount the remainder is subtracted from the estimated number of random bits remaining in the pool. If not enough unknown bits are available the process will be blocked until enough are available.

Now fire off:

<pre> $ hexdump /dev/./urandom</pre>

The /dev/urandom device is a simple modification to /dev/random in that it doesn&#8217;t perform the second check against the entropy pool which disregards estimates of input randomness. This small but significant difference results in the number produced by /dev/urandom is likely not to have as high an entropy count as a number produced by /dev/random.