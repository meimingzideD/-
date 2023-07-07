Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def l(a,b,c,d):
...     k=(d-b)/(c-a)
...     m=b-k*a
...     return( 'y=%sx+%s'%(k,m))
... 
>>> def power(x,n=2):
...     s=1
...     while n>0:
...         n=n-1
...         s=x*s
...     return s
... 
>>> def genhao(n,x):
...     m=n/2
...     if m=float:
...         
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> def genhao(n,x):
...     m=n/2
...     if m==float:
...         if x>=0:
...             s=0
...             while power(s,n)=x
...             
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> def genhao(n,x):
...     m=n/2
...     if m==float:
...         if x>=0:
...             s=0
...             while power(s,n)==x
...             
SyntaxError: expected ':'
>>> def genhao(n,x):
...     m=n/2
...     if m==float:
...         if x>=0:
...             s=0
...             while power(s,n)==x:
...                 s=s+power(10,-10)
...             return s
...         else :
