import sys
from Replyer import Replyer


def read_input(file_path):
    with open(file_path,'r') as f:
        linhas = f.readlines()
        m,n = linhas[0].split()
        n = int(n)
        qtd_devs = int(linhas[n+1])
        
        qtd_pos = int(linhas[qtd_devs+n+2])
        
        mapa = linhas[1:n+1]
        linhas_devs = linhas[n+2:qtd_devs+n+2]
        linhas_pos = linhas[qtd_devs+n+3::]
        mapa_final = []
        for linha in mapa:
            linha_mapa = [c for c in linha if c !='\n']
            mapa_final.append(linha_mapa)


        list_devs = []
        i = 0
        for dev in linhas_devs:
            dev.replace("\n",'')
            componenetes_dev = dev.split()
            company = componenetes_dev[0]
            bonus = componenetes_dev[1]
            linha_skills = componenetes_dev[3::]
            list_devs.append(Replyer(i, company, bonus, linha_skills))
            i += 1

        list_pos = []
        i = 0
        for po in linhas_pos:
            po.replace("\n",'')
            company,bonus = po.split()
            list_pos.append(Replyer(i, company, bonus))
            i += 1
        return mapa_final, list_devs, list_pos


        


mapa_final, list_devs, list_pos = read_input(sys.argv[1])
print('mapa')
for m in mapa_final:
    print(m)

print('devs')
for item in list_devs:
    print(item.id)
    print(item.company)
    print(item.bonus)
    print(item.skills)
    print(item.dev_friends)
    print(item.po_friends)

print('pos')
for item in list_pos:
    print(item.id)
    print(item.company)
    print(item.bonus)
    print(item.skills)
    print(item.dev_friends)
    print(item.po_friends)