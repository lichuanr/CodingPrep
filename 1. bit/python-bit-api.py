a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

#Operator copies a bit to the result if it exists in both operands	
c = a & b;        # 12 = 0000 1100
print "Line 1 - Value of c is ", c

#It copies a bit if it exists in either operand.	
c = a | b;        # 61 = 0011 1101 
print "Line 2 - Value of c is ", c

#It copies the bit if it is set in one operand but not both.	
c = a ^ b;        # 49 = 0011 0001
print "Line 3 - Value of c is ", c

#It is unary and has the effect of 'flipping' bits.
c = ~a;           # -61 = 1100 0011
print "Line 4 - Value of c is ", c 
Notes: ~n = -n - 1

#The left operands value is moved left by the number of bits specified by the right operand.	
c = a << 2;       # 240 = 1111 0000
print "Line 5 - Value of c is ", c

#The left operands value is moved right by the number of bits specified by the right operand.	
c = a >> 2;       # 15 = 0000 1111
print "Line 6 - Value of c is ", c

#Result
Line 1 - Value of c is 12
Line 2 - Value of c is 61
Line 3 - Value of c is 49
Line 4 - Value of c is -61
Line 5 - Value of c is 240
Line 6 - Value of c is 15