import sys

f=open(sys.argv[1], 'r')
index=0
h=open(sys.argv[3], 'w')
s=f.read()
n=len(s)

key=sys.argv[2]
len_key=len(key)

for i in range(0,n,7):
    nr=int(s[i])*64 + int(s[i+1])*32 + int(s[i+2])*16 + int(s[i+3])*8 + int(s[i+4])*4 + int(s[i+5])*2 + int(s[i+6])*1
    nr2=ord(key[index % len_key])
    nr3=nr ^ nr2
    h.write(chr(nr3))
    index+=1

h.close()
f.close()