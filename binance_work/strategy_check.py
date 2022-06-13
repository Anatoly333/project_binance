a = str
s = r'C:\Users\Анатолий\Desktop\Project_Binance\Svetchi.txt'
f = open(s)
a = f.read()
c = str
q = []
i = 0
j = 0
i = chr
z = int
r = int
e = int
mas = []
rubbish = []
WinCounter = int
LoseCounter = int
WinShablonCounter = int
LoseShablonCounter = int
#while i < len(a):
 #   if a[i] =='"':
  #      a.replace('"','')
   # i = i+1
#a.split(',')
for i in ['"']:
    if i in a:
        a = a.replace(i,'')
a = a[1:]
a = a[:-1]
a = a[1:]
a = a[:-1]
r = len(a)

a = a.split("],[")
for i in range(len(a)):
    a[i] = a[i].split(",")
    i = i+1
i = 0
e = 0
for i in range(len(a)):
    if a[i][1] < a[i][4]:
        mas.append("1")
    elif a[i][1] > a[i][4]:
        mas.append("0")
    elif a[i][1] == a[i][4]:
        rubbish.append("5")
        e = e+1
    #i = i+1

i = 0
WinShablonCounter = 0
LoseShablonCounter = 0
for i in range(len(mas)-3):
    if ((mas[i] == '0') and (mas[i+1] == '1') and (mas[i+2] == '1') and (a[i][3] < a[i+2][3])) or ((mas[i] == '1') and (mas[i+1] == '0') and (mas[i+2] == '0') and (a[i][3] > a[i+2][3])):
        WinShablonCounter = WinShablonCounter+1
    else:
        LoseShablonCounter = LoseShablonCounter+1
i = 0
WinCounter = 0
LoseCounter = 0
for i in range(len(mas) - 4):
    if ((mas[i] == '0') and (mas[i+1] == '1') and (mas[i+2] == '1') and (a[i][3] < a[i+2][3])) and (a[i+3][3] > a[i+2][3]) or ((mas[i] == '1') and (mas[i+1] == '0') and (mas[i+2] == '0') and (a[i][3] > a[i+2][3]) and (a[i+3][3] < a[i+2][3])):
        WinCounter = WinCounter + 1
        print(a[i],a[i+1],a[i+2],a[i+3],"+",r"\n")
    elif((mas[i] == '0') and (mas[i+1] == '1') and (mas[i+2] == '1') and (a[i][3] < a[i+2][3])) or ((mas[i] == '1') and (mas[i+1] == '0') and (mas[i+2] == '0') and (a[i][3] > a[i+2][3])):
        LoseCounter = LoseCounter + 1
        print(a[i], a[i+1], a[i+2], a[i+3], "-", r"\n")
print(len(mas))
print(LoseShablonCounter)
print(WinShablonCounter)
print(LoseCounter)
print(WinCounter)
print(e)



#i = 0
#mas = mas*len(a)
#for i in range(len(a)):
    #mas[i] = a[i]
    #i = i+1


#while z==0:
 #   a = a.replace(a[r-2],'')
  #  z = z+1
#1 - Медвежья
