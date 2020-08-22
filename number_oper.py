def pow(a,b):
 p=1
 for i in range(b):
  p=p*a
 return p
def hcf(a,b):
 if a<b:
  temp=a
  a=b
  b=temp
 if a%b==0: return b
 else: return hcf(b,a%b)
def lcm(a,b):
 return (a*b)/hcf(a,b)
def fact(a):
 if a==0: return 1
 elif a==1: return a
 else: return a*fact(a-1)
def isprime(n):
 if n==0:
  return False
 elif n==1:
  return None
 elif n==2:
  return True
 elif n%2==0:
  return False
 else:
  for i in range(3,int(n/2)):
   if n%i==0: return False
  return True
def totient(n):
 c=0
 for i in range(1,n+1):
  if hcf(n,i)==1:
   c+=1
 return c
def prime_fact(n):
 t=isprime(n)
 if t==None:
  return {1:1}
 elif t:
  return {n:1}
 else:
  res={}
  for i in range(2,n):
   temp=n
   c=0
   while temp%i==0 and isprime(i):
    temp/=i 
    c+=1
   if c!=0:
    res[i]=c
  return res
def divisors(n):
 res=[]
 for i in range(2,n):
  if n%i==0:
   res.append(i)
 return res
def rel_prime(n):
 res=[]
 for i in range(1,n+1):
  if hcf(n,i)==1:
   res.append(i)
 return res