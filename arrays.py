def enter ( a , n ):
 for i in range(n):
  e=input("Enter element %d = " %(i+1) )
  e=int(e,10)
  a.append(e)
def deldup(a):
 arr=[]
 for i in a:
  while a.count(i)>1 :
   ind=a.index(i)
   arr=a[(ind+1):]
   arr.remove(i)
   a[(ind+1):]=arr
def rotlist(list,rot):
 s=len(list)
 list1=list.copy()
 list1[:rot]=list[s-rot:]
 list1[rot:]=list[:s-rot]
 return list1
def prdup(a):
 dup=[]
 for i in a:
  if a.count(i)>1 : 
   dup.append(i)
 print ( dup )
def isdist(a):
 for i in a:
  if a.count(i)>1:
   print(i)
   return False
 return True
def freqtable(a):
 freq_tab={}
 b=a.copy()
 deldup(b)
 for i in b:
  freq_tab[i]=a.count(i)
 return freq_tab
def sortfreq ( arr , ord ):
 if ord=="a" or ord=="A":
  tab=freqtable(arr)
  l=[]
  for i in tab:
   t=(tab[i],i)
   l.append(t)
  l.sort()
  ret=[]
  for i in l:
   ret.append(i[1])
 else:
  tab=freqtable(arr)
  l=[]
  for i in tab:
   t=(tab[i],i)
   l.append(t)
  l.sort()
  l.reverse()
  ret=[]
  for i in l:
   ret.append(i[1])
 return ret
def chksort(a): 
 flag=-1
 n=len(a)
 if a[0]<a[1]:
  flag=1
 elif a[0]>a[1]:
  flag=0
 for i in range(n):
  if i==n-1: break
  if (a[i]>a[i+1] and flag!=0) or (a[i]<a[i+1] and flag!=1):
   return 'N'
 if flag==0:
  return 'D'
 elif flag==1:
  return 'A'
 else:
  return 'E'