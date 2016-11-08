---
id: 124
title: Something neat
date: 2011-08-07T18:56:41+00:00
author: Chris
layout: post
guid: http://104.196.105.206/site/?p=124
permalink: /2011/08/07/something-neat/
tags:
  - howto
  - puddletag
  - Ubuntu
---
I haven&#8217;t posted anything for a long, long time so I thought that I would just post something very quickly. A link to something very cool: <a href="http://puddletag.sourceforge.net/" target="_blank">puddletag</a>. puddletag is an audio tag editor (primarily created) for GNU/Linux similar to the Windows program, [Mp3tag](http://www.mp3tag.de/). Unlike most taggers for GNU/Linux, it uses a spreadsheet-like layout so that all the tags you want to edit by hand are visible and easily editable.

<!--more-->The usual tag editor features are supported like extracting tag information from filenames, renaming files based on their tags by using patterns and basic tag editing.

Then there’re Functions, which can do things like replace text, trim it, do case conversions, etc. Actions can automate repetitive tasks. You can import your QuodLibet library, lookup tags using Amazon (including cover art), Discogs (does cover art too!), FreeDB and MusicBrainz. There’s quite a bit more, but I’ve reached my comma quota.

## Installing puddletag

The following instructions are for installing on Ubuntu using the .deb from here: [puddletag\_0.10.5-1\_all.deb](http://sourceforge.net/projects/puddletag/files/puddletag_0.10.6-1_all.deb). Double clicking on it and letting your package manager do the work should be cool but if you would want to it manually (as root):

<div>
  <pre lang="bash">apt-get install python-qt4 python-pyparsing python-mutagen python-configobj python-musicbrainz2</pre>
</div>

<div>
  Then (presuming you downloaded to /tmp) run the following:
</div>

<div>
  <div>
    <pre lang="bash">dpkg -i /tmp/puddletag_0.10.5-1_all.deb</pre>
  </div>
  
  <div>
    Boom. An amazing tag editor for keeping your mp3 library manager looking pretty!
  </div>
</div>