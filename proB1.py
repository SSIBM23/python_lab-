import re
string = "Anusha salary is 500000"
res = re.findall(r'[a-m]' ,string)
print(res)
res = re.search(r"\d" ,string)
print(res)
res = re.search("[^0-9]","123anu")
print(res)
res = re.findall(r'\d',string)
print(res)
res = re.split(r"\s",string)
print(res)
res = re.sub(r'\s',"-",string)
print(res)