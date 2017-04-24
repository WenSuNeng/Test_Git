def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 2
	print 'step 3'
	yield 3

o = odd()
print o.next()
print o.next()
print o.next()
print o.next()
