Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='python programming'
>>> s.startswith('p')
True
>>> s.endswith('g')
True
>>> s.endswith('ing')
True
>>> 'y' isloer()
SyntaxError: invalid syntax
>>> 'y' .islower()
True
>>> 'code' .isalpha()
True
>>> '1234' .isalnum()
True
>>> 'code' .isnum()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    'code' .isnum()
AttributeError: 'str' object has no attribute 'isnum'
>>> 'code' .isalnum()
True
>>> 'sopher12e2@' .isalnum()
False
>>> 'my@var'.isidentifier()
False
>>> ' ' .isspace()
True
>>> '12.345' .isdecimal()
False
>>> 'a-b-c-d' .split()
['a-b-c-d']
>>> 'a-b-c-d-e' .rsplit()
['a-b-c-d-e']
>>> 'a-b-c-d' .rsplit()
['a-b-c-d']
>>> 'a-b-c-d' .partication()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'a-b-c-d' .partication()
AttributeError: 'str' object has no attribute 'partication'
>>>  'a-b-c-d' .partition()
 
SyntaxError: unexpected indent
>>>  'a-b-c-d' .rsplit('-',2)
 
SyntaxError: unexpected indent
>>> 'a,b,c,d' .split('-',2)
['a,b,c,d']
>>> l= 'a,b,c,d'
>>> '-'.join(l)
'a-,-b-,-c-,-d'
>>> '*&' .join(i)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    '*&' .join(i)
NameError: name 'i' is not defined
>>> '*&' .join(l)
'a*&,*&b*&,*&c*&,*&d'
>>> s='a-b-c-d'
>>> s.partition('s')
('a-b-c-d', '', '')
>>> s.rpartition('-')
('a-b-c', '-', 'd')
>>> .join('l','s')
SyntaxError: invalid syntax
>>> .join(s)
SyntaxError: invalid syntax
>>> s="hello"
>>> s.encode ()
b'hello'
>>> s.decode()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> t="hello"
>>> t.encode()
b'hello'
>>> t.encode()
b'hello'
>>> b'hello'.decode()
'hello'
>>> l=[1,2,3,4,5,6,7,8,9]
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(l)
<class 'list'>
>>> #types of features
>>> # mutable order duplicate hetrogeniues dynamic
>>> l=[1,2,3,4,5,6,"str",[1,2,3],(1,2)]
>>> l
[1, 2, 3, 4, 5, 6, 'str', [1, 2, 3], (1, 2)]
>>> l=['python','java,'oracle','string','mysql']
   
SyntaxError: invalid syntax
>>>  l=['python','java','string','mysql']
 
SyntaxError: unexpected indent
>>> s=['python','java','kuberneets','fastapi']
>>> s[1:3]
['java', 'kuberneets']
>>> s[-1:0]
[]
>>> s[-1:-3]
[]
>>> s[-1:-3:-1]
['fastapi', 'kuberneets']
>>> 'python in s"
SyntaxError: EOL while scanning string literal
>>> "python in s
SyntaxError: EOL while scanning string literal
>>> s[1:2:3]
['java']
>>> 'mysql' in s
False
>>> 'java in l
SyntaxError: EOL while scanning string literal
>>> 'java' in s
True
>>> s[-1:-2:-1]
['fastapi']
>>> len[s]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    len[s]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> len(s)
4
>>> sorted(s)
['fastapi', 'java', 'kuberneets', 'python']
>>> max(s)
'python'
>>> s.append('sql','object')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.append('sql','object')
TypeError: append() takes exactly one argument (2 given)
>>> s.append('a')
>>> s.extend(1,2,3,4,5,6,7)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.extend(1,2,3,4,5,6,7)
TypeError: extend() takes exactly one argument (7 given)
>>> s.extend([1,2,3,4,5,6,7])
>>> s
['python', 'java', 'kuberneets', 'fastapi', 'a', 1, 2, 3, 4, 5, 6, 7]
>>> max(s)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    max(s)
TypeError: '>' not supported between instances of 'int' and 'str'
>>> max('s')
's'
>>> s[s]
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s[s]
TypeError: list indices must be integers or slices, not list
>>> s[1]='html'
>>> s
['python', 'html', 'kuberneets', 'fastapi', 'a', 1, 2, 3, 4, 5, 6, 7]
>>> s.insert(2,'malco')
>>> 
