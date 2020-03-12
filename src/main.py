import sys
from Replyer import Replyer
from mapa import Mapa


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

        # mapa_final = Mapa(mapa_final)
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

# for m in mapa_final:
#     print(m)
max_score = -1

while(True):
	mapa_ = Mapa(mapa_final) 
	mapa_.config_map()
	mapa_.set_random(list_devs, list_pos)
	score = mapa_.get_score(list_devs, list_pos)
	if max_score < score:
		max_score = score
		
		output_devs = list()
		output_pos = list()
		for dev in list_devs:
			if dev.x != None:
				output_devs.append(str(dev.x) + ' ' + str(dev.y))
			else:
				output_devs.append('X')
		for po in list_pos:
			if po.x != None:
				output_pos.append(str(po.x) + ' ' + str(po.y))
			else:
				output_pos.append('X')
		
		result_output = '\n'.join(output_devs) + '\n' + '\n'.join(output_pos)
		output_filename = sys.argv[2] + '/' + (sys.argv[1].split('/')[-1]).replace('.txt', '') + '.' + str(score)

		print(output_filename)
		with open(output_filename, 'w') as f:
			f.write(result_output)
