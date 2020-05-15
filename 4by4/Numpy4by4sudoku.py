import numpy as np
fc=np.zeros((5,5),dtype='int')
pv1=np.zeros((5,5),dtype="int")
#BLOCK LISTS
b1=[11,12,21,22]
b2=[13,14,23,24]
b3=[31,32,41,42]
b4=[33,34,43,44]
block_list=[b1,b2,b3,b4]
steps=0

#ACCEPTING VALUES FROM USER/QUESTION

while True :
    inp=input('Would you like to add fc: y/done: ')
    if inp=='d':
        break
    else:
        ij=int(input('enter i,j: '))
        i=int(ij%10)
        j=int(ij/10)
        val=int(input('enter val: '))
        fc[j,i]= val

#question for cehcking
fc[2,1]=1
fc[2,3]=2
fc[3,4]=3
fc[3,2]=4

pv1[1:,1:]=[1234]
#print("pv1=",pv1)
#print("fc=",fc)

#updating pv by removing fc
def Update_PV():
    for j in range(1,5):
        for i in range(1,5):
            if fc[j,i]!=0:
                pv1[j,i]=0

def Update_FC():
    for j in range(1, 5):
        for i in range(1, 5):
            if pv1[j, i] != 0:
                pv1_list = list(map(int, str(pv1[j, i])))
                if len(pv1_list)==1:
                    fc[j,i]=pv1[j,i]
                    pv1_list.remove(fc[j,i])

print(pv1)
Update_PV()
#Update_FC()
while not np.all(fc):
    steps+=1
    for j in range(1, 5):
        for i in range(1, 5):
            if fc[j, i] != 0:
                fc_value = fc[j, i]
                for iterator in range(1, 5):
                    # check row
                    if iterator != i:  # and iterator!=i:
                        pv1_list = list(map(int, str(pv1[j, iterator])))  # converting string from pv1 to lists for removing values from fc
                        try:
                            pv1_list.remove(fc_value)
                        except:
                            ValueError
                        value = "".join(map(str, pv1_list))  # converting list to string and reassigning it to pv1
                        pv1[j, iterator] = value
                    # check column
                    if iterator != j:  # and iterator!=i:
                        pv1_list = list(map(int, str(pv1[iterator, i])))  # converting string from pv1 to lists for removing values from fc
                        try:
                            pv1_list.remove(fc_value)
                        except:
                            ValueError
                        value = "".join(map(str, pv1_list))  # converting list to string and reassigning it to pv1
                        pv1[iterator, i] = value
                #check block
                check_cell=int(str(j)+str(i))
                #print(check_cell)
                for block in block_list: #block list=b1,b2,b3,b4
                    if check_cell in block:  # if check cell  in b1,b2,b3,b4
                        for block_iterator in block:
                            if block_iterator==check_cell:pass
                            else:
                                jj=int(block_iterator/10)
                                ii=(block_iterator%10)
                                # converting string from pv1 to lists for removing values from fc
                                pv1_list = list(map(int, str(pv1[jj, ii])))
                                try:
                                    pv1_list.remove(fc_value)
                                except:
                                    ValueError
                                # print("pv1_list=", j, i, pv1_list)
                                # print(type(pv1_list))
                                # converting list to string and reassigning it to pv1 print(value, type(value))
                                value = "".join(map(str, pv1_list))
                                pv1[jj, ii] = value

    #print(steps)
    Update_FC()
    Update_PV()
    if steps>50:break

print(steps)
print("pv1=")
print(pv1[1:,1:])
print("fc=")
print(fc[1:,1:])
"""
#Map Function
for j in range(1,5):
    for i in range(1,5):
        if fc[j,i]!=0:
            pv1_list=list(map(int, str(pv1[j,i])))      #converting string from pv1 to lists for removing values from fc
            pv1_list.remove(fc[j,i])
            print("pv1_list=",j,i,pv1_list)
            print(type(pv1_list))
            value= "".join(map(str, pv1_list))          #converting list to string and reassigning it to pv1
            print(value,type(value))
            pv1[j, i]=value
print("pv1=",pv1)
print("fc=",fc)
"""
