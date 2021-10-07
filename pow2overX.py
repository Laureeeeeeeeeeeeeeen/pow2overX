# pow2overX.py
# Lauren Arvanitis
# October 7th, 2021
# ---------------------------------------
# This program was created to demonstrate 
# to a friend that there does not exist a 
# power of 2 that is divisible by any
# prime number except for 2.




# Non-tweakable variables
i = 1
hit = 0 
import math

# Tweakable inputs
maxpower = 256
div = 3




while (i <= maxpower):
    if ( ( pow(2,i) % div) == 0 ):
        print( "%s is divisible by %s!" % ( pow(2,i), div ) )
        hit = hit + 1
    i = i + 1
    pass
if (hit == 0):
    print( "No power of 2 (from 2^1 to 2^%s) is divisible by %s." % ( maxpower, div )  )
else: 
    if (hit == 1):
        print( "There is 1 power of 2 (from 2^1 to 2^%s) that is divisible by %s." % ( maxpower, div )  )
    else:
        print( "There are %s powers of 2 (from 2^1 to 2^%s) that are divisible by %s." % ( hit, maxpower, div )  )