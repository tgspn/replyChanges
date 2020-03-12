from Replyer import Replyer
import random
class Mapa:
	def __init__(self, mapa):
		self.mapa = mapa


	def config_map(self):
		mapa_aux = []
		for item in self.mapa:
			linha = []
			for item2 in item:
				item2 = item2.replace("#",'-1')
				item2 = item2.replace("_",'-2')
				item2 = item2.replace("M",'-3')
				add = int(item2)
				linha.append([add, -1, -1])
			mapa_aux.append(linha)
		self.mapa = mapa_aux

	def set_random(self, list_devs, list_pos):
		lista_devs_aux = list_devs.copy()
		lista_devs_aux = random.sample(lista_devs_aux, len(lista_devs_aux))

		lista_pos_aux = list_pos.copy()
		lista_pos_aux = random.sample(lista_pos_aux, len(lista_pos_aux))

		for i in range(len(self.mapa)):
			for j in range(len(self.mapa[i])):
				if self.mapa[i][j][0] == -2 and self.mapa[i][j][1] == -1:
					if len(lista_devs_aux) > 0:
						escolha = lista_devs_aux.pop()
						self.mapa[i][j][1] = escolha.id
						escolha.x = i
						escolha.y = j
				if self.mapa[i][j][0] == -3 and self.mapa[i][j][1] == -1:
					if len(lista_pos_aux) > 0:
						escolha = lista_pos_aux.pop()
						self.mapa[i][j][1] = escolha.id
						escolha.x = i
						escolha.y = j
		return self




	def get_score(self, list_devs, list_pos):
		score_map = 0
		for i in range(len(self.mapa)):
			for j in range(len(self.mapa[i])):
				if self.mapa[i][j][0] == -2 and self.mapa[i][j][1] != -1:
					dev = list_devs[self.mapa[i][j][1]]
					coleguinhas = self.get_colegas(i, j)
					score_coleguinhas = 0
					for colega in coleguinhas:
						x, y = colega[0], colega[1]
						if self.mapa[x][y][0] == -2 and self.mapa[x][y][1] != -1: 
							dev2 = list_devs[self.mapa[x][y][1]]
							score_coleguinhas += self.calc_score_posic(dev, dev2)
						if self.mapa[x][y][0] == -3 and self.mapa[x][y][1] != -1: 
							po2 = list_devs[self.mapa[x][y][1]]
							score_coleguinhas += self.calc_score_posic(dev, po2)
						score_map += score_coleguinhas
						self.mapa[i][j][2] = score_coleguinhas
				if self.mapa[i][j][0] == -3 and self.mapa[i][j][1] != -1:
					po = list_devs[self.mapa[i][j][1]]
					coleguinhas = self.get_colegas(i, j)
					score_coleguinhas = 0
					for colega in coleguinhas:
						x, y = colega[0], colega[1]
						if self.mapa[x][y][0] == -2 and self.mapa[x][y][1] != -1: 
							dev2 = list_devs[self.mapa[x][y][1]]
							score_coleguinhas += self.calc_score_posic(po, dev2)
						if self.mapa[x][y][0] == -3 and self.mapa[x][y][1] != -1: 
							po2 = list_devs[self.mapa[x][y][1]]
							score_coleguinhas += self.calc_score_posic(po, po2)
						score_map += score_coleguinhas
						self.mapa[i][j][2] = score_coleguinhas
		return score_map

	def pegar_o_mais_fdp(self):
		menor = 10000**10000
		x = -1
		y = -1
		for i in range(len(self.mapa)):
			for j in range(len(self.mapa[i])):
				if self.mapa[i][j][2] < menor and self.mapa[i][j][0] != -1:
					x = i
					y = j
					menor = self.mapa[i][j][2]
		return x, y


	def random_swap_fdp(self, x, y, list_devs, list_pos):
		lista_devs_aux = list_devs.copy()
		lista_devs_aux = random.sample(lista_devs_aux, len(lista_devs_aux))

		lista_pos_aux = list_pos.copy()
		lista_pos_aux = random.sample(lista_pos_aux, len(lista_pos_aux))
		if self.mapa[x][y] == -2:
			if len(lista_devs_aux) > 0:
				escolha = lista_devs_aux.pop()
				if escolha.x == None:
					escolha.x = x
					escolha.y = y
					anterior = list_devs[self.mapa[x][y][1]]
					anterior.x = None
					anterior.y = None
					self.mapa[x][y][1] = escolha.id
				else:
					anterior = list_devs[self.mapa[x][y][1]]
					anterior.x = escolha.x
					anterior.y = escolha.y
					escolha.x = x
					escolha.y = y
					self.mapa[x][y][1] = escolha.id





	def get_colegas(self, i, j):
		lista = []
		if i-1 >=0:
			lista.append((i-1, j))
		if i+1 < len(self.mapa):
			lista.append((i+1, j))
		if j-1 >=0:
			lista.append((i, j-1))
		if j+1 < len(self.mapa[i]):
			lista.append((i, j+1))
		return lista

	def calc_score_posic(self, cara, coroa):
		power = 0
		skills_cara = set(cara.skills.copy())
		skills_coroa = set(coroa.skills.copy())
		common_skills = skills_cara  & skills_cara
		unique_skills = skills_coroa - skills_coroa
		power += len(common_skills) * len(unique_skills)
		if cara.company == coroa.company:
			power += int(cara.bonus) * int(coroa.bonus)
		return power