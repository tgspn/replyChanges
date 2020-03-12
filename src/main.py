import sys

def read_input(file_path):
	with open(file_path,'r') as f:
		linhas = f.readlines()
		m,n = linhas[0].split()
		qtd_devs = int(linhas[int(n)+1])
		qtd_pos = linhas[qtd_devs+1]


		print(str_input)


read_input(sys.argv[1])
