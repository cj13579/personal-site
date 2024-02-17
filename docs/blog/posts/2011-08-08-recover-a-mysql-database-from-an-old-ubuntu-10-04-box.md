---
id: 137
comments: true
title: Recover a MySQL database from an old Ubuntu 10.04 box
date: 2011-08-08 19:54:28 
authors:
  - cj13579
tags:
  - howto
  - mysql
  - Ubuntu
---
One of my boxes died the other day (the one which hosts this actually) and I needed to recover the mysql database from it and move it from the old one to the new one. I didn't know whether or not it was possible and if it was, how easy it would be to do. As it turns out, it is pretty easy and I'll share with you know how I did it.<!-- more -->

Firstly you'll need to the take the HDD from your old box and somehow connect it to your new one. I have bought an HHD enclosure for mine and have converted it into an external drive.

Boot up and from a shell you will need to stop the mysql-server process

<pre>sudo service mysql stop</pre>

Once you have done this you will need to find the mysql database from the mount that you made and copy it to /var/lib/mysql folder. E.g:

<pre>sudo cp -pr /mount/var/lib/mysql/{db-name} /var/lib/mysql</pre>

After this you will need to change the permissions on the folder and files so the your new instance of MySQL can read the files:

<pre>sudo chown -R mysql:mysql /var/lib/mysql/{db-name}</pre>

Nearly done, all you need to do now is start up the mysql process again:

<pre>sudo service mysql start</pre>

All done! Simples!