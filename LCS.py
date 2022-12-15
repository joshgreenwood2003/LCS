a = "ABCBDAB"
b = "BDCABA"
aux = []
for j in range(0,len(b)+1):
    t = []
    for i in range(0,len(a)+1):
        t.append([0,"-"])
    aux.append(t)

for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            aux[j][i][0] = aux[j-1][i-1][0]+1
            aux[j][i][1] = "↖"
        else:
            if aux[j-1][i][0] < aux[j][i-1][0]:
                aux[j][i][0] = aux[j][i-1][0]
                aux[j][i][1] = "⬅"
            else:
                
                aux[j][i][0] = aux[j-1][i][0]
                aux[j][i][1] = "⬆"

itj = len(b)
iti = len(a)
subbuild = ""
while itj > 0 and iti > 0:
    if aux[itj][iti][1] == "⬅":
        itj -=1
    elif aux[itj][iti][1] == "⬅":
        iti -= 1
    else:
        itj -= 1
        iti -=1
        subbuild= a[iti] + subbuild
print(subbuild)