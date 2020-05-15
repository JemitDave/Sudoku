import json
from collections import OrderedDict
fc=OrderedDict()
fc[11]=0
fc[12]=0
fc[13]=0
fc[14]=0
fc[21]=0
fc[22]=0
fc[23]=0
fc[24]=0
fc[31]=0
fc[32]=0
fc[33]=0
fc[34]=0
fc[41]=0
fc[42]=0
fc[43]=0
fc[44]=0
#print(json.dumps(fc, indent=4))
#for fc,value in fc.items():
#    print(type(fc),type(value))     #class int,  class int
pv=OrderedDict()
pv[11]=[1,2,3,4]
pv[12]=[1,2,3,4]
pv[13]=[1,2,3,4]
pv[14]=[1,2,3,4]
pv[21]=[1,2,3,4]
pv[22]=[1,2,3,4]
pv[23]=[1,2,3,4]
pv[24]=[1,2,3,4]
pv[31]=[1,2,3,4]
pv[32]=[1,2,3,4]
pv[33]=[1,2,3,4]
pv[34]=[1,2,3,4]
pv[41]=[1,2,3,4]
pv[42]=[1,2,3,4]
pv[43]=[1,2,3,4]
pv[44]=[1,2,3,4]
#BLOCK LISTS
b1=[11,12,21,22]
b2=[13,14,23,24]
b3=[31,32,41,42]
b4=[33,34,43,44]
block_list=[b1,b2,b3,b4]
#print(json.dumps(pv, indent=4))
#for pv,value in pv.items():
#    print(type(pv),type(value))   # class int, class list
#check = pv.get(11)
#print(check)
while True :                #accepting values from question
    inp=input('Would you like to add fc: y/done: ')
    if inp=='done':
        break
    else:
        i=int(input('enter i: '))
        j=int(input('enter j: '))
        val=int(input('enter val: '))
        ij=int(str(i)+str(j))
        fc[ij]= val
for iteration in fc.values():
    if iteration!=0:
        def update():
            for fcell, value in fc.items():  # UPDATES PV WRT FC ie removes all the fc in pv
                if value != 0:
                    if fcell in pv:
                        try:
                            # print(fc,value)

                            pv.pop(fcell)
                        # print(json.dumps(pv, indent=4))
                        except KeyError:
                            pass


        def check_row(i, j, value):
            for pcell, value2 in pv.items():
                m = pcell // 10
                n = pcell % 10
                if m == i:
                    try:
                        value2.remove(value)
                    except ValueError:
                        pass


        def check_col(i, j, value):
            for pcell, value2 in pv.items():
                m = pcell // 10
                n = pcell % 10
                if n == j:
                    try:
                        value2.remove(value)
                    except ValueError:
                        pass


        def check_block(fcell, value):
            for block in block_list:  # block_list=[b1,b2,b3,b4]
                # print(block)
                for blockcell in block:  # b1=[11,12,21,22] b2=[13,14,23,24]
                    # print(blockcell)
                    if blockcell == fcell:
                        for blockcell in block:
                            try:
                                pv[blockcell].remove(value)
                            except:
                                ValueError


        update()
        for fcell, value in fc.items():  # UPDATES ROW AND COL
            if value != 0:
                i = fcell // 10
                j = fcell % 10
                check_row(i, j, value)
                check_col(i, j, value)

        for fcell, value in fc.items():  # UPDATES pv blockwise
            if value != 0:
                # print(fcell)
                check_block(fcell, value)

        newpv = pv.copy()
        for pcell, value2 in newpv.items():
            # print(value)
            if len(value2) == 1:
                for ans in value2:
                    # print(pcell,type(ans),type(value2))
                    fc[pcell] = ans
                    update()


#print(json.dumps(pv, indent=7))
#print(json.dumps(fc, indent=4))
printer=list()
for keys,values in fc.items():
    i=keys//10
    j=keys%10
    #print(keys)
    printer.append(values)
    if i==3 and j==4:
        print('________________')
    #print(keys,printer)
    if len(printer)==4:
        printer.insert(2,"/")
        print(printer)
        printer.clear()

