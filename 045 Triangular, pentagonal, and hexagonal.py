tr = list()
pen = list()
hexo = list()

for i in range(20000, 60000):
    tr.append(i*(i+1)//2)
    pen.append(i*(3*i - 1)//2)
    hexo.append(i*(2*i - 1))


for item in tr:
    if item in pen and item in hexo:
        print(item)
