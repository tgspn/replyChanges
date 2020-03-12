import sys

def read_input(file_path):
	with open(file_path,'r') as f:
		linhas = f.readlines()
		m,n = linhas[0].split()
		n = int(n)
		print(m, n)
		qtd_devs = int(linhas[n+1])
		print(qtd_devs)
		qtd_pos = int(linhas[qtd_devs+n+2])
		print(qtd_pos)
		mapa = linhas[1:n+1]
		print(mapa)
		linhas_devs = linhas[n+2:qtd_devs+n+2]
		print(linhas_devs)
		linhas_pos = linhas[qtd_devs+n+3::]
		print(linhas_pos)



		


read_input(sys.argv[1])
