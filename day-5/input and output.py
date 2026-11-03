Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bitwise operator
>>> 5&4
4
>>> 11|12
15
>>> 8|9
9
>>> 11^12
7
>>> ~11
-12
>>> ~909
-910
>>> 11&12
8
\
>>> 2<<2
8
>>> 2>>2
0
>>> 12>>>1
SyntaxError: invalid syntax
>>> 12>>>14
SyntaxError: invalid syntax
>>> 12>>14
0
>>> 12>>2
3
>>> a= input("enter a number ")
enter a number 12wew3
>>> a
'12wew3'
>>> type(a)
<class 'str'>
>>> b=100
>>> b
100
>>> type(b)
<class 'int'>
>>> a=input()
123
>>> a
'123'
>>> a=int(input(enter number ))
SyntaxError: invalid syntax
>>> a=int(input("enter a number "))
enter a number 12
>>> a=list(int,input().splite())
12,34,5,0,689
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a=list(int,input().splite())
AttributeError: 'str' object has no attribute 'splite'
>>> a=list(int,input().split())
12,34,56,78,99,0
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a=list(int,input().split())
TypeError: list expected at most 1 arguments, got 2
>>> a=list(map(int,input().splite()))
12,45,67
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a=list(map(int,input().splite()))
AttributeError: 'str' object has no attribute 'splite'
>>>  a=list(map(int,input().split()))
 
SyntaxError: unexpected indent
>>>  c=list(map(int,input().split()))
 
SyntaxError: unexpected indent
>>> c=list(map(int,input().split()))
 
12,34,56
SyntaxError: multiple statements found while compiling a single statement
>>> a=list(int,input().split())
12 34 56 78
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a=list(int,input().split())
TypeError: list expected at most 1 arguments, got 2
>>> D=list(map(int,input().split()))
12 2 3 45 
>>> D
[12, 2, 3, 45]
>>> D=list(int,input().split())
12 12 34 56 78
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    D=list(int,input().split())
TypeError: list expected at most 1 arguments, got 2
>>> a,b,c=list
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a,b,c=list
TypeError: cannot unpack non-iterable type object
>>> a,b,c=list(map(int,input().split()))
1 2 3
>>> a
1
>>> b
2
>>> c
3
>>> email,password = input().split()
adityakulkarni156@gmail.com 14323
>>> email
'adityakulkarni156@gmail.com'
>>> password
'14323'
>>> a=eval(input())
1 2 3 
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    1 2 3
      ^
SyntaxError: invalid syntax
>>> a=eval(input())
[1,2,3]
>>> a
[1, 2, 3]
>>> a=eval(input())
{1:1,2:2,3:3,4:4}
>>> a
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a= 10
>>> b=20
>>> c= 'codegnan'
>>> a,b,c
(10, 20, 'codegnan')
>>> print (f'a,b,c')
a,b,c
>>> print (f'"a=",a,"b=",b,"c=",c')
"a=",a,"b=",b,"c=",c
>>> print ("a=",a,"b=",b,"c=",c)
a= 10 b= 20 c= codegnan
>>> print (f'"a=",a,"b=",b,"c=",c' sep="")
SyntaxError: invalid syntax
>>> print (f'"a=",a,"b=",b,"c=",c'sep='')
SyntaxError: invalid syntax
>>> print ("a=",a,"b=",b,"c=",c sep='')
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> print ("a=",a,"b=",b,"c=",c sep='')
SyntaxError: invalid syntax
>>> print ("a=",a,"b=",b,"c=",c sep='-')
SyntaxError: invalid syntax
>>> print ("a=",a,"b=",b,"c=",c ,end='@')
a= 10 b= 20 c= codegnan@
>>> print ("a=",a,"b=",b,"c=",c ,sep='')
a=10b=20c=codegnan
>>> 
