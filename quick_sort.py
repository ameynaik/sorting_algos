# Copyright AN. January 2016
#!/usr/bin/python -tt

# Quick Sort Algorithm
# Source : https://www.youtube.com/watch?v=y_G9BkAm6B8


import sys
import random
import time
start_time = time.time()

def quick_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	partition(array,0,len_of_array-1)
	return array
	
def partition(array,first,last):
	size = last-first+1
	subarr = array[first:last+1]
	if(size < 2):
		return array
	pivot = subarr[random.randint(1, 1000000)%size]
	
	L = 0
	U=size-1
	while L<U:
		while subarr[L]<pivot:
			L = L + 1
		while subarr[U]>pivot:
			U = U - 1
		subarr[L],subarr[U] = subarr[U],subarr[L] #Swap
	array[first:last+1] = subarr
	partition(array,first,L-1+first)
	partition(array,L+first,first+L+size-L-1)
	
	return array

	
	
	
		 
def main():
  if len(sys.argv) != 2:
    print 'usage: ./quick_sort.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  array = random.sample(xrange(10000000), int(len_of_array))
  sorted_array = quick_sort(array)


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))
