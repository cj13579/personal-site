---
id: 517
comments: true
title: Rebuilding and redeploying the SAS Web Applications Silently
date: 2014-08-11 08:16:38
authors:
  - cj13579
wptr_hide_title:
  - "0"
tags:
  - analytics
  - code
  - howto
  - Linux
  - SAS
  - scripting
  - work
---
If you run a large SAS estate like the organisation that I work for, or you want to develop an automated way of installing hot-fixes or promoting customised content then you will probably want to script the rebuilding and redeploying of the SAS Web Applications.<!-- more -->

Interactively, this is done by using the SAS Deployment Manager (SDM). The SDM takes many of the same command line arguments that the SDW does and we can therefore use response files to  drive the Wizard and automate this stuff. However, with the SDM in 9.4M1, there seems to be a bug where certain answers don't get read from the response file and therefore we get prompted for the answers to those questions.

In order to circumvent this problem, I came up with the following solution. The _-console_ switch puts the SDM in a text only mode (don't be fooled, you may still need and X connection) which allows us to pass a hereto doc to the SDM to answer the prompts when they appear allowing you to successfully rebuild and redeploy the SAS web applications in a fully scripted and silent way.

NOTE: The command below has been split for formatting reasons. Up until the & should be on one line.

<pre>${SASHOME}/SASDeploymentManager/9.4/sasdm.sh -console -partialprompt 
-responsefile /tmp/wip_redeploy.response &lt;&lt; EOF &gt;/dev/null &
 2
 Y
 Y
 Y
 Y
 EOF</pre>