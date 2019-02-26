import re


class polynom:

    def __init__(self, inp):
        if isinstance(inp, list):
            self.wsp = []
            for x in inp:
                if isinstance(x, str):
                    self.wsp.append(float(x))
                else:
                    self.wsp.append(float(x))
        elif isinstance(inp, str):
            # for i in inp:
            #     print(i)
            listaliczb=[]
            lista=inp.split('+')

            # if lista[lista.__len__()-1].__len__()==1:
            #     bol=True
            # elif not(lista[lista.__len__()-1][-2]=='+'and int(lista[lista.__len__()-1][-1])  ):
            #     bol=False
            # elif not(lista[lista.__len__()-1][-3]=='+'and int(lista[lista.__len__()-1][-2])):
            #     bol = False
            for i in lista:
                # if i[0]=='-':

                i = re.split("x\^|x", i)
                listaliczb.append(i)
            # print(listaliczb)
            # print(listaliczb[listaliczb.__len__()-1].__len__())
            bol=True
            if listaliczb[listaliczb.__len__()-1].__len__()==2:
                bol=False
            wiel=[]
            # print(listaliczb)

            for i in range(listaliczb.__len__()):
                for j in range(listaliczb[i].__len__()):
                    if listaliczb[i][j]=='':
                        listaliczb[i][j]=1
                    elif listaliczb[i][j][0]=='('and listaliczb[i][j][listaliczb[i][j].__len__()-1]==')':
                        listaliczb[i][j]=int(listaliczb[i][j][1:3])
                    elif listaliczb[i][j][0]=='('and listaliczb[i][j][listaliczb[i][j].__len__()-1]!=')':
                        listaliczb[i][j] = int(listaliczb[i][j][1:listaliczb[i][j].__len__()])
                    elif listaliczb[i][j][0] != '(' and listaliczb[i][j][listaliczb[i][j].__len__() - 1] == ')':
                        listaliczb[i][j] = int(listaliczb[i][j][:listaliczb[i][j].__len__()-1])
                    else:
                        listaliczb[i][j]=int(listaliczb[i][j])
                    # print(listaliczb)

            for i in range(int(listaliczb[0][1])+1):
                wiel.append(0)

            for i in range(listaliczb.__len__()-1):
                wiel[listaliczb[i][1]-wiel.__len__()+1+(i*2)]=listaliczb[i][0]
                # print(listaliczb[i][1],'-',wiel.__len__(),'+',1+(i*2),'   ',listaliczb[i][0])

            if bol==False:
                # print('dziala')
                wiel[listaliczb[listaliczb.__len__()-1][1] - wiel.__len__() + 1 + ((listaliczb.__len__()-1) * 2)] = listaliczb[listaliczb.__len__()-1][0]
            else:
                wiel[wiel.__len__()-1]=listaliczb[listaliczb.__len__()-1][0]
            # print(wiel)
            self.wsp=wiel
        else:
            return false



    def dodaj(self, W):


        if isinstance(W, (polynom)):
            while W.wsp[0] == 0 or self.wsp[0] == 0:
                if W.wsp[0] == 0:
                    W.wsp.pop(0)
                if self.wsp[0] == 0:
                    self.wsp.pop(0)

            minimum = min(len(W.wsp), len(self.wsp))

            while len(W.wsp)!=len(self.wsp):
                if minimum==len(W.wsp):
                    W.wsp.insert(0,0)
                else:
                    self.wsp.insert(0,0)

            for i in range(len(W.wsp)):
                self.wsp[i] += W.wsp[i]

        return self.wypsiywanie()

    def wypsiywanie(self):

        while self.wsp[0] == 0:
            if self.wsp[0] == 0:
                self.wsp.pop(0)

        wielomian = ''
        for i in range(self.wsp.__len__()):
            if i != self.wsp.__len__() - 1:
                if i == self.wsp.__len__() - 2:
                    if self.wsp[i] < 0:
                        wielomian += '(' + str(self.wsp[i]) + 'x' + ')' + '+'
                    else:
                        wielomian += str(self.wsp[i]) + 'x' + '+'
                else:
                    if self.wsp[i] < 0:
                        wielomian += '(' + str(self.wsp[i]) + 'x^' + str(self.wsp.__len__() - 1 - i) + ')' + '+'
                    else:
                        wielomian += str(self.wsp[i]) + 'x^' + str(self.wsp.__len__() - 1 - i) + '+'
            else:
                if self.wsp[i] < 0:
                    wielomian += '(' + str(self.wsp[i]) + ')' + '+'
                else:
                    wielomian += str(self.wsp[i])
        return wielomian

    def mnozenie(self, W):

        if isinstance(W, (polynom)):
            while W.wsp[0]==0 or self.wsp[0]==0:
                if W.wsp[0]==0:
                    W.wsp.pop(0)
                if self.wsp[0] == 0:
                    self.wsp.pop(0)
            nlist = []

            print(nlist)
            minimum = min(len(W.wsp), len(self.wsp))

            while len(W.wsp)!= len(self.wsp):
                if minimum == len(W.wsp):
                    W.wsp.insert(0,0)
                else:
                    self.wsp.insert(0,0)

            for i in range(W.wsp.__len__()+self.wsp.__len__()-1):
                nlist.append(0)

            print(W.wsp)
            print(self.wsp)
            for i in range(len(W.wsp)):
                for j in range(len(self.wsp)):
                    nlist[i+j] += W.wsp[i]*self.wsp[j]

            while nlist[0] == 0 :
                if nlist[0] == 0:
                    nlist.pop(0)

            self.wsp=nlist
            print(self.wsp)
            return self.wypsiywanie()


dwa = polynom('3x^3+(-2x^2)+2x')
D = polynom('-2x^2+1')
C = polynom('x^2+(-2)x+3')
W = polynom([1, 0])
U = polynom([1, 2, 3])

print(D.mnozenie(dwa))
print(W.dodaj(U))