---
id: 432
comments: true
title: Preventing numeric overflow in SAS
date: 2013-04-24T22:52:33+00:00
author: Chris
layout: post
guid: http://cj13579.dyndns-server.com/site/?p=432
permalink: /2013/04/24/preventing-numeric-overflow-in-sas/
tags:
  - code
  - SAS
  - work
---
An interesting problem at work a while ago came about when a colleague was trying to perform a calculation on two numbers but instead of getting back the result the program was returning a NULL value. It turns out that the reason for this is that the number was so big that his machine was not able to handle it. Not ideal. So how can we pre-empt this and ensure that the calculation that we want to do is achievable within our environment?

<!--more-->


  
Let&#8217;s start with the exact same problem which the colleague had. The code that they were using for the calculation was:

<pre>data check_power;
   x=8969;
   y=240;
   x_power_y=x**y;
run;</pre>

Well what does this mean then? Is this a software bug as can often be the case with numeric overflow (according to Wikipedia)? Not in this case, here this is an architectural limitation. A 64-bit IEEE floating-point number can only hold values as big as about 1.798 times 10\*\*308. In our problem, the result of 8969\*\*240 is much bigger than that, so we need a floating-point representation that has range more than precision. 8989 is about 2*\*13, and 13\*240 is 3120.

Taken from Wikipedia we can see the exponent limits for IEEE floating point numbers:

<div class="table-responsive">
  <table class="table table-striped">
    <tr>
      <th>
        Name
      </th>
      
      <th>
        Common name
      </th>
      
      <th>
        Base
      </th>
      
      <th>
        Digits
      </th>
      
      <th>
        E min
      </th>
      
      <th>
        E max
      </th>
    </tr>
    
    <tr>
      <td>
        binary16
      </td>
      
      <td>
        Half precision
      </td>
      
      <td>
        2
      </td>
      
      <td>
        10+1
      </td>
      
      <td>
        −14
      </td>
      
      <td>
        +15
      </td>
    </tr>
    
    <tr>
      <td>
        binary32
      </td>
      
      <td>
        Single precision
      </td>
      
      <td>
        2
      </td>
      
      <td>
        23+1
      </td>
      
      <td>
        −126
      </td>
      
      <td>
        +127
      </td>
    </tr>
    
    <tr>
      <td>
        binary64
      </td>
      
      <td>
        Double precision
      </td>
      
      <td>
        2
      </td>
      
      <td>
        52+1
      </td>
      
      <td>
        −1022
      </td>
      
      <td>
        +1023
      </td>
    </tr>
    
    <tr>
      <td>
        binary128
      </td>
      
      <td>
        Quadruple precision
      </td>
      
      <td>
        2
      </td>
      
      <td>
        112+1
      </td>
      
      <td>
        −16382
      </td>
      
      <td>
        +16383
      </td>
    </tr>
  </table>
</div>

So here we are over the exponent limit for 64-bit floating point (1023), but under the exponent limit for 128-bit IEEE floating point (16,383).

So is there any way to prevent this? Something thing that we can do is check what the maximum value that we can store in our system is. This could either be used in a program as some sort of checker before you do your calculation. Or it could be used outside of the job to check for potential overflow situations without having to remember the range for your system.

<pre>data check;
  logbig = constant('logbig');
run;</pre>

The above code makes use of the CONSTANT(&#8216;logbig&#8217;) function which returns the largest possible number that can be represented on the system. You could take this check further and a loop which increases the value of Y until you hit logbig thus allowing you to calculate the largest possible number you are able to work out for you calculation before you hit &#8216;logbig&#8217;:

<pre>data check2;
   x=8969;
   logx = log(x);
   logbig = constant('logbig');
   do y= 20 to 240 by 10;
      logx_to_y = logx * y;
      if (logx_to_y &lt; logbig) then do;
         x_power_y = x ** y;
         x_power_y2 = exp(logx_to_y);  /* this returns the same value */
      end;
      output;
   end;
run;</pre>