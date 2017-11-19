#!usr/bin/env python
#coding: utf-8

l = -1212345
# rev=list(str(l))[::-1]
# print rev
# a = ''.join(rev)
# print int(a)
print `l`
x = -123
s = cmp(x, 0)
r = int(`s*x`[::-1])
# return s*r * (r < 2**31)
print s*r