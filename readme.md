 Regular  Expressions with python 

 here we use re module 

 Regular expression is an expression which is used inorder to specify  a set of strings
 suppose {room,room1,room2} are public rooms available instead of specifying each rooms  we can create an expression which  takes less space and can specify any  room 
here room(1|2)? can be a regular expression where ?== multiply by 0 or 1 , (1|2)== either 1 or 2  
so if we want to search room 2  we can  specify it by  room 2*1    where 2 is choosen from  1 or 2
there can be multiple regular expression for a set of  elements 
An example could be to check if in a given email field the users are entering valid emails which are in the valid email format   
