---
id: 387
comments: true
title: Find libraries of a particular type and reassign them to improve job performance
date: 2012-07-20T16:12:50+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=387
permalink: /2012/07/20/find-libraries-of-a-particular-type-and-reassign-them-with-sas/
tags:
  - code
  - SAS
  - Teradata
  - work
---
I recently came across a situation at work where I was getting some performance issues with a program because of the way it had been written to find some libraries that it needed. What was happening was that if you have a number of Teradata libraries assigned in your SAS session and you use sashelp.vslib to query what libraries you have assigned you will see that SAS goes off an queries the Teradata dbc.tables table for information about the tables SAS knows about. If there are lots and/or if these tables are large, then you could see a significant drop in the performance of your job while this exercise takes place.<!--more-->

To get around this problem, we need to use a slightly different method of checking which libraries we have assigned in the session: dictionary.libnames. We use this in conjunction with proc SQL:

<pre>%let lib1 = work ;
proc sql ;
   create table &lib1..teralibs as
   select libname
   from dictionary.libnames
   where engine="TERADATA" ;
quit ;
proc sql;
   select count(*)
   into :NObs
   from &lib1..teralibs;
   select libname
   into :libname1-:libname%left(&NObs)
   from &lib1..teralibs;
   %put &libname1;
quit;
%macro AssignLib ;
   %do i=1 %to &NObs;
   libname &&libname&i '';
   %end;
%mend;
%AssignLib ;</pre>

A break down of the code:

<div id="_mcePaste" style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; font-size: 13px; line-height: 19px; white-space: normal;">
  Firstly we extract the Teradata librefs from the dictionary table of assigned libraries.
</div>

<pre>proc sql ;
   create table &lib1..teralibs as
   select libname
   from dictionary.libnames
   where engine="TERADATA" ;
quit ;</pre>

<div id="_mcePaste" style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; font-size: 13px; line-height: 19px; white-space: normal;">
  Assign the librefs that have been extracted to a variable for more processing later on.
</div>

<pre>proc sql;
   select count(*)
   into :NObs
   from &lib1..teralibs;
   select libname
   into :libname1-:libname%left(&NObs)
   from &lib1..teralibs;
   %put &libname1;
quit;</pre>

<div id="_mcePaste" style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; font-size: 13px; line-height: 19px; white-space: normal;">
  For each libref that we have extracted run a libname statement temporarily assigning the libref to a filesystem location. The reason that the libraries are reassigned as opposed to cleared or unassigned is because when a &#8220;libname x clear ;&#8221; statement is  run an out-of-scope ERROR message was received.
</div>

<pre>%macro AssignLib ;
   %do i=1 %to &NObs;
   libname &&libname&i '';
   %end;
   %mend;
%AssignLib ;
%let lib1 = work ;</pre>