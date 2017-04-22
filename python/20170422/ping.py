import os
return1 = os.system('ping 8.8.8.8 -c 2')
if return1:
    print 'ping fail'
else:
    print 'ping ok'
