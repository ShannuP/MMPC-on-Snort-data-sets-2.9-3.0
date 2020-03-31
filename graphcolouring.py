import math
file1= open("runiquefsnort.txt","r")
lb=[]
ub=[]
c=0
for line in file1:
    line=line.rstrip()
    line=line.lstrip()
    line=line.split(':')
    lb.append(line[0])
    ub.append(line[1])
    c=c+1
file1.close()
print(c)
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
print(degree)

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
    f1=open("keys.txt","w")
    key=["" for i in range(2)]
    f2=open("runiquefsnort.txt","r")
    cc=1
    for line in f2:
        line=line.rstrip()
        line=line.lstrip()
        line=line.split(':')
        l=line[0]
        u=line[1] 
        rs=l
        re=l    
        print(cc)
        cc=cc+1
        if int(l)==0:
            continue
        for i in range(int(l),int(u)+1):
            ct=0
            for j in range(len(layer)):
                for k in range(1,len(bitlayer[j]),3):
                    if i>=int(bitlayer[j][k]) and i<=int(bitlayer[j][k+2]):
                        key[1]=key[1]+bitlayer[j][k+1]
                        break
            if int(l)-int(u)==0:
                print(rs,re,key[1],file=f1)
                ct=1
            elif i!=int(l):
                if key[1]==key[0]:
                    re=i
                else:
                    print(rs,re,key[0],file=f1)
                    rs=i
                    re=i
            key[0]=key[1]
            key[1]=""
        if ct!=1:
            print(rs,re,key[0],file=f1)
    f2.close()
    f1.close()
    # print(key)  
    s1=open("keys.txt","r")
    lines = s1.readlines()
    l1 = [i.split(" ")[0] for i in lines]
    l2 = [i.split(" ",1)[1] for i in lines]
    l1 = [int(i) for i in l1]
    arr=[[-1 for i in range(1)]for j in range(c)]
    for i in range(c):
        arr[i].append(l1[i])
        arr[i].append(' ')
        arr[i].append(l2[i])       
    arr.sort(key= lambda arr:arr[1])
    print(*arr)        
    s1.close()
    s2=open("result1.txt","w")
    for i in range(c):
        for j in range(1,4):
            s2.write(str(arr[i][j]))
    s2.close()
    lines_seen = set()
    outfile = open('result2.txt', "w")
    infile = open('result1.txt', "r")
    for line in infile:    
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
idassignment()



