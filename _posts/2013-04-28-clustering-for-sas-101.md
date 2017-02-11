---
id: 475
comments: true
title: Clustering for SAS 101
date: 2013-04-28T12:10:44+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=475
permalink: /2013/04/28/clustering-for-sas-101/
tags:
  - SAS
  - work
---
At work the other day I used the following descriptions for describing the 4 types of clustering that we use in a SAS environment. I think that they are really useful short descriptions of each type so noting here for future use.

### Load Balancing

This is what we do for our the middle tier. A cluster of your Java Application Server of choice is sat behind a load balancing HTTP server distributing requests for the application or service across multiple cluster nodes to balance the request load. There are a number of different methods for load balancing in this scenario but we generally use round robin or dynamic round robin (weighted round robin with server monitoring). If a node in a load-balancing cluster becomes unavailable the cluster detects the failure and redirects requests to other cluster nodes. Node failures in a load-balancing cluster are not visible from clients outside the cluster.

### High Performance

AKA- Grid Computing. High-performance clusters use cluster nodes to perform concurrent operations. A high-performance cluster allows applications to work in parallel enhancing the performance of the applications.

### Storage

Often at SAS when talking about Grid we talk about shared configuration and shared binaries. A storage cluster allows us to do this. Storage clusters provide a consistent file system image across the servers in a cluster allowing the servers to simultaneously read and write to a single shared file system. A storage cluster simplifies storage administration by limiting the installation and patching of applications to one file system.

### High Availability

High-availability clusters provide continuous availability of applications or services by eliminating single points of failure and by failing over services from one cluster node to another in case a node becomes inoperative. Node failures in a high-availability cluster are not visible from clients outside the cluster.