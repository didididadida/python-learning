
def cacluate():
    a = 0
    ls1 = input('Please input numbers,and press the Enter to end.(gap with ,)').split(',')

    #print(ls1)
    for i in range(0, len(ls1)):
        a = a + float(ls1[i])
    b = len(ls1)
    c= a / b
    #print(c)
    ls = []
    for q in range(0,len(ls1)):
        if float(ls1[q]) > c:
            w = int(ls1[q])
            ls.append(w)
    aut = (c,ls)
    print('\n',aut)


cacluate()
