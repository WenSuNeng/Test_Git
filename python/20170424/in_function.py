def f(max):
	return max * max
def add(x,y,f):
	return f(x) + f(y)

print add(8, 9, f)
