Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[23,34,45,67,89,76,54,33,45,65,76,]
>>> l
[23, 34, 45, 67, 89, 76, 54, 33, 45, 65, 76]
>>> l.pop(3)
67
>>> 
>>> l
[23, 34, 45, 89, 76, 54, 33, 45, 65, 76]
>>> l.remove(89)
>>> i.clear()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    i.clear()
NameError: name 'i' is not defined
>>> l.clear
<built-in method clear of list object at 0x0000000003CBFD88>
>>> l
[23, 34, 45, 76, 54, 33, 45, 65, 76]
>>> l.clear[]
SyntaxError: invalid syntax
>>> l.pop()
76
>>> l.clear()
>>> 
>>> l'
SyntaxError: EOL while scanning string literal
>>> l
[]
>>> l=[12,34,56,78,90,12,34,56,78,90,09]
SyntaxError: invalid token
>>> l=[12,34,56,78,90,12,34,56,78,90,09]
SyntaxError: invalid token
>>> l=[12,34,56,78,90,12,34,56,78,90]
>>> del l[1]
>>> l
[12, 56, 78, 90, 12, 34, 56, 78, 90]
>>> l.clear()
>>> l
[]
>>> l=[12,34,45,67,78,78,78,89,89,09,87,65,44,32,23,45]
SyntaxError: invalid token
>>> l=[12,34,45,67,78,78,78,89,89,87,65,44,32,23,45]
>>> l.count(12)
1
>>> l.sorted(l)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.sorted(l)
AttributeError: 'list' object has no attribute 'sorted'
>>> l.sort()
>>> l
[12, 23, 32, 34, 44, 45, 45, 65, 67, 78, 78, 78, 87, 89, 89]
>>> l.reverse()
>>> l
[89, 89, 87, 78, 78, 78, 67, 65, 45, 45, 44, 34, 32, 23, 12]
>>> l.sort()
>>> l
[12, 23, 32, 34, 44, 45, 45, 65, 67, 78, 78, 78, 87, 89, 89]
>>> l.reverse()
>>> l
[89, 89, 87, 78, 78, 78, 67, 65, 45, 45, 44, 34, 32, 23, 12]
>>> l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined
>>> l.sort(reverse=True)
>>> l
[89, 89, 87, 78, 78, 78, 67, 65, 45, 45, 44, 34, 32, 23, 12]
>>> a=[1,2]
>>> c=a
>>> c
[1, 2]
>>> a is c
True
>>> c.append(3)
>>> c
[1, 2, 3]
>>> a
[1, 2, 3]
>>> b=a.copy(12)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    b=a.copy(12)
TypeError: copy() takes no arguments (1 given)
>>> b= a.copy()
>>> any(l)
True
>>> l.append(0)
>>> l
[89, 89, 87, 78, 78, 78, 67, 65, 45, 45, 44, 34, 32, 23, 12, 0]
>>> all(l)
False
>>> k=[0,0.0,'']
>>> any[k]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    any[k]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> any(k)
False
>>> all(l)
False
>>> sum[l]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    sum[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> sum(l)
866
>>> t=()
>>> t=tuple()
>>> t=tuple((1,2,3,4))
>>> t
(1, 2, 3, 4)
>>> type(t)
<class 'tuple'>
>>> t=11,2,3,4,5
>>> t
(11, 2, 3, 4, 5)
>>> t=(1)
>>> t
1
>>> t=(4)
>>> t
4
>>> t=(1,2,3,4,5,6,7)
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> t[3]
4
>>> a,b,c,d=t
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a,b,c,d=t
ValueError: too many values to unpack (expected 4)
>>> a
[1, 2, 3]
>>> a,b,c,d=t
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a,b,c,d=t
ValueError: too many values to unpack (expected 4)
>>> a,b,c,d=t
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a,b,c,d=t
ValueError: too many values to unpack (expected 4)
>>> a,b,c=(1,2,3,4,5,6,7,8,9)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a,b,c=(1,2,3,4,5,6,7,8,9)
ValueError: too many values to unpack (expected 3)
>>> a,b,c=(1,2,3)
>>> a
1
>>> b
2
>>> c
3
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> t=t=(1,1.1,'hkly',[1,2,3],[1,2,3,4],{1,2,3,4})
>>>  >
 
SyntaxError: unexpected indent
>>> t
(1, 1.1, 'hkly', [1, 2, 3], [1, 2, 3, 4], {1, 2, 3, 4})
>>> t[3].append(1)
>>> t
(1, 1.1, 'hkly', [1, 2, 3, 1], [1, 2, 3, 4], {1, 2, 3, 4})
>>> t[3].append(1)
>>> t[2]
'hkly'
>>> t[3]
[1, 2, 3, 1, 1]
>>> a=(1,2,3,4)
>>> b=(5,4,3,1,2)
>>> a+b
(1, 2, 3, 4, 5, 4, 3, 1, 2)
>>> a*b
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> a*2
(1, 2, 3, 4, 1, 2, 3, 4)
>>> t
(1, 1.1, 'hkly', [1, 2, 3, 1, 1], [1, 2, 3, 4], {1, 2, 3, 4})
>>> t[2]
'hkly'
>>> t[-1]
{1, 2, 3, 4}
>>> t[-2:]
([1, 2, 3, 4], {1, 2, 3, 4})
>>> t[-2::]
([1, 2, 3, 4], {1, 2, 3, 4})
>>> t[::-2]
({1, 2, 3, 4}, [1, 2, 3, 1, 1], 1.1)
>>> 1 in t
True
>>> false in t
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    false in t
NameError: name 'false' is not defined
>>> true not in t
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    true not in t
NameError: name 'true' is not defined
>>> t
(1, 1.1, 'hkly', [1, 2, 3, 1, 1], [1, 2, 3, 4], {1, 2, 3, 4})
>>> len(t)
6
>>> sorted(t)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
>>> max(t)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'
>>> t=[1,2,3,4,5,6,7,9]
>>> sum(t)
37
>>> sorted(t)
[1, 2, 3, 4, 5, 6, 7, 9]
>>> max(t)
9
>>> min(t)
1
>>> count (2)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    count (2)
NameError: name 'count' is not defined
>>> len(t)
8
>>> any(t)
True
>>> all(t)
True
>>> t.append(0)
>>> all(t)
False
>>> any(t)
True
>>> s=se()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    s=se()
NameError: name 'se' is not defined
>>> s={90,67,45,67,23,45,67}
>>> s
{90, 67, 45, 23}
>>> #properties unordered universal mutable hetrogenius dynamic
>>> s={1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> s.append("str")
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    s.append("str")
AttributeError: 'set' object has no attribute 'append'
>>> s.add(1)
>>> s
{1, 2, 3, 4, 5}
>>> s.add("str")
>>> s
{1, 2, 3, 4, 5, 'str'}
>>> s
{1, 2, 3, 4, 5, 'str'}
>>> s={1,'str',12}
>>> s
{1, 12, 'str'}
>>> s.add(2+3j)
>>> s
{1, (2+3j), 12, 'str'}
>>> s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
>>> # set operations
>>> a={1,2,3,4,5,6}
>>> b={4,5,6,98,8}
>>> a | b
{1, 2, 3, 4, 5, 6, 98, 8}
>>> a^b
{1, 98, 2, 3, 8}
>>> a&b
{4, 5, 6}
>>> a.isdisjoint(b)
False
>>> a-b
{1, 2, 3}
>>> a+b
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a.iddisjoint({2,3})
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    a.iddisjoint({2,3})
AttributeError: 'set' object has no attribute 'iddisjoint'
>>> {100,99}.issubset(a)
False
>>> {1,2,3,4,5,6,7}.issuperset(a)
True
>>> 
