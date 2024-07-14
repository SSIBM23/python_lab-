boxoffice={}
for i in range(0,4):
 key=input("enter key:")
 value=input("enter value:")
 boxoffice[key]=value
print(boxoffice)
print("length of dictionary:",len(boxoffice))
boxoffice["avatar"]=2009
print("dictionary after modification:",boxoffice)
print("titanic is present:","titanic" in boxoffice)
print("titanic was released in the year:",boxoffice.get("titanic",1997))
print("dictionary keys are:",boxoffice.keys())
print("dictionary values are:",boxoffice.values())
print("pop item from dictionary",boxoffice.popitem())
boxoffice.setdefault("harrypotter",2011)
print("after setting harrypotter:",boxoffice)
boxoffice.update({"frozen":2013})
print("after inserting new item",boxoffice)