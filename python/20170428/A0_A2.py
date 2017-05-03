A0 = (i for i in range(10) if i % 2 == 0)
print A0
A1 = {i:i+2 for i in A0}
print A1
A2 = sorted(A0,reverse = True)
print A2
