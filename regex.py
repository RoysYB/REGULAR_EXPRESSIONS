import re

#creating pattern
pattern=re.compile("expression")  #it is used  to compile  the given input("the regular expression") which is processed in form of strings  into a pattern object of regex 
#the  format  is    re.compile("expression",flags)
#where flags can be set as 
p=re.compile("green",flags=re.I)
#  which allows patterns of  upper and lower cases combined

#______________________________
#matching  functions 
  
  #match(): checks only at the beginnig(by default)
  #match("  ",pos,endpos)
k=p.match("green lantern")  #match object is returned if a match is found
print(type(k))
print(k)
print(k.span())#returns the index where the match of the input has been found
l=pattern.match("first expression here")
print(l)#this will retun none since no match was found because we used match function which checks the beginning
d=pattern.match("first expression", pos=6, endpos=17)
print(d)#pos and endpos specifies the index to begin and end search  endpos can be any big integer
 
 #search(): doesnot depend on value of pos 

search=pattern.search(" the  expression  is  here") 
print(search)#match object is returned if the pattern is found


 #findall(): returns all the strings same to that of the input
 #findall(" " ,pos=<int> ,endpos=<int> )  
findall=p.findall("that is a green car near to a green truck")
print(findall) #returns the same substring  not an object

digits=re.compile("\d")#\d represents all the digits
findall=digits.findall("1 tree 3 boys 4 girls 5 cats")
print(findall) #prints all the digits returned from the findall function


 #finditer(" ", pos=<int>,endpos=<int>)  
 #finds all  the same matching substrings and returns all of them as an iterator of the match object

pattern=re.compile("red")
finditer=pattern.finditer(" red roses are red  ")
for i in finditer: #print all the substrings matching the input
  print(i)

#we can give inputs like this also for a single case searching

i= re.findall("cat","cat women is not a cat") #search for cat in the  input string
print(i)


#__________________

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#suppose in this case
text="this cake costs about $100"
#if we want to search $100
amount=re.compile("$100")
k=amount.search(text)
print(k)# it will return none
#since $ is a metacharacter and has a special meaning in regex engine
#inorder to treat it as a literal use  \  
amount=re.compile("\$100")
k=amount.search(text)
print(k)
#now it works