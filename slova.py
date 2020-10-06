f = open(r'C:\Users\Анастасия\Desktop\Учеба в ИТМО\программирование\lab1\steam_description_data.csv',encoding='utf=8')
k = 0
s=''
for i in f:
    for j in i:
        if ord(j)!=32:
            s+=j
        elif s!= '':
            k+=1
            s=''
f.close()
print(k)