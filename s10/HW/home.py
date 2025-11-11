def make_list():
    b=[]
    return b

def mosalas(n):
    a=[1]
    b=[1,1]
    c=b
    print(a)
    print(b)
    for _ in range(n):
        l=make_list()
        l.append(1)
        for i in range(len(c)-1):
            l.append(c[i]+c[i+1])
        l.append(1)
        print(l)
        c=l

mosalas(5)