#https://www.glassdoor.co.in/Interview/Reverse-a-string-of-words-Hi-I-am-John-as-John-am-I-Hi-without-using-array-functions-like-split-reverse-or-join-QTN_3012748.htm
# Reverse a string of words "Hi I am John" as "John am I Hi" without using array functions like split , reverse or join? 


s = "Hi I am John"
l = 0
c = ""
h = 0
while h < len(s):
    if s[h] == " ":
        c = " " + s[l:h] + c
        l = h+1
        
    h = h+ 1
c =  s[l:h] + c
print(c)
