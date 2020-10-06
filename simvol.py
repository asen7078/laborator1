f = open(r'C:\Users\Анастасия\Desktop\Учеба в ИТМО\программирование\lab1\steam_description_data.csv',encoding='utf=8')
k = 0
for i in f:
    for j in i:
        k += 1
f.close()
print(k)