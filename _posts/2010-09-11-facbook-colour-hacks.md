---
id: 19
title: Facbook colour hacks
date: 2010-09-11T18:35:11+00:00
author: Chris
layout: post
guid: http://104.196.105.206/site/?p=19
permalink: /2010/09/11/facbook-colour-hacks/
tags:
  - Facebook
  - Fun
  - Hacks
comments: true 
---
So, what a better way to start this newly revamped site but with some good for nothing hacks that may keep you occupied for a little while. Having taken the idea from <a title="The post where I found the hacks" href="http://www.puremango.co.uk/2009/05/hacking-facebook/" target="_blank">here</a> I decided to play with the colour ones. I have updated them and added some of my own.

Since the original post was published, Facebook have changed their layout significantly. Although the colour hack in the original post still works, due to these layout changes it doesn&#8217;t work nearly as effectively. In addition to this, I have discovered some more, meaning if you want to, you can turn the whole page another colour!!

<!--more-->So, what do you need to do? This is really simple, all you need to do is copy and paste the following code snippets into your browser&#8217;s address bar (e.g. where it says http://www.facebo&#8230;..) over the top of where the Facebook URL is.

To make the area around the search bar a different colour simply use:

<pre lang="java">javascript:void(document.getElementById('headNavOut').style.backgroundColor="red");</pre>

To make the blue bar that spans the screen turn another colour use:

<pre lang="java">javascript:void(document.getElementById('blueBar').style.backgroundColor="red");</pre>

To make the shortcuts to Friend Request, Messages and Notifications turn red use:

<pre lang="java">javascript:void(document.getElementById('jewelCase').style.backgroundColor="red");</pre>

To make (on IE) most of the page go red. But on firefox just make the area on the left where your online friends and shortcut to profile are displayed use:

<pre lang="java">javascript:void(document.getElementById('globalContainer').style.backgroundColor="red");</pre>

There is absolutely no point in doing this other than you can. Enjoy.