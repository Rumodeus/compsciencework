#another quick booklet task
def pali(s):
    #returns true or false depending on whether the string is the same when reversed
    return s == s[::-1]
print("enter string")
s = input()
#checks length of string
s1 = len(s)
print("your string is", s1, "characters long including spaces")
#checks the length of the string when the spaces are removed
s2 = len(s.replace(" ", ""))
print("your string is", s2, "characters long excluding spaces")
#counts number of uppercase letters in string
s3 = sum(1 for c in s if c.isupper())
print("your string has", s3, "uppercase letters")
#counts number of lowecase letters in string
s4 = sum(1 for c in s if c.islower())
print("your string has", s4, "lowercase letters")
#converts string to lowercase
s5 = s.lower()
print("your string in lowercase is", s5)
#converts string to uppercase
s6 = s.upper()
print("your string in uppercase is", s6)
#runs the function we made earlier
s7 = pali(s)
if s7: 
    print("it is a palidrome")
else: 
    print("it isnt a palidrome")
#reverses the string
s8 = s[::-1]
print("your string in reverse is", s8)