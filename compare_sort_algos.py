# Copyright AN. December 2015
#!/usr/bin/python -tt

# Compare Sorting Algorithms
# For the same random input, prints the time taken by each of the sorting algorithms
# Sorting Algorithms compared are Insertion, Selection, Bubble, Merge.

import sys
import random														
import time
import insertion_sort
import selection_sort
import bubble_sort
import merge_sort
import quick_sort
import heap_sort

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

start_time = time.clock()


def main():
  if len(sys.argv) != 2:
    print 'usage: ./compare_sort_algos.py --len_of_array'
    sys.exit(1)

  len_of_array = sys.argv[1] # This argument has length of the array to be sorted.
  print len_of_array
  # Create Random numbers of this length. The random numbers generated are unique.
  array = random.sample(xrange(10000000), int(len_of_array))
  #print array
  sorted_array = insertion_sort.insertion_sort(array)
  insertion_time = time.clock()
  insertion_tot = insertion_time - start_time
  print ("Insertion Sort %s" % insertion_tot)
  sorted_array = selection_sort.selection_sort(array)
  selection_time = time.clock()
  selection_tot = selection_time - insertion_time
  print ("Selection Sort %s" % (selection_tot))
  sorted_array = bubble_sort.bubble_sort(array)
  bubble_time = time.clock()
  bubble_tot = bubble_time - selection_time
  print ("Bubble Sort %s" % (bubble_tot))
  sorted_array_m = merge_sort.merge_sort(array)
  merge_time = time.clock()
  merge_tot = merge_time - bubble_time
  print ("Merge Sort %s" % (merge_tot))
  sorted_array_q = quick_sort.quick_sort(array)
  quick_time = time.clock()
  quick_tot = quick_time - merge_time
  print ("Quick Sort %s" % (quick_tot))
  sorted_array_h = heap_sort.heap_sort(array)
  heap_time = time.clock()
  heap_tot = heap_time - quick_time
  print ("Heap Sort %s" % (heap_tot))
  
  objects = ('Insertion', 'Selection', 'Bubble', 'Merge','Quick','Heap')
  y_pos = np.arange(len(objects))
  performance = [insertion_tot/merge_tot,selection_tot/merge_tot,bubble_tot/merge_tot,merge_tot/merge_tot,quick_tot/merge_tot,heap_tot/merge_tot]
 
  if (sorted_array_m == sorted_array_q):
	print "Merge and Quick sorts are giving the same sorted array results"
  plt.bar(y_pos, performance, align='center', alpha=0.5)
  plt.xticks(y_pos, objects)
  plt.ylabel('Time taken w.r.t merge sort')
  plt.title('Sorting Techniques')
 
  plt.show()
  

  #print sorted_array


if __name__ == '__main__':
  main()