---
id: 507
comments: true
title: Changing IP Octets with Bash
date: 2014-08-12 15:30:48
authors:
  - cj13579
tags:
  - bash
  - code
  - Linux
  - SAS
  - scripting
  - Unix
---
I have program at work which needs to create a UDP multicast address from a server's IP address. This process basically just entails replacing the first IP octet with &#8220;239&#8221;. In order to be able to do this I wrote the following. There is probably a much neater and more efficient way of doing this and I would love to hear it:

<pre>MCAST_IP=$(echo ${SERVER_IP} | cut -d. -f2-4)
MCAST_IP=$(echo "239."${META_MCAST_IP})</pre>