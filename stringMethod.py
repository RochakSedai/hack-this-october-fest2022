inform_str = """hello, my 
name is Rochak Sedai. I
am currently styudying in Trbhuwan University"""
if "Rochak" in inform_str:
    print("Rochak is in")

mylist = ["apple","ball","apple","cat","dog","elephant"]
print(mylist[2:])
print(len(mylist))
if "apple" in mylist:
    print("Yes, I am in the list..")

mylist[1:3] = ["Banana","Ant"]
mylist.insert(3,"Cow")
print(mylist)
mylist.append("orange")
print(mylist)
#creating the list using copnstructor
mylist1 = list(("apple","ball","apple","cat","dog","elephant"))
print(mylist1)
mylist.extend(mylist1)
print(mylist)
mylist.remove("apple")
print(mylist)

mytuples = ("Apple","Ball")
print(mytuples)
x = list(mytuples)
x.append("Cat")
mytuples = tuple(x)
print(mytuples)
for x in mytuples:
    print(x)
for i in range(len(mytuples)):
    print(mytuples[i])
tuples = mytuples * 2
print(tuples)
tuples = mytuples + tuples
print(tuples)

myset = {"ram","shyam","hari"}
print(myset)

mydict = {
    "brand":"Ford",
    "model":"mustang",
    "year":"1994"
}
print(mydict)
print(mydict["brand"])
print(mydict.keys())
mydict["color"] = "red"
print(mydict.keys())
mydict.update({"year":"1995"})
print(mydict)
mydict.popitem()
print(mydict)

def my_function(fname):
    print("Hello I am from a function")
    print(fname + " " +"arguments")

my_function("Email")

def arg_function(name,caste):
    print(name + " " + caste)
arg_function("Rochak","Sedai")

def point_function(*arg):
    print("The second arguments is" + arg[1])

point_function("hari","Ram","Shyam")

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\n Recursion Example results")
tri_recursion(6)

def factorial(k):
    if(k == 0):
        return 1
    elif(k == 1):
        return 1
    else:
        return k * factorial(k-1)

print(factorial(8))

def lambda_prac(n):
    return lambda a: a + n

mine_double = lambda_prac(3)
print(mine_double(2))