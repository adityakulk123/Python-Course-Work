Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ("heelo world")
heelo world
>>> n='2'
>>> b='8'
>>> a='n+b'
>>> print(a)
n+b
>>> b=n+b
>>> print (b)
28
>>> c=b+n
>>> print (C)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print (C)
NameError: name 'C' is not defined
>>> print(c)
282
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist))
35
>>>  import keyword
print(keyword.kwlist)

SyntaxError: unexpected indent
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> b
10
>>> a
20
>>> 
