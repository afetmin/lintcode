#!usr/bin/env python
#coding:utf-8

def Permutation(A, B):
	a=list(A)
	b=list(B)
	a.sort()
	b.sort()
	A=''.join(a)
	B=''.join(b)
	if A==B:
		print A+'为'+B+'的置换' 
	else:
		print A+'不是'+B+'的置换' 
	
if __name__ == '__main__':
	A = 'abc'
	B = 'cba'
	Permutation(A,B)

