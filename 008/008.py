"""
Project Euler Problem 8
=======================

Find the greatest product of thirteen consecutive digits in the 1000-digit
number.

            73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450


"""
# first remove all the \n and glue all the numbers into a very long str
# then remove all the zeros
# then loop through the 13-digits-block to find the max product
filename = 'n.txt'
fd = open(filename)
m = 0                              # store the max product
longstr = str()                      # store the very long str
for line in fd:
    line = line.strip()              # remove the spaces and \n
    for items in line:
        longstr += items
l = len(longstr)
line = line.split("0")
for pieces in line:
    if len(pieces) >= 13:
        # loop throug l - 13 blocks, +1 cuz the last number in range() will not
        # be included
        for i in range(0, l - 13 + 1):
            block = longstr[i:i + 13]
            product = 1                      # clear the previous value
            for digits in block:
                product *= int(digits)
            if product > m:
                m = product
print(m)
