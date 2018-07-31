name= input("what's your name? ")
length= len(name)
print ("your name is "+ str(length)+' letters long!')
if len(name)>10:
    print('your name is too long!')
else:
    print("hello there, "+name.capitalize())
firstle=name[0]
lastle=name[-1]
print('the first letter of your name is: '+firstle.capitalize())
print('the last letter of your name is: '+lastle.capitalize())
mood=input("so how do you feel today? ")
mood=mood.lower()
if mood=='good':
    print("Oh, I'm glad to hear that:)")
if mood=='bad':
    print("I hope you feel better!")


