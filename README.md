# Fuzzytime Pip Module

A published pip module that converts a datetime object, time object, date object, epoch int or date/time string into a fuzzy timestamp such as "just now", "about 5 minutes ago" or "about an hour ago". This module also works for future dates giving an output such as "in five minutes". The latest version of the module utilizes a binary search algorithm to speed up the overall process. Although miniscule, the difference is felt when a large number of consecutive operations are conducted.

## Prerequisites

Python2+ and Pip

## Installing

To install from the command line interface, simply type:
```
pip install fuzzytime
```

## To Use

To utilize the module in a python script first import it into your project with the line
To use, simply type:
```
from fuzzytime import *
```

The functions you can utilize are fuzzytime\(x), secondsago\(x) and minutesago\(x). To call them, type in the name and pass a single variable *x* of type datetime, time, date, string or epoch int. Note\: String dates can be in the format YYYY/MM/DD or YYYY\-MM\-DD whereas time strings must be in the format HH\:MM\:SS. For example:
```
x = "2017/12/12"

print fuzzytime(x) # Should output the time difference between today and Dec. 12th, 2017 in the form of a string
```

