Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> str(a)
'10'
>>> complex(a)
(10+0j)
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> b=10ii+0
SyntaxError: invalid syntax
>>> b = 10+oj
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b = 10+oj
NameError: name 'oj' is not defined
>>> b= 10 + 9A
SyntaxError: invalid syntax
>>> bool(a)
True
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> b (1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b (1,2,3,4,5)
NameError: name 'b' is not defined
>>> c={1,2,3,4,5,5}
>>> c
{1, 2, 3, 4, 5}
>>> int(a)
10
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a number, not 'set'
>>> set(c)
{1, 2, 3, 4, 5}
>>> list(c)
[1, 2, 3, 4, 5]
>>> bool(c)
True
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict(c)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dict (c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict (c)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> tuple(c)
(1, 2, 3, 4, 5)
>>> set(c)
{1, 2, 3, 4, 5}
>>> complex(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex(c)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> complex(a)
(10+0j)
>>> d= {10:,20:}
SyntaxError: invalid syntax
>>> d
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d={10:20:
   
SyntaxError: invalid syntax
>>> e={10:20:}
SyntaxError: invalid syntax
>>> e={10:20}
>>> complex(e)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex(e)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dict(c)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dict(e)
{10: 20}
>>> bool('')
False
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> c=(1,2,3,4,5,6,7)
>>> list(c)
[1, 2, 3, 4, 5, 6, 7]
>>> tuple(c)
(1, 2, 3, 4, 5, 6, 7)
>>> c.append(1,4,2)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.append(1,4,2)
AttributeError: 'tuple' object has no attribute 'append'
>>> str(bool)
"<class 'bool'>"
>>> bool(str)
True
>>> 
