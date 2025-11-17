n,k,l,c,d,p,nl,np=map(int,input().split())
s=int((k*l)/nl)
t=c*d
q=p/np
a=min(s,t,q)
print(int(a/n))
