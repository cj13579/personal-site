---
id: 401
title: Extract all machines associated with a SAS environment
date: 2012-11-09T13:49:46+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=401
permalink: /2012/11/09/extract-all-machines-associated-with-a-sas-environment/
tags:
  - code
  - SAS
---
Something that, certainly for large SAS deployments, may be across multiple tiers is having the ability to work out what machines you have in the environment and have been registered in the Metadata Server. This could be useful in a number of circumstances such as for a health check application which uses remote sign-on. It might cycle through all of your hosts to check if a session can be started.
  
<!--more-->


  
The following code can be used to extract all of the hostnames that are registered within an instance of a SAS Metadata server. You can customise (and limit expand the scope of the search) by changing the Name query (contained within the single quotes). If you have a naming convention for box types this could be used to exclude certain servers such as Metadata servers or Middle tier boxes which would not, in a normal set-up, be able start SAS sessions:

<pre>options metaserver='a123.us.company.com'
metaport=8561
metauser='myid'
metapass='mypassword'
metarepository='myrepos';

data machines;
   length comp_uri uri text $256;
   n=1;
   comp_uri='';
   rc=metadata_getnobj('omsobj:Machine?@Name contains '.'',n,comp_uri);
   put rc;
   do n = 1 to rc ;
      nasc_rc=metadata_getnasn(comp_uri,'AssociatedMachine',0,uri);
      put nasc_rc;
      arc=metadata_getattr(uri,'Name',text);
      hostname=text;
      output;
      n=n+1;
   end;
run;</pre>