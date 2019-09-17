#Dimention of paper A0 is given : 1189mm X 841mm
length = 1189
breath = 841
for i in range(1,9):
    temp = length
    length = breath
    breath = temp / 2
    print("Dimention of A{} : {}mm X {}mm".format(i,length,breath))
