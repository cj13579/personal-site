---
id: 87
comments: true
title: Explode and Implode strings with PHP
date: 2010-09-29 18:00:23
authors:
  - cj13579
tags:
  - code
  - Fun
  - How-To
  - PHP
  - web
  - work
---
So I came across a problem at work the other day: Take a string (in this case Job number) with a &#8220;/&#8221; in it and manipulate it. The strings looked something like 126/6. I needed to be able to perform a couple of condition based actions on the string. Doing this meant that I had to take the string apart, perform what I needed to do, then sew it all back together again. In order to do this I knew that I would need to explode the string using PHP's built in explode() function but didn't know how I would then be able to stitch the string back together once I had done the necessary manipulations.

<!-- more -->It didn't take a lot of browsing the web to find the opposite implode() function, but one thing that annoyed me was that there wasn't one site I could find an article or blog which covered both explode() and implode() in the same place. Needless to say, I intend to right this wrong here, now.

The example that I will be using for this is the job number problem that I had. The job numbers (e.g 126/6), unsurprisingly, increment. They increment like: 126/6, 126/7, 126/8, 126/9 up until the part of the &#8220;/&#8221; gets to 9 where the number after the &#8220;/&#8221; is set back to 1 and the number before the &#8220;/&#8221; is incremented by 1. e.g. 127/1. Simple, right?

So, in order to do this this is what I wrote:

<pre lang="PHP">$split = explode("/", $job);
$j1 = $split[0];
$j2 = $split[1];
if($j2&lt;9)  {
    $j2=$j2+1;
    $job = array($j1,$j2);
    $new = implode("/",$job);     }
    elseif($j2==9)    {
        $j2=1;
        $j1=$j1+1;
        $job = array($j1,$j2);
        $new = implode("/",$job);     }
else        {
    echo "An error has occured";     }</pre>

So, a little explanation of what is going on above. Firstly, we explode the job number into an array:

<pre lang="PHP">$split = explode("/", $job);</pre>

In the brackets of the explode function we first specify our string delimiter, followed by a comma, and then the string we want to explode. Next we the separate the elements of the array into their own variables so that we can perform the necessary manipulations:

<pre lang="PHP">$j1 = $split[0];
$j2 = $split[1];</pre>

Once we have done this we are at the stage where we can perform our necessary actions. Firstly, we check the second number to make sure it is less than 9. If it is, all we do is increment the number by 1:

<pre lang="PHP">if($j2&lt;9)  {
    $j2=$j2+1;</pre>

Once we have done all our manipulations (in this instance just the one) we essentially just trace back our steps. We start by putting the separated parts back into an array:

<pre lang="PHP">$job = array($j1,$j2);</pre>

Once we have done this, we just sew back together the separate parts of the job number. The implode function takes its arguments in exactly the same way as the explode function with the string delimiter first, followed by a comma, followed by the array (string) to be imploded:

<pre lang="PHP">$new = implode("/",$job);     }</pre>

If the second part of the string does equal 9 then the process is very similar. The only difference is that we reset the second part of the string to be 1 and increment the first part of the string:

<pre lang="PHP">$j2=1;
$j1=$j1+1;</pre>

I hope that this at least saves someone some valuable time searching the web. If you have any comments or suggestions I would love to hear them.

Best

Chris