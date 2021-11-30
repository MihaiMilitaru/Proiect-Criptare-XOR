import sys

def binr(x):
    sir=[0,0,0,0,0,0,0]
    index=0
    while x:
        r=x%2
        c=x//2
        sir[index]=r
        index+=1
        x=x//2
    sir.reverse()
    return sir


key=sys.argv[1]
f=open(sys.argv[2], 'r')
g=open(sys.argv[3], 'w')

len_key=len(key)

s=f.read()

for i in range(len(s)):
    ls=binr(ord(s[i]) ^ ord(key[i%len_key]))
    for x in ls:
        g.write(str(x))

g.close()
f.close()