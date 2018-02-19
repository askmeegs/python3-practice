"""
Background:
- Pancake has H side (w/ face) and B side (blank)
- Pancakes cooked in 1 row
- 1 flipper can flip K consecutive pancakes (but not their L-R order!)
- You must flip K pancakes in every flip, not K-1

Question:
- Given an initial row state of pancakes, find the minimum # of oversized flips to leave all pancakes H-side up
- OR state there is no way to do it

Input:
3
---+-++- 3
+++++ 4
-+-+- 4

Output:
Case #1: 3
Case #2: 0
Case #3: IMPOSSIBLE
"""

def solveFile(fname):
    with open(fname) as f:
        input = f.readlines()
        f.rea
        input = [x.strip() for x in input]
    output = []
    for i, case in enumerate(input):
        result = calcFlips(i, case)
        output.append(result)

    outfile = open('OUT_' + fname, 'w')
    for item in output:
        outfile.write("%s\n" % item)


"""
How many possible individual flips are there if you have a string S of length N, and a flipper of length K?

<------ N ------>
<- K ->

Total # flips = N-K+1 (+1 is the starting line state, at index 0 of S.)



Given that, how many possible configuartions


"""

def calcFlips(i, case):
    n = -1


    result = "IMPOSSIBLE"
    if n != -1:
        result = str(n)

    return "Case #%d: %s" % (i+1, result)




solveFile("tiny.txt")
