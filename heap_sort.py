# Copyright AN. December 2015
#!/usr/bin/python -tt
# HeapSort algorithm
# Source : https://youtu.be/v1YUApMYXO4

from heap import * 
import sys
import random
import time
start_time = time.time()


def main():
  if len(sys.argv) != 2:
    print 'usage: ./heap_sort.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  #array = random.sample(xrange(10000000), int(len_of_array))
  array = random.sample(xrange(100), int(len_of_array))
  #print array
  sorted_array = heap_sort(array)
  #print sorted_array
  

def heap_sort(array): 
  heap = []
  for item in range(len(array)):
	AddElement(heap,array[item])

  SortedHeap = [];
  for item in range(len(array)):
	SortedHeap.append(heap[0])
	heap = RmElement(heap)
	#print heap
  return SortedHeap
  
  
if __name__ == '__main__':
  main()