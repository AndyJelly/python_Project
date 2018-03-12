# -*- coding:utf-8 -*-
# from operator import add
# from functools import reduce
# from datetime import datetime
#
#
# def func():
#     begin = datetime.now()
#     ret = []
#     ret.append(2)
#
#     for i in range(3, 1000000, 2):
#         bexit = False
#         for j in range(2, int(i**.5) + 1):
#             if i % j == 0:
#                 bexit = True
#                 break
#         if not bexit:
#             ret.append(i)
#     result = reduce(add, ret[:])
#     end = datetime.now()
#     deltatime = (end - begin).total_seconds()
#     print('execute success,spend %f.' % deltatime)
#     print(result)
#
#     begin2 = datetime.now()
#     ret = [i for i in range(3, 2000000, 2) if not [i % j for j in range(2, int(i**.5) + 1) if i % j == 0]]
#     ret.append(2)
#     result2 = reduce(add, ret[:])
#     end2 = datetime.now()
#     deltatime2 = (end2 - begin2).total_seconds()
#     print('execute success,spend %f.' % deltatime2)
#     print(result2)
#
#
# if __name__ == '__main__':
#     func()


from itertools import compress
def primes(lim):
  assert lim>2
  BA = bytearray
  n = (lim-1)//2
  prime = BA([1])*(n+1)
  prime[0] = 0 # 2*0+1 = 1 n'est pas premier
  # Crible
  for i in range((int(lim**0.5)+1)//2):
    if prime[i]:
      p = 2*i+1 # p est premier
      i2 = i*(i+1)<<1
      prime[i2::p]=BA(1+ (n-i2)//p )
  return compress(range(1,lim+1,2),prime)

# for i in range(3, 30):  # tests
#   print(i, list(primes(i)))

print(2+sum(primes(2*10**6)))
