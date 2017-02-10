---
title: Iterable JSON in Python
date: 2016-11-17
author: Chris
layout: post
tags:
  - Python
  - code
---

Python works relly nicely with JSON objects so long as all of your keys are nicely labeled and you dont have object or arrays with no key labels:

```python
json = {
  "key" : "value",
  "anotherkey" : "value"
}

```

You can access the items really easily:

```python
data = json.loads(json);
```

But it seems to work much less well, or at least, much less obviously if you have a JSON array of objects:

```python
json = {
  "key": "value",
  {
    "a1key1" : "value",
    "a1key1" : "value"
  },
  {
    "a2key1" : "value",
    "a2key1" : "value"
  },
  {
    "a3key1" : "value",
    "a3key1" : "value"
  }
}
```

To access objects easily within your program, I have found it easiest if you add an additonal step to convert you JSON into a regular python array:

```python
data = json.loads(json)
data = {int(k):v for k,v in data.items() if k.isdigit()}
```