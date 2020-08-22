#This module contains functions and classes intended for developing new methods of encryption.
#Note: 'arrays' and 'number_oper' are custom-made modules for array and number theory related operations respectively.

import arrays
import random
import number_oper
#The following function returns a string with characters in the order
#A-Z, a-z, 0-9, special characters
def init_chrs(chrs):
 for i in range(65,91):
  chrs.append(chr(i))
 for i in range(97,123):
  chrs.append(chr(i))
 for i in range(48,58):
  chrs.append(chr(i))
 for i in range(33,48):
  chrs.append(chr(i))
 for i in range(58,65):
  chrs.append(chr(i))
 for i in range(91,97):
  chrs.append(chr(i))
 for i in range(123,127):
  chrs.append(chr(i))
 chrs.append(' ')
 return ''.join(chrs)

chset=[]
chset=init_chrs(chset)
#Function to return nth permutation of a string as obtained by recursion-backtracking method.
res=[]
c=0
done=False
def per(l,u,s,n):
 global done,c
 if (l==u) and (''.join(s) not in res):
  res.append(''.join(s))
  c+=1
  if c==n:
   done=True
 else:
  for i in range(l,u+1):
   if done: break
   else:
    temp=s[i]
    s[i]=s[l]
    s[l]=temp
    per(l+1,u,s,n)
    temp=s[i]
    s[i]=s[l]
    s[l]=temp

class cipher1:
 def __init__(self,b=47,r=47,p=1):
  self.br_point=b
  self.rot=r
  self.per_loc=p
  ch=[]
  ch=init_chrs(ch)
  ch=list(ch)
  per(0,94,ch,p)
  ch=res[-1]
  s1=ch[:b]
  print('s1:\n')
  print(s1)
  s2=ch[b:]
  print('s2:\n')
  print(s2)
  s1=list(s1)
  s1.reverse()
  s1=''.join(s1)
  print('s1 reversed:\n')
  print(s1)
  s2=list(s2)
  s2.reverse()
  s2=''.join(s2)
  print('s2 reversed:\n')
  print(s2)
  s3=s1+s2
  print('s3:')
  print(s3)
  s3=''.join(arrays.rotlist(list(s3),self.rot))
  print(ch)
  print(s3)
  self.charmap={}
  self.invmap={}
  for i in range(95):
   self.charmap[ch[i]]=s3[i]
   self.invmap[s3[i]]=ch[i]
 def encrypt(self,s):
  s=list(s)
  n=len(s)
  for i in range(n):
   s[i]=self.charmap[s[i]]
  return ''.join(s)
 def decrypt(self,s):
  s=list(s)
  n=len(s)
  for i in range(n):
   s[i]=self.invmap[s[i]]
  return ''.join(s)

#The following function converts all the elements of a list to integer type

def intize(l):
 n=len(l)
 for i in range(n):
  l[i]=int(l[i])

#The following function converts all elements of a list to string type

def chrize(l):
 n=len(l)
 for i in range(n):
  l[i]=str(l[i])

#Dictionary to map digits to characters upto base 94

dig={}

'''Function to do the process of mapping. Digits 0-9 are mapped to '0'-'9',
   The next 26 digits are mapped to 'A'-'Z', the next 26 to 'a'-'z' and the
   rest are mapped to special characters'''

def init_digits():
 for i in range(0,10):
  dig[i]=str(i)
 for i in range(10,36):
  dig[i]=chr(i+55)
 for i in range(36,62):
  dig[i]=chr(i+61)
 for i in range(62,77):
  dig[i]=chr(i-29)
 for i in range(77,84):
  dig[i]=chr(i-19)
 for i in range(84,90):
  dig[i]=chr(i+7)
 for i in range(90,94):
  dig[i]=chr(i+33)

init_digits()
dig_str=''.join(dig.values())
'''A class describing a characters for the digits of a number system
   and the operations that can be performed on such a character set.
   Data members:
   1. base - A number denoting the base of the number system.
   2. digits - A dictionary mapping each digit to the character denoting it.
   3. invmap - A dictionary which maps characters to the corresponding digits.'''

class dig_set:
 def __init__(self,b=94):
  self.base=b
  
  self.digits={}
  for i in range(self.base):
   self.digits[i]=dig[i]
  self.invmap={}
  r=list(self.digits.values())
  for i in range(self.base):
   self.invmap[self.digits[i]]=i

'''Function to convert a number from base m to n. Default value of n is 10.
   The first argument is the number to be converted. A string with the target
   base is returned.'''
def basem2n ( a , m , n=10 , ):
 dset=dig_set(m)
 if m!=10:
  s=str(a)
  s=list(s)
  length=len(s)
  for i in range(length):
   s[i]=dset.invmap[s[i]]
  s.reverse()
  num=0
  for i in range(length):
   num+=(s[i]*(m**i))
  a=num
  if n==10:
   return str(num)
 res=[]
 if m==10: a=int(a)
 while a!=0:
  res.append(a%n)
  a=(int)(a/n)
 res.reverse()
 length=len(res)
 dset1=dig_set(n)
 for i in range(length):
  res[i]=dset1.digits[res[i]]
 return ''.join(res)
def jumble(s,a,b):
 l=len(s)
 s=list(s)
 s1=s.copy()
 i=0
 while i<l:
  s1[((a*i)+b)%l]=s[i]
  i+=1
 return ''.join(s1)
def jumbleback(s,a,b):
 n=len(s)
 i=0
 s=list(s)
 s1=s.copy()
 while i<n:
  j,k=0,0
  while (j<=((n*a)+b-i)//n):
   if (((n*j)-b+i)%a)==0:
    k=j
    break
   j+=1
  s1[((n*k)+i-b)//a]=s[i]
  i+=1
 return ''.join(s1)

#The following is an All or Nothing transform which
#converts the plaintext from one number system base to another,
#Then jumbles it according to randomly generated keys.
#On computers with accurate calculation power, ths algorithm never fails.
#But due to the presence of large numbers in the calculations, the method fails due to
#the computer's approximations.
def encrypt1(s):
 bs=0
 i=93
 while i>=0:
  if dig_str[i] in s:
   bs=i+1
   break
  i-=1
 if bs<2: bs=2
 print('bs=%d' %(bs))
 t=random.randint(0,1)
 bt=0
 if t==0:
  if bs==2: bt=2
  else:
   bt=random.randint(2,bs-1)
 else:
  if bs==94: bt=94
  else:
   bt=random.randint(bs+1,94)
 print('bt=%d' %(bt))
 bts=basem2n(s,bs,bt)
 print('Converted number=%s' %(bts))
 bs=str(bs) if (bs//10)!=0 else '0'+str(bs)
 bt=str(bt) if (bt//10)!=0 else '0'+str(bt)
 s=bs+bts+bt
 print('s before jumbling=%s' %(s))
 l=len(s)
 rp=number_oper.rel_prime(l)
 a=rp[random.randint(0,len(rp)-1)]
 b=random.randint(1,l-1)
 s=jumble(s,a,b)
 print('s after jumbling=%s' %(s))
 a=str(a) if (a//10)!=0 else '0'+str(a)
 b=str(b) if (b//10)!=0 else '0'+str(b)
 s=a+s+b
 return s
def decrypt1(s):
 a=int(s[0:2])
 b=int(s[-2:])
 s=s[2:-2]
 print('Converted string with bases (jumbled) = %s' %(s))
 s=jumbleback(s,a,b)
 print('Jumbled back = %s' %(s))
 bs=int(s[0:2])
 bt=int(s[-2:])
 s=s[2:-2]
 print('Converted number = %s' %(s))
 s=basem2n(s,bt,bs)
 return s

#Fntip
def add(s,k,nospace=False):
 r=[]
 max=95
 if nospace:
  global chset
  chset=chset[:-1]
  max=94
 l=len(s)
 i=0
 while i<l:
  r.append(chset[(chset.index(s[i])+chset.index(k[i]))%max])
  i+=1
 return ''.join(r)

def sub(s,k,nospace=False):
 l=len(s)
 r=[]
 max=95
 if nospace:
  max=94
  global chset
  chset=chset[:-1]
 i=0
 while i<l:
  si=chset.index(s[i])
  ki=chset.index(k[i])
  if si-ki<0:
   r.append(chset[si-ki+max])
  else:
   r.append(chset[si-ki])
  i+=1
 return ''.join(r)

def genkeyword(n,nospace=False):
 i=0
 r=''
 max=95
 if nospace:
  max=94
  global chset
  chset=chset[:-1]
 while i<n:
  r+=chset[random.randint(1,max-1)]
  i+=1
 return r

def backmix(s1,s2):
 l=len(s1)
 i=0
 r=''
 while i<(2*l):
  if i%2==0:
   r+=s1[i//2]
  else:
   r+=s2[(i-1)//2]
  i+=1
 return r

def sepback(s):
 l=len(s)
 i=0
 s1,s2='',''
 while i<l:
  if i%2==0: s1+=s[i]
  else: s2+=s[i]
  i+=1
 return [s1,s2]

def frontmix(s1,s2):
 l=len(s1)
 i=0
 r=''
 while i<(2*l):
  if i%2==0:
   r+=s2[i//2]
  else:
   r+=s1[(i-1)//2]
  i+=1
 return r

def sepfront(s):
 l=len(s)
 i=0
 s1,s2='',''
 while i<l:
  if i%2==0: s2+=s[i]
  else: s1+=s[i]
  i+=1
 return [s1,s2]

#This is an All or Nothing transform which works as follows:
# 1. Jumble plaintext from randomly generated keys,
# 2. Pack keys with jumbled string in the format <first_key><string><second_key>
# 3. Generate random keyword(k) and add it (as defined by add()) to string obtained in step 2.
# 4. Generate next operation choice from 1-3:
#    Choice 1: Concatenate the string obtained in step 3 with k and append '1' to the string.
#    Choice 2: Call backmix(s,k) and append '2' to the string.
#    Choice 3: Call frontmix(s,k) and append '3' to the string.
def encrypt2(s):
 l=len(s)
 rp=number_oper.rel_prime(l)
 a=rp[random.randint(0,len(rp)-1)]
 b=random.randint(0,l-1)
 s=jumble(s,a,b)
 a,b=str(a),str(b)
 a=(3-len(a))*'0'+a
 b=(3-len(b))*'0'+b
 s=a+s+b
 k=genkeyword(len(s))
 s=add(s,k)
 t=random.randint(1,3)
 if t==1:
  s=s+k+'1'
 elif t==2:
  s=backmix(s,k)
  s+='2'
 else:
  s=frontmix(s,k)
  s+='3'
 return s

def decrypt2(s):
 c=int(s[-1])
 s=s[:-1]
 if c==1:
  l=len(s)
  k=s[l//2:]
  s=s[:l//2]
 elif c==2:
  r=sepback(s)
  s=r[0]
  k=r[1]
 else:
  r=sepfront(s)
  s=r[0]
  k=r[1]
 s=sub(s,k)
 a,b=int(s[:3]),int(s[-3:])
 s=s[3:-3]
 s=jumbleback(s,a,b)
 return s