Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'python'
>>> p='programming'
>>> s
'python'
>>> s+p
'pythonprogramming'
>>> 
>>> 
>>> 



>>> 

>>> 


>>> 

>>> 

>>> s+p*3
'pythonprogrammingprogrammingprogramming'
>>> s*9
'pythonpythonpythonpythonpythonpythonpythonpythonpython'
>>> a='op'
>>> a*
SyntaxError: invalid syntax
>>> a*9
'opopopopopopopopop'
>>> s='python is a very good language '
>>> s[0]
'p'
>>> s[9]
' '
>>> s[13]
'e'
>>> s[-7]
'n'
>>> s[6:0:1]
''
>>> s[0:6:1]
'python'
>>> s[-6:-13:-1]
'gnal do'
>>> s[0:6:2]
'pto'
>>> s[::-1]
' egaugnal doog yrev a si nohtyp'
>>> s[0::6]
'p von '
>>> s[0::6:1]
SyntaxError: invalid syntax
>>> s[0:6:1]
'python'
>>> s[0:6:2]
'pto'
>>> 'python' in s
True
>>> 'good' in s
True
>>> 'vthi' in s
False
>>> len(s)
31
>>> ord('y')
121
>>> ord('s')
115
>>> ord('+')
43
>>> ord
<built-in function ord>
(
>>> ord('D')
68
>>> sorted(s)
[' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'd', 'e', 'e', 'g', 'g', 'g', 'h', 'i', 'l', 'n', 'n', 'o', 'o', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'y']
>>> s.upper()
'PYTHON IS A VERY GOOD LANGUAGE '
>>> s.lowercase()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.lowercase()
AttributeError: 'str' object has no attribute 'lowercase'
>>> s.lower()
'python is a very good language '
>>> s.casefold()
'python is a very good language '
>>> s.title()
'Python Is A Very Good Language '
>>> s.cqptalize
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s.cqptalize
AttributeError: 'str' object has no attribute 'cqptalize'
>>> s.capitliaze()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.capitliaze()
AttributeError: 'str' object has no attribute 'capitliaze'
>>> s.capitliaze
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.capitliaze
AttributeError: 'str' object has no attribute 'capitliaze'
>>> s.capitliaze()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.capitliaze()
AttributeError: 'str' object has no attribute 'capitliaze'
>>> s.capitliaze()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.capitliaze()
AttributeError: 'str' object has no attribute 'capitliaze'
>>> s
'python is a very good language '
>>> s.capitaliaze()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    s.capitaliaze()
AttributeError: 'str' object has no attribute 'capitaliaze'
>>>  s.capitaliaze()
 
SyntaxError: unexpected indent
>>>  s.capitaliaze()
 
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> s.capitalize()
'Python is a very good language '
>>> s.center(20,'*')
'python is a very good language '
>>> s=python
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s=python
NameError: name 'python' is not defined
>>> s
>>> s = python
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s = python
NameError: name 'python' is not defined
>>> b = bython
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b = bython
NameError: name 'bython' is not defined
>>> NameError: name 'bython' is not defined
SyntaxError: invalid syntax
>>> 
>>> 
>>> a = 'python'
>>> a.center(40,'*')
'*****************python*****************'
>>> '1'.zfill(5)
'00001'
>>> s = "python is very nice language"
>>> s
'python is very nice language'
>>> s.find('n')
5
>>> s.rfind('n')
22
>>> s.lfind('n')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.lfind('n')
AttributeError: 'str' object has no attribute 'lfind'
>>> s.inded('f')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.inded('f')
AttributeError: 'str' object has no attribute 'inded'
>>> s.index('f')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.index('f')
ValueError: substring not found
>>> s.strip()
'python is very nice language'
>>> s.rsrip()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    s.rsrip()
AttributeError: 'str' object has no attribute 'rsrip'
>>> s.rstrip()
'python is very nice language'
>>> s.strip()
'python is very nice language'
>>> s.replace('p','1')
'1ython is very nice language'
>>> s.replace ('n','1')
'pytho1 is very 1ice la1guage'
>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> 
