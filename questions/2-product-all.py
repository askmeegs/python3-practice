# interview cake - product of all other numbers

"""
Given a list of ints, return a list of products of every integer except the integer at that index.

given:   [1, 7, 3, 4]
return [7*3*4, 1*3*4, 1*7*4, 1*7*3]

constraint: not allowed to use division

"""

def prod_all(A):
    P = []
    for i in range(0, len(A)):
        # calculate product to pivot
        L,R = 1 # setup
        for x in range(0, i):
            L=L*A[x]
        # calculate product after pivot
        for y in range(i+1, len(A))
            R=R*A[y]
        # append product of L, R products to P
        P.append(L*R)
    return P



print prod_all([1,7,3,4])
