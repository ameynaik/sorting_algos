# Copyright AN. December 2015
#!/usr/bin/python -tt

# bubble Sort Algorithm
# Source : https://www.youtube.com/watch?v=P00xJgWzz2c


import sys
import random
import time
start_time = time.time()

def bubble_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	for j in range(len_of_array):
		for i in range(j,len_of_array):
			if array[i] < array[j]:
				array[j],array[i] = array[i],array[j]		
	return array	
		 
def main():
  if len(sys.argv) != 2:
    print 'usage: ./bubble_sort.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  array = random.sample(xrange(10000000), int(len_of_array))
  #print array
  sorted_array = bubble_sort(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))