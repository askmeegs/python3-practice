
# given list of ints, return list of products of every int except the one at that index
# first, brute force solution-- O(n^2) time, O(n) space
def prod_all_brute(A):
    P = []
    for i in range(0, len(A)):
        # calculate product to pivot
        L = 1 # setup
        R = 1
        for x in range(0, i):
            L=L*A[x]
        # calculate product after pivot
        for y in range(i+1, len(A)):
            R=R*A[y]
        # append product of L, R products to P
        P.append(L*R)
    print(P)

#prod_all_brute([1,7,3,4])
#prod_all_brute([1,0,3,4])


# now do this in O(n) time, O(n) space
def prod_all_linear(A):
    P = [None] * len(A)

    accum = 1
    # go forwards (prod_all before index i )
    for i in range(0, len(A)):
        P[i] = accum #accum starts at 1 -- QUEUE UP
        accum *= A[i] #now for the next iteration, accum is the element before me


    accum = 1 #reset accum
    #go backwards (prod_all after index i )
    for i in range(len(A)-1, -1, -1):
        P[i] *= accum
        accum *= A[i]

    print(P)


prod_all_linear([1,7,3,4])
