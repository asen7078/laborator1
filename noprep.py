f = open(r'C:\Users\Анастасия\Desktop\Учеба в ИТМО\программирование\lab1\steam_description_data.csv',encoding='utf=8')
k = 0
for i in f:
    for j in i:
        if (ord(j) >= ord('0') & ord(j) <= ord('9')) | (ord(j) >= ord('A') & ord(j) <= ord('Z')) | (ord(j) >= ord('a') & ord(j) <= ord('z')) | ord(j) == 32:
            k += 1
f.close()
print(k)