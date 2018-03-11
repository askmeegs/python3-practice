
def quicksort_not_in_place(x):
    # base case - 1-element subarray
      if len(x) < 2:
          print "BASE CASE: x is currently  - done! \n\n" + str(x)
          return x
    # recursive case:
            # choose pivot value to be the first elt of list x
            # perform a PARTITION resulting in lists: lessThan pivot to the left, greaterThan pivot to the right
                    # less copied into new list
                    # greater copied into list
            # perform quicksort on lessThan
            # perform quicksort on greaterThan
      else:
          print "RECURSIVE CASE: pivot is x[0], and x is currently - "
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          print "... concating less (%s), pivot (%s), and greater (%s)" % (str(less), str(pivot), str(greater))
          return quicksort_not_in_place(less) + [pivot] + quicksort_not_in_place(greater)


L = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
print quicksort_not_in_place(L)
