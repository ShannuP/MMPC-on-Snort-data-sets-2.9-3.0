import math
import itertools 
from itertools import combinations, chain 

f1=open("3.0sport","r")
lbb1=[]
ubb1=[]
for line in f1:
    line=line.split(":")
    lbb1.append(int(line[0].lstrip()))
    ubb1.append(int(line[1].rstrip()))
f1.close()

f1=open("3.0dport","r")
lbb2=[]
ubb2=[]
for line in f1:
    line=line.split(":")
    lbb2.append(int(line[0].lstrip()))
    ubb2.append(int(line[1].rstrip()))
f1.close()

f1=open("3.0sadd2","r")
lbb3=[]
ubb3=[]
for line in f1:
    line=line.split(":")
    lbb3.append(int(line[0].lstrip()))
    ubb3.append(int(line[1].rstrip()))
f1.close()

f1=open("3.0dadd2","r")
lbb4=[]
ubb4=[]
for line in f1:
    line=line.split(":")
    lbb4.append(int(line[0].lstrip()))
    ubb4.append(int(line[1].rstrip()))
f1.close()

f1=open("3.0prot","r")
lbb5=[]
ubb5=[]
for line in f1:
    line=line.split(":")
    lbb5.append(int(line[0].lstrip()))
    ubb5.append(int(line[1].rstrip()))
f1.close()


def seperation(*w1):
    ln1=[]
    lb1=w1[0]
    ub1=w1[1]
    for i in range(len(lb1)):
        ln1.append(lb1[i])
        ln1.append(ub1[i])
    ln1.sort()
    res1 = [] 
    for i in ln1: 
        if i not in res1: 
            res1.append(i) 
    # print(res1)
    # print(lb1)
    # print(ub1)
    s1=[[-1 for i in range(1)]for j in range(2*len(res1))]
    s2=[]
    c=0
    i=0
    while i<(len(res1)-1):
        k=1
        k1=1
        if res1[i+1] in lb1 and res1[i+1] in ub1:
            if lb1.index(res1[i+1])==ub1.index(res1[i+1]):
                k1=0
            if res1[i] in lb1 and res1[i] in ub1:
                # if lb1.index(res1[i])==ub1.index(res1[i]):
                k=0
            if k==1:         
                if res1[i] in lb1:
                    s1[c].extend((res1[i],res1[i+1]-1))
                    for j in range(len(lb1)):
                        if res1[i+1]-1>=lb1[j] and res1[i+1]-1<=ub1[j]:
                            s1[c].append(j+1)
                else:
                    s1[c].extend((res1[i]+1,res1[i+1]-1))
                    for j in range(len(lb1)):
                        if res1[i+1]-1>=lb1[j] and res1[i+1]-1<=ub1[j]:
                            s1[c].append(j+1)
                if c>0:
                    if s1[c-1][1]!=s1[c][1] and s1[c-1][2]!=s1[c][2]:
                        s2.append(s1[c][1:])
                        c=c+1
                    else:
                        c=c+1
                else:
                    s2.append(s1[c][1:])
                    c=c+1
            elif k1==1:         
                if res1[i] in lb1:
                    s1[c].extend((res1[i]+1,res1[i+1]-1))
                    for j in range(len(lb1)):
                        if res1[i+1]-1>=lb1[j] and res1[i+1]-1<=ub1[j]:
                            s1[c].append(j+1)
                else:

                    s1[c].extend((res1[i]+1,res1[i+1]-1))
                    for j in range(len(lb1)):
                        if res1[i+1]-1>=lb1[j] and res1[i+1]-1<=ub1[j]:
                            s1[c].append(j+1)
                if c>0:
                    if s1[c-1][1]!=s1[c][1] and s1[c-1][2]!=s1[c][2]:
                        s2.append(s1[c][1:])
                        c=c+1
                    else:
                        c=c+1
                else:
                    s2.append(s1[c][1:])
                    c=c+1


            s1[c].extend((res1[i+1],res1[i+1]))
            for j in range(len(lb1)):
                if res1[i+1]>=lb1[j] and res1[i+1]<=ub1[j]:
                    s1[c].append(j+1)
            s2.append(s1[c][1:])
            c=c+1
            if i+2<len(res1):
                if res1[i+2] in lb1 and res1[i+2] in ub1:
                    if res1[i+2]-res1[i+1]>1:
                        s1[c].extend((res1[i+1]+1,res1[i+2]-1))
                        for j in range(len(lb1)):
                            if res1[i+2]-1>=lb1[j] and res1[i+2]-1<=ub1[j]:
                                s1[c].append(j+1)
                        if c>0:
                            if s1[c-1][1]!=s1[c][1] and s1[c-1][2]!=s1[c][2]:
                                s2.append(s1[c][1:])
                                c=c+1
                            else:
                                c=c+1
                        else:
                            s2.append(s1[c][1:])
                            c=c+1
                    # if ub1.index(res1[i+2])==lb1.index(res1[i+2]):
                    i=i+1
                    continue  
                if res1[i+2] in lb1:
                    s1[c].extend((res1[i+1]+1,res1[i+2]-1))
                    for j in range(len(lb1)):
                        if res1[i+2]-1>=lb1[j] and res1[i+2]-1<=ub1[j]:
                            s1[c].append(j+1)
                else:
                    s1[c].extend((res1[i+1]+1,res1[i+2]))
                    for j in range(len(lb1)):
                        if res1[i+2]>=lb1[j] and res1[i+2]<=ub1[j]:
                            s1[c].append(j+1)
                i=i+1
        elif res1[i] in lb1 and res1[i+1] in ub1:
            s1[c].extend((res1[i],res1[i+1]))
            for j in range(len(lb1)):
                if res1[i+1]>=lb1[j] and res1[i+1]<=ub1[j]:
                    s1[c].append(j+1)
        elif res1[i] not in lb1 and res1[i+1] in ub1:
            s1[c].extend((res1[i]+1,res1[i+1]))
            for j in range(len(lb1)):
                if (res1[i+1])>=lb1[j] and (res1[i+1])<=ub1[j]:
                    s1[c].append(j+1)
        elif res1[i] in lb1 and res1[i+1] not in ub1:
            s1[c].extend((res1[i],res1[i+1]-1))
            for j in range(len(lb1)):
                if (res1[i+1]-1)>=lb1[j] and (res1[i+1]-1)<=ub1[j]:
                    s1[c].append(j+1)
        elif res1[i] not in lb1 and res1[i+1] not in ub1:
            s1[c].extend((res1[i]+1,res1[i+1]-1))
            for j in range(len(lb1)):
                if (res1[i+1]-1)>=lb1[j] and (res1[i+1]-1)<=ub1[j]:
                    s1[c].append(j+1)
        s2.append(s1[c][1:])
        c=c+1
        i=i+1

    # print(*s2,sep="\n")
    return s2

r1=seperation(lbb1,ubb1)
r2=seperation(lbb2,ubb2)
r3=seperation(lbb3,ubb3)
r4=seperation(lbb4,ubb4)
r5=seperation(lbb5,ubb5)
print(*r1,sep="\n")
print("-------------------------------------")
print(*r2,sep="\n")
print("-------------------------------------")
print(*r3,sep="\n")
print("-------------------------------------")
print(*r4,sep="\n")
print("-------------------------------------")
print(*r5,sep="\n")
print("-------------------------------------")
print("r1=",len(r1))
print("r2=",len(r2))
print("r3=",len(r3))
print("r4=",len(r4))
print("r5=",len(r5))
# print("hai",len(r1))
# c=0
# seen=[]
# sm=[]
# for i in range(len(r1)-1):
#     for j in range(i+1,len(r1)):
#         if i not in seen:
#             if r1[i][2:]==r1[j][2:]:
#                 c=c+1
#                 seen.append(j)
#                 s=(i,j)
#                 sm.append(list(s))
# print("c=",c) 
# print(sm)
# e1=[]
# for i in range(len(r1)):
#     print(r1[i][0:2])
# for i in range(len(r1[1])):
#     if r1[1][i] not in r1[0]:
#         e1.append(r1[1][i])
# print("e1=",e1)

# def findsubsets(s, n): 
# 	return list(map(tuple, itertools.combinations(s, n))) 
# y=[]
# y2=[]
# y3=[]
# for i in range(len(r1)):
#     print(i)
#     print(len(r1[i]))
#     y2=[]
#     if len(r1[i])>=4:
#         for j in range(2,len(r1[i])-1):
#             x=findsubsets(r1[i][2:],j)
#             y2=y2+x
#             print("+++",j)
#         print("----",i)
#         y3=y3+list(set(y2)-set(y3))
# y1=[]
# for i in range(len(y3)):
#     x=list(y3[i])
#     y1.append(x)
            # print(x[k])
# print(*y1,sep="\n")
# print("haiiii",y1[0],y1[0][1])
# y2=[]
# for i in range(len(r2)):
#     if len(r2[i])>=4:
#         for j in range(2,len(r2[i])-1):
#             x=findsubsets(r2[i][2:],j)
#             for k in range(len(x)):
#                 if x[k] not in y2:
#                     y2.append(x[k])

# for i in range(len(y1)):
#     if y1[i] in y2:
#         y.append(y1[i])

# print(lbb2)
# print(ubb2)
# order1=[[-1 for i in range(1)] for j in range(len(y1)*2)]
# order1=[]
# def common(*p1):
#     l1=p1[0]
#     l2=p1[1]
#     if ubb2[l1]<=ubb2[l2] and ubb2[l1]>=lbb2[l2] and lbb2[l1]<lbb2[l2]:
#         return 1
#     elif lbb2[l1]>=lbb2[l2] and lbb2[l1]<=ubb2[l2] and ubb2[l1]>ubb2[l2]:
#         return 1
#     elif ubb2[l1]<=ubb2[l2] and ubb2[l1]>=lbb2[l2] and lbb2[l1]>=lbb2[l2]:
#         order1.append([l1+1,l2+1])
#         return 1
#     elif lbb2[l1]<lbb2[l2] and ubb2[l1]>ubb2[l2]:
#         order1.append([l2+1,l1+1])
#         return 1
#     else:
#         return 0


# for i in range(len(y1)):
#     k=1
#     k2=1
#     j1=len(y1[i])
#     print(i,j1)
#     for j2 in range(j1-1):
#         for j3 in range(j2+1,j1):
#         # print(y1[i][j],y1[i][j+1])
#             k=common(y1[i][j2]-1,y1[i][j3]-1)
#             if k==0:
#                 k2=0
#                 break
#         if k2==0:
#             break
#     if k==1:
#         y.append(y1[i])
#         print(y1[i])


# print(*y,sep="\n")
# order2=[]
# for i in range(len(order1)):
#     if order1[i] not in order2:
#         order2.append(order1[i])


# print(order2)
itcs=[]
cs2=[]
cs3=[]
cs4=[]
for i in range(len(r1)):
    print(i)
    for k in range(len(r5)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r5[k][2:]:
                s1.append(r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    print(i)
    for k in range(len(r4)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r4[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    print(i)
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    print(i)
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in cs4:
                cs4.append(s4)          
    
print("no.of intersections4=",len(cs4))


f1=open("2.9SSA-INP","w")
for i in range(len(cs4)):
    f1.write(str(cs4[i]))
    f1.write("\n")
max1=0
for i in range(len(cs4)):
    for j in range(len(cs4[i])):
        if len(cs4[i])>max1:
            max1=len(cs4[i])
            id1=i
max_intersections=cs4[id1]
print("maximum intersections=",len(max_intersections))
print(max_intersections)

f1.close()
wf1=open("3.0_GI_intrules.txt","w")
saddlb=[]
saddub=[]
daddlb=[]
daddub=[]
sportlb=[]
sportub=[]
dportlb=[]
dportub=[]
protlb=[]
protub=[]
for i in range(len(cs4)):
    mnsp=0
    mndp=0
    mnsa=0
    mnda=0
    mnpt=0
    mxsp=65535
    mxdp=65535
    mxsa=math.pow(2,32)
    mxda=math.pow(2,32)
    mxpt=255
    for j in range(len(cs4[i])):
        if lbb1[cs4[i][j]-1]>mnsp:
            mnsp=lbb1[cs4[i][j]-1]
        if ubb1[cs4[i][j]-1]<mxsp:
            mxsp=ubb1[cs4[i][j]-1]

        if lbb2[cs4[i][j]-1]>mndp:
            mndp=lbb2[cs4[i][j]-1]
        if ubb2[cs4[i][j]-1]<mxdp:
            mxdp=ubb2[cs4[i][j]-1]

        if lbb3[cs4[i][j]-1]>mnsa:
            mnsa=lbb3[cs4[i][j]-1]
        if ubb3[cs4[i][j]-1]<mxsa:
            mxsa=ubb3[cs4[i][j]-1]

        if lbb4[cs4[i][j]-1]>mnda:
            mnda=lbb4[cs4[i][j]-1]
        if ubb4[cs4[i][j]-1]<mxda:
            mxda=ubb4[cs4[i][j]-1]

        if lbb5[cs4[i][j]-1]>mnpt:
            mnpt=lbb5[cs4[i][j]-1]
        if ubb5[cs4[i][j]-1]<mxpt:
            mxpt=ubb5[cs4[i][j]-1]
    wf1.write(str(mnsa)+":"+str(mxsa)+" "+str(mnda)+":"+str(mxda)+" "+str(mnsp)+":"+str(mxsp)+" "+str(mndp)+":"+str(mxdp)+" "+str(mnpt)+":"+str(mxpt)+"\n")
wf1.close()        

def change11():
    ct1=0
    ct2=0
    for i in range(len(val)):
        if val[i]==1:
            ct1=ct1+1
        elif val[i]==2:
            ct2=ct2+1
    if ct1>ct2:
        return 2
    else:
        return 1
c1=list(cs4)
c2=list(c1)
fil=[]
for i in range(len(c1)):
    for j in range(len(c1[i])):
        if c1[i][j] not in fil:
            fil.append(c1[i][j])
print("No.of filters=",len(fil))
fil.sort()
val=[0 for i in range(len(fil))]
w1=[0 for i in range(len(c1))]
for i in range(len(c1)):
    w1[i]=math.pow(2,-len(c1[i]))
w2=list(w1)
ff1=[1 for i in range(len(c1))]
ff2=[1 for i in range(len(c2))]

for i in range(len(fil)):
    if i==4 or i==40 or i==119 or i==430:
        continue
    # if(i%50==0):
    #     print(i)
    v1=1
    v2=1
    l1=[]
    l2=[]
    for j in range(len(c1)):
        if fil[i] in c1[j]:
            if ff1[j]==1:
                v1=v1*w1[j]
                l1.append(j)
        if fil[i] in c2[j]:
            if ff2[j]==1:
                v2=v2*w2[j]
                l2.append(j)
    if v1==1:
        v1=math.pow(2,-50)
    if v2==1:
        v2=math.pow(2,-50)
    if v1==v2:
        flag=change11()
        if flag==1:
            val[i]=1
            for k in range(len(l1)):
                ff1[l1[k]]=0
            for k in range(len(l2)):
                w2[l2[k]]=w2[l2[k]]*2
        else:
            val[i]=2
            for k in range(len(l2)):
                ff2[l2[k]]=0
            for k in range(len(l1)):
                w1[l1[k]]=w1[l1[k]]*2

    elif v1>v2:
        val[i]=1
        for k in range(len(l1)):
            ff1[l1[k]]=0
        for k in range(len(l2)):
            w2[l2[k]]=w2[l2[k]]*2
    else:
        val[i]=2
        for k in range(len(l2)):
            ff2[l2[k]]=0
        for k in range(len(l1)):
            w1[l1[k]]=w1[l1[k]]*2
print("-------------")
# print(val)
val22=[]
val21=[]
t1l1=[]
t1u1=[]
t1l2=[]
t1u2=[]
t1l3=[]
t1u3=[]
t1l4=[]
t1u4=[]
t1l5=[]
t1u5=[]
t2l1=[]
t2u1=[]
t2l2=[]
t2u2=[]
t2l3=[]
t2u3=[]
t2l4=[]
t2u4=[]
t2l5=[]
t2u5=[]

for i in range(len(val)):
    if val[i]==1 or i==4 or i==40 or i==119 or i==430:
        t1l1.append(lbb1[i])
        t1u1.append(ubb1[i])
        t1l2.append(lbb2[i])
        t1u2.append(ubb2[i])
        t1l3.append(lbb3[i])
        t1u3.append(ubb3[i])
        t1l4.append(lbb4[i])
        t1u4.append(ubb4[i])
        t1l5.append(lbb5[i])
        t1u5.append(ubb5[i])
        val21.append(i)
    else:
        t2l1.append(lbb1[i])
        t2u1.append(ubb1[i])
        t2l2.append(lbb2[i])
        t2u2.append(ubb2[i])
        t2l3.append(lbb3[i])
        t2u3.append(ubb3[i])
        t2l4.append(lbb4[i])
        t2u4.append(ubb4[i])
        t2l5.append(lbb5[i])
        t2u5.append(ubb5[i])
        val22.append(i)

print('len of t1=',len(t1l1))
print("len 0f t2=",len(t2l1))
print("FOR TCAM-1:")
r1=seperation(t1l1,t1u1)
r2=seperation(t1l2,t1u2)
r3=seperation(t1l3,t1u3)
r4=seperation(t1l4,t1u4)
r5=seperation(t1l5,t1u5)  


itcs=[]
cs2=[]
cs3=[]
cs4=[]
for i in range(len(r1)):
    for k in range(len(r5)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r5[k][2:]:
                s1.append(r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    for k in range(len(r4)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r4[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in cs4:
                cs4.append(s4)          
    
print("no.of intersections4=",len(cs4))


print("FOR TCAM-2:")

r1=seperation(t2l1,t2u1)
r2=seperation(t2l2,t2u2)
r3=seperation(t2l3,t2u3)
r4=seperation(t2l4,t2u4)
r5=seperation(t2l5,t2u5)  


itcs=[]
cs2=[]
cs3=[]
css4=[]
for i in range(len(r1)):
    for k in range(len(r5)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r5[k][2:]:
                s1.append(r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    for k in range(len(r4)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r4[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in css4:
                css4.append(s4)          
    
print("no.of intersections4=",len(css4))

print("-----------------------")
print("SSA on TCAM-1:")

c1=list(cs4)
c2=list(c1)
fil=[]
# for i in range(len(css4)):
#     for j in range(len(css4[i])):
#         if css4[i][j] not in fil:
#             fil.append(css4[i][j])
fil=list(val21)
print("No.of filters=",len(fil))
fil.sort()
val=[0 for i in range(len(fil))]
w1=[0 for i in range(len(c1))]
for i in range(len(c1)):
    w1[i]=math.pow(2,-len(c1[i]))
w2=list(w1)
ff1=[1 for i in range(len(c1))]
ff2=[1 for i in range(len(c2))]

for i in range(len(fil)):
    if i==4 or i==40 or i==119 or i==430:
        continue
    # if(i%50==0):
    #     print(i)
    v1=1
    v2=1
    l1=[]
    l2=[]
    for j in range(len(c1)):
        if fil[i] in c1[j]:
            if ff1[j]==1:
                v1=v1*w1[j]
                l1.append(j)
        if fil[i] in c2[j]:
            if ff2[j]==1:
                v2=v2*w2[j]
                l2.append(j)
    if v1==1:
        v1=math.pow(2,-50)
    if v2==1:
        v2=math.pow(2,-50)
    if v1==v2:
        flag=change11()
        if flag==1:
            val[i]=1
            for k in range(len(l1)):
                ff1[l1[k]]=0
            for k in range(len(l2)):
                w2[l2[k]]=w2[l2[k]]*2
        else:
            val[i]=2
            for k in range(len(l2)):
                ff2[l2[k]]=0
            for k in range(len(l1)):
                w1[l1[k]]=w1[l1[k]]*2

    elif v1>v2:
        val[i]=1
        for k in range(len(l1)):
            ff1[l1[k]]=0
        for k in range(len(l2)):
            w2[l2[k]]=w2[l2[k]]*2
    else:
        val[i]=2
        for k in range(len(l2)):
            ff2[l2[k]]=0
        for k in range(len(l1)):
            w1[l1[k]]=w1[l1[k]]*2
print("-------------")
# print(val)
t1l1=[]
t1u1=[]
t1l2=[]
t1u2=[]
t1l3=[]
t1u3=[]
t1l4=[]
t1u4=[]
t1l5=[]
t1u5=[]
t2l1=[]
t2u1=[]
t2l2=[]
t2u2=[]
t2l3=[]
t2u3=[]
t2l4=[]
t2u4=[]
t2l5=[]
t2u5=[]

for i in range(len(val)):
    if val[i]==1 or fil[i]==4 or fil[i]==40 or fil[i]==119 or fil[i]==430:
        t1l1.append(lbb1[fil[i]])
        t1u1.append(ubb1[fil[i]])
        t1l2.append(lbb2[fil[i]])
        t1u2.append(ubb2[fil[i]])
        t1l3.append(lbb3[fil[i]])
        t1u3.append(ubb3[fil[i]])
        t1l4.append(lbb4[fil[i]])
        t1u4.append(ubb4[fil[i]])
        t1l5.append(lbb5[fil[i]])
        t1u5.append(ubb5[fil[i]])
    else:
        t2l1.append(lbb1[fil[i]])
        t2u1.append(ubb1[fil[i]])
        t2l2.append(lbb2[fil[i]])
        t2u2.append(ubb2[fil[i]])
        t2l3.append(lbb3[fil[i]])
        t2u3.append(ubb3[fil[i]])
        t2l4.append(lbb4[fil[i]])
        t2u4.append(ubb4[fil[i]])
        t2l5.append(lbb5[fil[i]])
        t2u5.append(ubb5[fil[i]])

print('len of t11=',len(t1l1))
print("len 0f t12=",len(t2l1))
print("FOR TCAM-1-1:")
r1=seperation(t1l1,t1u1)
r2=seperation(t1l2,t1u2)
r3=seperation(t1l3,t1u3)
r4=seperation(t1l4,t1u4)
r5=seperation(t1l5,t1u5)  


itcs=[]
cs2=[]
cs3=[]
cs4=[]
for i in range(len(r1)):
    for k in range(len(r5)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r5[k][2:]:
                s1.append(r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    for k in range(len(r4)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r4[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in cs4:
                cs4.append(s4)          
    
print("no.of intersections4=",len(cs4))

print("FOR TCAM-1-2:")

print('len of t2l1=',len(t2l1))
print('len of t2l5=',len(t2l5))


r1=seperation(t2l1,t2u1)
r2=seperation(t2l2,t2u2)
r3=seperation(t2l3,t2u3)
r4=seperation(t2l4,t2u4)
r5=seperation(t2l5,t2u5)  
print('len of r1=',len(r1))
print('len of r4=',len(r4))
print(r5)

itcs=[]
cs2=[]
cs3=[]
ccs4=[]
for i in range(len(r1)):
    for k in range(len(r4)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r4[k][2:]:
                s1.append(r1[i][j])
                print("j=",j," appenden=",r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)
                print("k=",k," appenden=",r1[i][j])

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    for k in range(len(r5)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r5[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in ccs4:
                ccs4.append(s4)          
    
print("no.of intersections4=",len(ccs4))

print("------------------------")
print("SSA on TCAM-2:")

c1=list(css4)
c2=list(c1)
fil=[]
# for i in range(len(c1)):
#     for j in range(len(c1[i])):
#         if c1[i][j] not in fil:
#             fil.append(c1[i][j])
fil=list(val22)
print("No.of filters=",len(fil))
fil.sort()
val=[0 for i in range(len(fil))]
w1=[0 for i in range(len(c1))]
for i in range(len(c1)):
    w1[i]=math.pow(2,-len(c1[i]))
w2=list(w1)
ff1=[1 for i in range(len(c1))]
ff2=[1 for i in range(len(c2))]

for i in range(len(fil)):
    if i==4 or i==40 or i==119 or i==430:
        continue
    # if(i%50==0):
    #     print(i)
    v1=1
    v2=1
    l1=[]
    l2=[]
    for j in range(len(c1)):
        if fil[i] in c1[j]:
            if ff1[j]==1:
                v1=v1*w1[j]
                l1.append(j)
        if fil[i] in c2[j]:
            if ff2[j]==1:
                v2=v2*w2[j]
                l2.append(j)
    if v1==1:
        v1=math.pow(2,-50)
    if v2==1:
        v2=math.pow(2,-50)
    if v1==v2:
        flag=change11()
        if flag==1:
            val[i]=1
            for k in range(len(l1)):
                ff1[l1[k]]=0
            for k in range(len(l2)):
                w2[l2[k]]=w2[l2[k]]*2
        else:
            val[i]=2
            for k in range(len(l2)):
                ff2[l2[k]]=0
            for k in range(len(l1)):
                w1[l1[k]]=w1[l1[k]]*2

    elif v1>v2:
        val[i]=1
        for k in range(len(l1)):
            ff1[l1[k]]=0
        for k in range(len(l2)):
            w2[l2[k]]=w2[l2[k]]*2
    else:
        val[i]=2
        for k in range(len(l2)):
            ff2[l2[k]]=0
        for k in range(len(l1)):
            w1[l1[k]]=w1[l1[k]]*2
print("-------------")
# print(val)
t1l1=[]
t1u1=[]
t1l2=[]
t1u2=[]
t1l3=[]
t1u3=[]
t1l4=[]
t1u4=[]
t1l5=[]
t1u5=[]
t2l1=[]
t2u1=[]
t2l2=[]
t2u2=[]
t2l3=[]
t2u3=[]
t2l4=[]
t2u4=[]
t2l5=[]
t2u5=[]

for i in range(len(val)):
    if val[i]==1 or i==4 or i==40 or i==119 or i==430:
        t1l1.append(lbb1[fil[i]])
        t1u1.append(ubb1[fil[i]])
        t1l2.append(lbb2[fil[i]])
        t1u2.append(ubb2[fil[i]])
        t1l3.append(lbb3[fil[i]])
        t1u3.append(ubb3[fil[i]])
        t1l4.append(lbb4[fil[i]])
        t1u4.append(ubb4[fil[i]])
        t1l5.append(lbb5[fil[i]])
        t1u5.append(ubb5[fil[i]])
    else:
        t2l1.append(lbb1[fil[i]])
        t2u1.append(ubb1[fil[i]])
        t2l2.append(lbb2[fil[i]])
        t2u2.append(ubb2[fil[i]])
        t2l3.append(lbb3[fil[i]])
        t2u3.append(ubb3[fil[i]])
        t2l4.append(lbb4[fil[i]])
        t2u4.append(ubb4[fil[i]])
        t2l5.append(lbb5[fil[i]])
        t2u5.append(ubb5[fil[i]])

print('len of t21=',len(t1l1))
print("len 0f t22=",len(t2l1))
print("FOR TCAM-2-1:")
r1=seperation(t1l1,t1u1)
r2=seperation(t1l2,t1u2)
r3=seperation(t1l3,t1u3)
r4=seperation(t1l4,t1u4)
r5=seperation(t1l5,t1u5)  


itcs=[]
cs2=[]
cs3=[]
cs41=[]
for i in range(len(r1)):
    for k in range(len(r5)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r5[k][2:]:
                s1.append(r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    for k in range(len(r4)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r4[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in cs41:
                cs41.append(s4)          
     
print("no.of intersections4=",len(cs41))

print("FOR TCAM-2-2:")

r1=seperation(t2l1,t2u1)
r2=seperation(t2l2,t2u2)
r3=seperation(t2l3,t2u3)
r4=seperation(t2l4,t2u4)
r5=seperation(t2l5,t2u5)  


itcs=[]
cs2=[]
cs3=[]
cs42=[]
for i in range(len(r1)):
    for k in range(len(r5)):
        s1=[]
        for j in range(2,len(r1[i])):
            if r1[i][j] in r5[k][2:]:
                s1.append(r1[i][j])
        if len(s1)>1:
            if s1 not in itcs:
                itcs.append(s1)

print("no.of intersections1=",len(itcs))
# print(*itcs,sep="\n")

for i in range(len(itcs)):
    for k in range(len(r4)):
        s2=[]
        for j in range(len(itcs[i])):
            if itcs[i][j] in r4[k][2:]:
               s2.append(itcs[i][j])
        if len(s2)>1:
            if s2 not in cs2:
                cs2.append(s2)
               
print("no.of intersections2=",len(cs2))

for i in range(len(cs2)):
    for k in range(len(r3)):
        s3=[]
        for j in range(len(cs2[i])):
            if cs2[i][j] in r3[k][2:]:
               s3.append(cs2[i][j])
        if len(s3)>1:
            if s3 not in cs3:
                cs3.append(s3)          
    
print("no.of intersections3=",len(cs3))

for i in range(len(cs3)):
    for k in range(len(r2)):
        s4=[]
        for j in range(len(cs3[i])):
            if cs3[i][j] in r2[k][2:]:
               s4.append(cs3[i][j])
        if len(s4)>1:
            if s4 not in cs42:
                cs42.append(s4)          
    
print("no.of intersections4=",len(cs42))