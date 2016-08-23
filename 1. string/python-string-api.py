Python String API:
Strings

#Accessing Values in Strings
#Example
var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]

var1[0]:  H
var2[1:5]:  ytho


#String Formatting Operator
#Example
print "My name is %s and weight is %d kg!" % ('Zara', 21) 

My name is Zara and weight is 21 kg!


str.count(sub, start= 0,end=len(string))
# str = "this is string example....wow!!!";
# sub = "i";
# print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
# sub = "wow";
# print "str.count(sub) : ", str.count(sub)


# str.count(sub, 4, 40) :  2
# str.count(sub, 4, 40) :  1

find(str, beg=0 end=len(string))
# Determine if str occurs in string or in a substring of string 
# if starting index beg and ending index end are given returns index if found and -1 otherwise.
# str1 = "this is string example....wow!!!";
# str2 = "exam";

# print str1.find(str2)
# print str1.find(str2, 10)
# print str1.find(str2, 40)

# 15
# 15
# -1

str.index(str, beg=0 end=len(string))
#Same as find(), but raises an exception if str not found.


isalnum()
#This method returns true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
# str = "this2009";  # No space in this string
# print str.isalnum()

# str = "this is string example....wow!!!";
# print str.isalnum()

# True
# False
 
isalpha()
#Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

# str = "this";  # No space & digit in this string
# print str.isalpha()
# str = "this is string example....wow!!!";
# print str.isalpha()
# When we run above program, it produces following result −

# True
# False

  
isdigit()
#Returns true if string contains only digits and false otherwise.

# str = "123456";  # Only digit in this string
# print str.isdigit()

# str = "this is string example....wow!!!";
# print str.isdigit()

# True
# False


   
islower()
#Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
#str = "THIS is string example....wow!!!"; 
#print str.islower()

# str = "this is string example....wow!!!";
# print str.islower()
# When we run above program, it produces following result −

# False
# True


isnumeric()
#Returns true if a unicode string contains only numeric characters and false otherwise.
# str = u"this2009";  
# print str.isnumeric()

# str = u"23443434";
# print str.isnumeric()
# When we run above program, it produces following result −

# False
# True

  
isspace()
#This method returns true if there are only whitespace characters in the string and there is at least one character, false otherwise.
# str = "       "; 
# print str.isspace()

# str = "This is string example....wow!!!";
# print str.isspace()

# True
# False
    
isupper()
#This method returns true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise.
# str = "THIS IS STRING EXAMPLE....WOW!!!"; 
# print str.isupper()

# str = "THIS is string example....wow!!!";
# print str.isupper()



join(seq)
#Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
# s = "-";
# seq = ("a", "b", "c"); # This is sequence of strings.
# print s.join( seq )
# When we run above program, it produces following result −

# a-b-c


len(string)
#Returns the length of the string

 
ljust(width[, fillchar])
#Returns a space-padded string with the original string left-justified to a total of width columns.

# str = "this is string example....wow!!!";
# print str.ljust(50, '0')

# this is string example....wow!!!000000000000000000

lower()
#Converts all uppercase letters in string to lowercase.
#str = "THIS IS STRING EXAMPLE....WOW!!!";
#print str.lower()
    
lstrip()
#Removes all leading whitespace in string.
# str = "     this is string example....wow!!!     ";
# print str.lstrip()
# str = "88888888this is string example....wow!!!8888888";
# print str.lstrip('8')

# this is string example....wow!!!
# this is string example....wow!!!8888888

max(str)
# Returns the max alphabetical character from the string str.
# str = "this is really a string example....wow!!!";
# print "Max character: " + max(str)

# str = "this is a string example....wow!!!";
# print "Max character: " + max(str)

# Max character: y
# Max character: x
 
min(str)
#Returns the min alphabetical character from the string str.


replace(old, new [, max])
# Replaces all occurrences of old in string with new or at most max occurrences if max given.
# str = "this is string example....wow!!! this is really string";
# print str.replace("is", "was")
# print str.replace("is", "was", 3)

# thwas was string example....wow!!! thwas was really string
# thwas was string example....wow!!! thwas is really string

   
rfind(str, beg=0,end=len(string))
#This method returns last index if found and -1 otherwise. 
#Same as find(), but search backwards in string.

# str1 = "this is really a string example....wow!!!";
# str2 = "is";

# print str1.rfind(str2)

# print str1.rfind(str2, 0, 10)
# print str1.rfind(str2, 10, 0)

# print str1.find(str2)
# print str1.find(str2, 0, 10)
# print str1.find(str2, 10, 0)
# When we run above program, it produces following result −

# 5
# 5
# -1
# 2
# 2
# -1


rindex( str, beg=0, end=len(string))
#index(), but search backwards in string.

rjust(width,[, fillchar])
#Returns a space-padded string with the original string right-justified to a total of width columns.
# str = "this is string example....wow!!!";
# print str.rjust(50, '0')

# 000000000000000000this is string example....wow!!!

  
rstrip()
# Removes all trailing whitespace of string.
# str = "     this is string example....wow!!!     ";
# print str.rstrip()
# str = "88888888this is string example....wow!!!8888888";
# print str.rstrip('8')

#      this is string example....wow!!!
# 88888888this is string example....wow!!!

    
split(str="", num=string.count(str))
# Splits string according to delimiter str (space if not provided) and returns list of substrings; 
# split into at most num substrings if given.
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print str.split( )
# print str.split(' ', 1 )

# ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
# ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']

    
splitlines( num=string.count('\n'))
#Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

# str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
# print str.splitlines( )
# print str.splitlines( 0 )
# print str.splitlines( 3 )
# print str.splitlines( 4 )
# print str.splitlines( 5 )

# ['Line1-a b c d e f', 'Line2- a b c', '', 'Line4- a b c d']
# ['Line1-a b c d e f', 'Line2- a b c', '', 'Line4- a b c d']
# ['Line1-a b c d e f\n', 'Line2- a b c\n', '\n', 'Line4- a b c d']
# ['Line1-a b c d e f\n', 'Line2- a b c\n', '\n', 'Line4- a b c d']
# ['Line1-a b c d e f\n', 'Line2- a b c\n', '\n', 'Line4- a b c d']


startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.
# str = "this is string example....wow!!!";
# print str.startswith( 'this' )
# print str.startswith( 'is', 2, 4 )
# print str.startswith( 'this', 2, 4 )
# When we run above program, it produces following result −

# True
# True
# False

strip([chars])
#Performs both lstrip() and rstrip() on string


upper()
# Converts lowercase letters in string to uppercase.
# str = "this is string example....wow!!!";

# print "str.capitalize() : ", str.upper()
# THIS IS STRING EXAMPLE....WOW!!!

