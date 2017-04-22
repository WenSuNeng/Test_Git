import os
print 'Process (%s) start ...' % os.getpid()
pid = os.fork()
if pid == 0
