---
id: 507
title: Changing IP Octets with Bash
date: 2014-08-12T15:30:48+00:00
author: Chris
layout: post
guid: http://104.196.105.206/?p=507
permalink: /2014/08/12/changing-ip-octets-with-bash/
wptr_hide_title:
  - "0"
tags:
  - bash
  - code
  - Linux
  - SAS
  - scripting
  - Unix
---
I have program at work which needs to create a UDP multicast address from a server&#8217;s IP address. This process basically just entails replacing the first IP octet with &#8220;239&#8221;. In order to be able to do this I wrote the following. There is probably a much neater and more efficient way of doing this and I would love to hear it:

<pre>MCAST_IP=$(echo ${SERVER_IP} | cut -d. -f2-4)
MCAST_IP=$(echo "239."${META_MCAST_IP})</pre>