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
# there are 12  metacharacters which are
#  \,^,$,.,|,?,*,+,(,),[,{



#special case
#\ is also a metacharacter so use \\ 
#in case of \
txt="""C:\Windows\System32"""
pattern=re.compile("C:\Windows\System32")
print(pattern.search(txt))#this will be none since \ is a metacharacter
#so
pattern=re.compile("C:\\Windows\\System32")
print(pattern.search(txt))#but this is also giving none
#it happens because of python interpreter since it also use \ for escaping  ( like  \n ) 
print("this is \\ me")#here the \\ is used as an escape sequence by the interpreter
#a way to perform would be
pattern=re.compile("C:\\\\Windows\\\\System32")
print(pattern.search(txt))
#so we have to use \\\\ for a single \
#another way could be to use  raw string
print(r"this is \n me")#the string is treated as raw
#so another way would be 
pattern=re.compile(r"C:\\Windows\\System32")
print(pattern.search(txt))
#we  can use escape() to escape metacharacters
print(re.escape("C:\Windows"))
# it outputs the escaped string  as C:\\windows
#so we can use as
pattern=re.compile(re.escape("C:\Windows\System32"))
print(pattern.search(txt))
#escape will escape all  metacharacters  so use if you dont need any metacharacter usecase


#character classes
#it allows us to define if a character that will match if any of the defined characters on the set is present
#ie for example  if  we have to find two words  beans and jeans where only first word only has a change so we can use a characer classes like
pattern=re.compile("[jb]eans")#here we have [] which are metacharacters for characters , so whatever characters are inside the brackets  any one from them could be at that place
print(pattern.findall("there was beans found in his jeans"))#so we used a single pattern for  two words



#character set range
#as the name says it describes a range
# supppose  [0123456789]  we can define it as [0-9]
#so we can use  , [A-Z],[a-z0-9A-Z]
pattern=re.compile("[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9]")
print(pattern.findall("    MESSI11     "))


# ^ symbol
#so in a character set whatever characters are after ^ none of  those characters wont be  taken as a pattern

pattern=re.compile("[^b]at")#so after ^ b is there so that whatever character except b in that place will be considered
print(pattern.findall("we played with a bat and sat ")) #so bat wont be taken


#predefined character classes
""" 
these elements are predefined so that we can use it instead of its equivalent symbols

.     this will match any character except newline
\d    matches any digit                      equivalent to[0-9]
\D    any non digit                          equivalent to[^0-9] 
\s    whitespaces                            equivalent to[\t\n\r\f\v] 
\S    any non whitespace                     equivalent to[^\t\n\r\f\v]
\w    any alphanumeric characters            equivalent to[a-zA_Z0-9]
\W    any non alphanumeric characters        equivalent to[^a-zA_Z0-9] 
"""
pattern=re.compile("b\w\w")# here we used instead of bat
print(pattern.findall("we played with a bat and sat ")) 
