def selec(a,size):
   for i in range(size):
      min=i
      for j in range(i+1,size):
         if a[j]<a[min]:
              min=j
      a[i],a[min]=a[min],a[i]
a=[-2,45,0,11,-9]
print(f"before sorting {a}")
size=len(a)
selec(a,size)
print(f"after sorting {a}")