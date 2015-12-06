# Copyright AN. December 2015
#!/usr/bin/python -tt

# Insertion Sort Algorithm
# Source : https://www.youtube.com/watch?v=c4BRHC7kTaQ

import sys
import random
import time
start_time = time.time()

def insertion_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	for i in range(1,len_of_array):
		j = i
		while (j > 0 and array[j]<array[j-1]):
		 array[j], array[j-1] = array[j-1], array[j]
		 j = j - 1
	return array	
		 
def main():
  if len(sys.argv) != 2:
    print 'usage: ./insertion_sort.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  array = random.sample(xrange(10000000), int(len_of_array))
  sorted_array = insertion_sort(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))