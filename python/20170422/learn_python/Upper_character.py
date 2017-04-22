#!/usr/bin/python
# -*- coding: utf-8 -*-
def charLower(x):
	return x.lower()

def charUpper(x):
	return x.upper()

def parseText(name):
	str = charUpper(name[:1]) + charLower(name[1:])
        return str

if __name__ == '__main__':
	L = ['adam','LISA', 'barT']
	print map(parseText,L)

