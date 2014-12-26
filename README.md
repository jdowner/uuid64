uuid64
======


Introduction
------------

This is a simple script that generates a 64bit UUID. The normal type of UUID
(e.g. those available in the uuid module) are 128bit, which provides
substantially greater ability to avoid collision between generated values.
However, it is sometimes convenient to have a smaller UUID, e.g. if the number
of generated values is not terribly large or will not be generated in large
batches. Or, perhaps, due to a lack of support for 128bit integers.

The algorithm used to generate these UUIDs is very simple. The UUID consists of
two 32bit parts. The first part is base upon the current time (seconds since the
beginning of epoch). When UUIDs are not generated in batches, i.e. all at the
same time, the time acts as an incrementing value so that UUID generate many
seconds apart are almost certain to be different (note that clock timing on
different machines means that this is not a guarantee).

The second part is a 32bit random number taken from the system that the script
is running on, e.g. on linux the value is taken from /dev/urandom rather than a
pseudo-random generator.


Install
-------

To install uuid64 you can use pip,

```
pip install uuid64
```

or install from source using,

```
python setup.py install
```
