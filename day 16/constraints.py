val=[1,2,3,4,5,6,7,8,9]
def is_valid(a,b,c,d,e,f,g,h,i):
    if a==b:
        return False
    if b == c:
        return False
    if c==d:
        return False
    if d==e:
        return False
    if e==f:
        return False
    if f==g:
        return False
    if g==h:
        return False
    if h==i:
        return False
    if i==a:
        return False
    return True
for a in val:
    for b in val:
        for c in val:
            for d in val:
                for e in val:
                    for f in val:
                        for g in val:
                            for h in val:
                                for i in val:
                                    def is_safe(a,b,c,d,e,f,g,h,i):
                                        print([(a,b,c,d,e,f,g,h,i)])