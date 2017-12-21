#assign all type varible in python
dictionary={}
arraylist=[]
string="word"
integer=1
x=3

# tacke integer input from user
value1=int(input("enter integer value"))
print("this is integer val:",value1)

# tacke float input from user
value2=float(input("enter float value"))
print("this is float val",value2)

#enter string
value3=input("enter string")
print("this is string:",value3,"\nthis is another string:",string)

#foor loop
for x in range(10):
   dictionary.setdefault("age", []).append(x)
print("this is decionery",dictionary,"\nthis is vales for key in decionery:",dictionary.get("age"))

#for loop value in something
for k,v in dictionary.items():
    if 3 in v or 4 in v:
        print("hello")

#wile loop
while x:
    x-=1
    print("hi")

#how to write function
def sum(a,b):
    z=a+b
    return z
print(sum(3,4))

#how to make class in python
class prson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
person=prson("ali",29)
print(person.name)