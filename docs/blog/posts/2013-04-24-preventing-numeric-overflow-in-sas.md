---
id: 432
comments: true
title: Preventing numeric overflow in SAS
date: 2013-04-24 22:52:33
authors:
  - cj13579
tags:
  - code
  - SAS
  - work
---
An interesting problem at work a while ago came about when a colleague was trying to perform a calculation on two numbers but instead of getting back the result the program was returning a NULL value. It turns out that the reason for this is that the number was so big that his machine was not able to handle it. Not ideal. So how can we pre-empt this and ensure that the calculation that we want to do is achievable within our environment?

<!-- more -->


  
Let's start with the exact same problem which the colleague had. The code that they were using for the calculation was:

<pre>data check_power;
   x=8969;
   y=240;
   x_power_y=x**y;
run;</pre>

Well what does this mean then? Is this a software bug as can often be the case with numeric overflow (according to Wikipedia)? Not in this case, here this is an architectural limitation. A 64-bit IEEE floating-point number can only hold values as big as about 1.798 times 10\*\*308. In our problem, the result of 8969\*\*240 is much bigger than that, so we need a floating-point representation that has range more than precision. 8989 is about 2*\*13, and 13\*240 is 3120.

Taken from Wikipedia we can see the exponent limits for IEEE floating point numbers:

| Name | Common name | Base | Digits | E min | E max |
| ---- | ----------- | ---- | ------ | ----- | ----- |
| binary16 | Half precision | 2 | 10+1 | -14 | +15 |
| binary32 | Single precision | 2 | 23+1 | -126 | +127 |
| binary64 | Double precision | 2 | 52+1 | -1022 | + 1023 |
| binary128 | Quadruple precision | 2 | 112+1 | -16382 | +16383 |

So here we are over the exponent limit for 64-bit floating point (1023), but under the exponent limit for 128-bit IEEE floating point (16,383).

So is there any way to prevent this? Something thing that we can do is check what the maximum value that we can store in our system is. This could either be used in a program as some sort of checker before you do your calculation. Or it could be used outside of the job to check for potential overflow situations without having to remember the range for your system.

<pre>data check;
  logbig = constant('logbig');
run;</pre>

The above code makes use of the `CONSTANT('logbig')` function which returns the largest possible number that can be represented on the system. You could take this check further and a loop which increases the value of Y until you hit logbig thus allowing you to calculate the largest possible number you are able to work out for you calculation before you hit 'logbig':

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