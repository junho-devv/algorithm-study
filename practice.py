from random import randint
import time

array = []

for _ in range(10000):
  array.append(randint(1, 100))

start_time = time.time()

for x in range(len(array)):
  min_index = x
  for y in range(x+1, len(array)):
    if array[min_index] > array[y]:
      min_index = y
  array[x], array[min_index] = array[min_index], array[x]
  print(array)

end_time = time.time()

print("selective sorting : ", end_time - start_time)

start_time = time.time()

array.sort()

end_time = time.time()

print("internal sorting : ", end_time - start_time)