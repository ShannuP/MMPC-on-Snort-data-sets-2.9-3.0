import math
f1=open("newlist2.txt","r")
lb=[]
ub=[]
for line in f1:
    if ":" in line:
        if "[" not in line:
            flag=0
            line=line.split(':')
            for i in range(len(lb)):
                if int(line[0])==lb[i] and int(line[1].rstrip())==ub[i]:
                    flag=1
                    break
            if flag==0:
                lb.append(int(line[0]))
                ub.append(int(line[1].rstrip()))
print(lb,ub)
f1.close()
s1=[]
f3=open("newlist2.txt","r")
for line in f3:
    if ":" not in line:
        if "[" not in line:
            line.rstrip()
            line.lstrip()
            # for i in range(len(lb)):
            #     if int(line)>=lb[i] and int(line)<=ub[i]:
            #         flag=1
            # if flag==0:
            if int(line) not in s1:
                s1.append(int(line))
# print(s1)
f3.close()
print("len=",len(s1),len(lb))
f3=open("newlist2.txt","r")
for line in f3:
    if "[" in line:
        line.rstrip()
        line.lstrip()
        line=line.split("[")[1]
        line=line.split("]")[0]
        line=line.split(",")
        for i in range(len(line)):
            flag1=0
            if ":" in line[i]:
                l1=int(line[i].split(":")[0])
                l2=int(line[i].split(":")[1])
                for j in range(len(lb)):
                    if l1==lb[j] and l2==ub[j]:
                        flag1=1
                        break
                if flag1==0:
                    lb.append(l1)
                    ub.append(l2)
            else:
                x=int(line[i])
                # flag=0
                # for j in range(len(lb)):
                #     if x>=lb[j] and x<=ub[j]:
                #         flag=1
                # if flag==0:
                if x not in s1:
                    s1.append(x)
# print(s1)
for i in range(len(s1)):
    lb.append(s1[i])
    ub.append(s1[i])
print(len(lb),len(ub))
c=len(lb)
f3.close()



result=[-1 for i in range(c)]
degree=[0 for i in range(c)]
adj=[[-1 for i in range(1)]for j in range(c)]
for i in range(c):
    for j in range(c):
        if j==i:
            continue
        lb[i]=int(lb[i])
        ub[i]=int(ub[i])
        lb[j]=int(lb[j])
        ub[j]=int(ub[j])
        if lb[i]<=ub[j] and lb[i]>=lb[j]:
            if j not in adj[i]:
                adj[i].append(j)
                degree[i]+=1
        if ub[i]>=lb[j] and ub[i]<=ub[j]:
            if j not in adj[i]:
                adj[i].append(j)
                degree[i]+=1
        if lb[i]>=lb[j] and ub[i]<=ub[j]:
            if j not in adj[i]:
                adj[i].append(j)
                degree[i]+=1
        if lb[i]<=lb[j] and ub[i]>=ub[j]:
            if j not in adj[i]:
                adj[i].append(j)
                degree[i]+=1

# print(*adj,sep="\n")
# print(degree)

def greedycolouring():
    rn=degree.index(max(degree))
    print(rn)
    result[rn]=0
    available=[1 for i in range(c)]
    for i in range(c):
        for j in range(1,len(adj[i])):
            if result[adj[i][j]]!=-1:
                available[result[adj[i][j]]]=0
        for k in range(c):
            if available[k]==1:
                break
        result[i]=k
        available=[1 for i in range(c)]
    # # for i in range(rn):
    #     for j in range(1,len(adj[i])):
    #         if result[adj[i][j]]!=-1:
    #             available[result[adj[i][j]]]=0
    #     for k in range(c):
    #         if available[k]==1:
    #             break
    #     result[i]=k
    
    print(result)
    
greedycolouring()


def idassignment():
    layer=[[0 for i in range(1)]for j in range(max(result)+1)]
    bitlayer=[["" for j in range(1)]for i in range(max(result)+1)]
    bitlength=[]
    for i in range(len(result)):
        layer[result[i]].append(lb[i])
        layer[result[i]].append(ub[i])
        layer[result[i]].sort()
    # print(layer)
    for i in range(max(result)+1):
        x=result.count(i)+1
        y=math.ceil(math.log(x,2))
        bitlength.append(y)
        k=1
        for j in range(1,len(layer[i]),2):
            if j==1:       
                if layer[i][j]-layer[i][j-1]==0:
                    bit=bin(k)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j])
                    bitlayer[i].append(bit)
                    bitlayer[i].append(layer[i][j+1])
                    k=k+1
                else:
                    bit=bin(0)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j-1])
                    bitlayer[i].append(bit)
                    bitlayer[i].append(layer[i][j]-1)
                    bit=bin(k)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j])
                    bitlayer[i].append(bit)
                    bitlayer[i].append(layer[i][j+1])
                    k=k+1
            else:
                if layer[i][j]-layer[i][j-1]==1:
                    bit=bin(k)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j])
                    bitlayer[i].append(bit)
                    bitlayer[i].append(layer[i][j+1])
                    k=k+1
                else:
                    bit=bin(0)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j-1]+1)
                    bitlayer[i].append(bit)
                    bitlayer[i].append(layer[i][j]-1)
                    bit=bin(k)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j])
                    bitlayer[i].append(bit)
                    bitlayer[i].append(layer[i][j+1])
                    k=k+1

            if j==len(layer[i])-2:
                if layer[i][j+1]!=15:
                    bit=bin(0)[2:].zfill(y)
                    bitlayer[i].append(layer[i][j+1]+1)
                    bitlayer[i].append(bit)
                    bitlayer[i].append(15)
    # print(bitlayer)
    print(bitlength)
idassignment()
# i=0
# while i<c:
#     for j in range(c):
#         if j==i:
#             continue
#         if lb[i]<=ub[j] and lb[i]>=lb[j] and ub[i]>ub[j]:
#             lb[i]=ub[j]+1
#         if lb[i]<=lb[j] and lb[i]>=lb[j] and ub[i]<=ub[j] and ub[i]>=lb[j]:
#             lb.pop(i)
#             ub.pop(i)
#             c=c-1
#             i=i-1
#             break
#         if ub[i]>=lb[j] and ub[i]<=ub[j] and lb[i]<lb[j]:
#             ub[i]=lb[j]-1
#         if ub[i]>=lb[j] and ub[i]<=ub[j] and lb[i]>=lb[j] and lb[i]<=ub[j]:
#             lb.pop(i)
#             ub.pop(i)
#             c=c-1
#             i=i-1
#             break
#     i=i+1
# print(lb,ub)




        

