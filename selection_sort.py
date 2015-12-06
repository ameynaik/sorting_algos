# Copyright AN. December 2015
#!/usr/bin/python -tt

# Selection Sort Algorithm
# Source : https://www.youtube.com/watch?v=6nDMgr0-Yyo


import sys
import random
import time
start_time = time.time()

def selection_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	for j in range(len_of_array):
		small_entry = array[j]
		small_index = j
		for i in range(j,len_of_array):
			if array[i] < small_entry:
				small_entry = array[i]
				small_index = i
		array[j],array[small_index] = array[small_index],array[j]		
	return array	
		 
def main():
  if len(sys.argv) != 2:
    print 'usage: ./selection_sort.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  array = random.sample(xrange(10000000), int(len_of_array))
  #print array
  sorted_array = selection_sort(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))