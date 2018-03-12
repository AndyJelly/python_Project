# -*- coding:utf-8 -*-
# import os
#
#
import subprocess
from datetime import datetime
import threading


mutex = threading.Lock()


def find_ip(i, f):
    system_cmd = 'nbtstat -a 10.18.131.' + str(i)
    print(system_cmd)
    begin = datetime.now()
    r = subprocess.Popen(system_cmd, stdout=subprocess.PIPE).communicate()[0]
    mutex.acquire()
    f.write(bytes(system_cmd, encoding="utf8"))
    f.write(r)
    mutex.release()
    end = datetime.now()
    deltatime = (end-begin).total_seconds()
    print('execute %s success,spend %f.' % (system_cmd, deltatime))


if __name__ == '__main__':
    with open('monkeyrunner.log', 'wb+') as f:
        threads = []*254
        for i in range(1, 255):
            thread = threading.Thread(target=find_ip, args=(i, f))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()





