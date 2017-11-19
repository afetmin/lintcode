#!usr/bin/env python
#coding: utf-8
s= 'lintcodelintcode'
for i,element in enumerate(s):
    if s.count(element) > 1:
        print -1
        break
    else:
        break
print i