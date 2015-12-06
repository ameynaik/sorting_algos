# Copyright AN. December 2015
#!/usr/bin/python -tt

# merge Sort Algorithm
# Source : https://www.youtube.com/watch?v=GCae1WNvnZM


import sys
import random
import time
start_time = time.time()

def merge_sort(array): # Array contains array to be sorted.
	len_of_array = len(array)
	i = 1
	level = 1
	while i < len_of_array:
		j = 0
		while j<len_of_array-i:
			sort_and_merge(array,level,j)
			j = j+2*i
		i = 2*i
		level = level + 1
	return array
	
def sort_and_merge(array,level,j):
	n = 2**(level) #Output Length of merged array.
	a = array[j:j+(n/2)]
	b = array[j+(n/2):j+n]
	c =[None]*n
	x = 0
	y = 0
	#print n,a,b
	for k in range(0,n):
		if x >= len(a):
			c[k:n] = b[y:(n/2)]
			break
		elif y >= len(b):
			c[k:n] = a[x:(n/2)]
			break
		else:
			if a[x] < b[y]:
				c[k] = a[x]
				x = x + 1
			else:
				c[k] = b[y]
				y = y + 1
	array[j:j+n] = c
	
	
	
		 
def main():
  if len(sys.argv) != 2:
    print 'usage: ./merge_sort.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  array = random.sample(xrange(10000000), int(len_of_array))
  #print array
  sorted_array = merge_sort(array)
  #print sorted_array


if __name__ == '__main__':
  main()
  print ("%s" % (time.time() - start_time))