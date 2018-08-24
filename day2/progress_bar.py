# Author:Jay
#f.flush()#实时将内存中内容刷进硬盘
import sys
import time
for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)