# file1 = open ("dataset4.txt", "r") 
# file2 = open ("rawf1.txt", "w")
f_out1 = open ("acl_sadd2","w")
file3 = open ("rawf2.txt", "w")
f_out2 = open ("rangef2.txt","w")
file4= open ("rawf3.txt", "w")
f_out3 = open ("rangef3.txt","w")
file5 = open ("rawf4.txt", "w")
f_out4 = open ("rangef4.txt","w")
file6 =open("rawf5.txt","w")
f_out5=open("rangef5.txt","w")
# for line in file1:        #extracting fields from file1 into individual files 
#       line = line.split()
#       file2.write(line[0]+"\n")
#       file3.write(line[1]+"\n")
#       file4.write(line[2]+line[3]+line[4]+"\n")
#       file5.write(line[5]+line[6]+line[7]+"\n")
#       file6.write(line[8]+"\n")
# file2.close()
file2 = open("acl_sadd", "r")
for s in file2:   # converting field1 into ranges
	f=str(s)
	# f=f.split('@')[1]
	d1 = f.index("/")
	#print d1
	s1 = f[:d1]
	s2 = f[d1+1:]
	#print s1
	#print s2
	n = int (s2)
	list = s1.split(".")
	r = " "
	for i in list:
		m = int (i)
		r = r +'{:08b}'.format(m)
	#print r	
	r1 = r[0 : n+1]
	#print r1
	x = 32 - n
	#print x
	res1 = r1
	res2 = r1
	for i in range(x):
		res1 = res1 + "0"
	#print res1
	for i in range(x):
		res2 = res2 + "1"
	#print res2
	w1 = int (res1,2)
	w2 = int(res2,2)
	w = str(w1) + ":" + str(w2)
	f_out1.write(w + "\n")
f_out1.close()
# f_out1 = open ("rangef1.txt","r")
# o = set()     #inorder to get unique values we use set( ) function 
# with open('rangef1.txt','r') as infile1:         
#     with open('new_sadd2', 'w') as outfile1:
#         for line in infile1:
#             if line not in o :
#                 outfile1.write(line)
#                 o.add(line)
file3.close()
file3 = open("rawf2.txt", "r") 
for t in file3:  #converting  field2 into ranges
	f=str(t)
	d1 = f.index("/")
	#print d1
	s1 = f[:d1]
	s2 = f[d1+1:]
	#print s1
	#print s2
	n = int (s2)
	list = s1.split(".")
	r = " "
	for i in list:
		m = int (i)
		r = r +'{:08b}'.format(m)
	#print r	
	r1 = r[0 : n+1]
	#print r1
	x = 32 - n
	#print x
	res1 = r1
	res2 = r1
	for i in range(x):
		res1 = res1 + "0"
	#print res1
	for i in range(x):
		res2 = res2 + "1"
	#print res2
	w1 = int (res1,2)
	w2 = int(res2,2)
	w = str(w1) + ":" + str(w2)
	f_out2.write(w + "\n")
	#print w1,":",w2	
f_out2.close()
f_out2 = open ("rangef2.txt","r")
a= set() # converting ranges  to unique ranges
with open('rangef2.txt','r') as infile2:
    with open('runiquef2.txt', 'w') as outfile2:
        for line in infile2:
            if line not in a:
                outfile2.write(line)
                a.add(line)
file4.close()
file4=open("rawf3.txt","r")
b=set()  # converting ranges  to unique ranges
with open('rawf3.txt','r') as infile3:
    with open('runiquef3.txt', 'w') as outfile3:
        for line in infile3:
            if line not in b:
                outfile3.write(line)
                b.add(line)
file5.close()
file5=open("rawf4.txt","r")
c=set()  # converting ranges  to unique ranges
with open('rawf4.txt','r') as infile4:
    with open('runiquef4.txt', 'w') as outfile4:
        for line in infile4:
            if line not in c:
                outfile4.write(line)
                c.add(line)              
file6.close()
file6 = open("rawf5.txt", "r")
for s in file6:
	f=str(s)
	d1 = f.index("/")
	s1 = f[:d1]
	s2 = f[d1+1:]
	w1=int(s1,16)
	w2=int(s2,16)
	n=int(w2)
	n1 =int(w1)
	res1=""
	res2=""
	if(n1==0):
		for i in range(8):
			res1=res1+'0'
		for i in range(8):
			res2=res2+'1'
		l1=int(res1,2)
		l2=int(res2,2)
		f_out5.write(str(l1)+":"+str(l2)+"\n")
	else:
		f_out5.write(str(w1)+":"+str(w1)+"\n")
f_out5.close()
f_out5 = open ("rangef5.txt","r")
y= set() # converting ranges  to unique ranges
with open('rangef5.txt','r') as infile5:
    with open('runiquef5.txt', 'w') as outfile5:
        for line in infile5:
            if line not in y:
                outfile5.write(line)
                y.add(line)		
		



		
		
		




