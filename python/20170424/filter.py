def not_empty(s):
	return s and s.strip()
print filter(not_empty, ['','B',None, 'C', ' '])

