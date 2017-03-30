#!/usr/bin/env python
# -*- coding: utf-8 -*-
from outils import *
from sys import argv
from sklearn.base import BaseEstimator
from zDataManager import DataManager
from sklearn.decomposition import PCA

class Preprocessor:
	def __init__(self):
		self.table = []
		self.categories = []
		self.transformer = PCA(n_components=2)
	def importer_fichier(self,fichier):
		f = open(fichier,"r")
		chargement_categories = False
		for ligne in f:
			element = []
			chaine_valeur = ""
			flotant = False
			for carractere in ligne:
				if carractere == '.':
					flotant = True
				if carractere == ","or carractere == ";" :
					if chargement_categories:
						if flotant:
							element.append(float(chaine_valeur))
							flotant = False
						else:
							element.append(int(chaine_valeur))
					else:
						self.categories.append(chaine_valeur)
					chaine_valeur = ""
				elif carractere <> '\n' and carractere <> '\r':
					chaine_valeur += carractere
			if chargement_categories:
				if flotant:
					element.append(float(chaine_valeur))
				else:
					element.append(int(chaine_valeur))
				self.table.append(copie(element))
			else:
				self.categories.append(chaine_valeur)
				chargement_categories = True
	def copie(self,prepro):
		self.categories = copie(prepro.categories)
		self.table = copie(prepro.table)
	def echanger(self,i,j):
		temp = self.table[i]
		self.table[i] = self.table[j]
		self.table[j] = temp
	def trier_r(self,x,y,*elements_de_comparaison):
		if x > y-1:
			return 0
		self.echanger(x,y)
		m = -1
		for i in range(x,y+1):
			if m == -1:
				if self.compare(self.table[y],self.table[i],*elements_de_comparaison) > -1:
					m = i
			else:
				if self.compare(self.table[y],self.table[i],*elements_de_comparaison) <1:
					self.echanger(i,m)
					m+=1
		if m > -1:
			self.trier_r(x,m-1,*elements_de_comparaison)
		self.trier_r(m,y,*elements_de_comparaison)		
	def trier(self,*elements_de_comparaison):
		#Attention : les elements de comparaison sont les indices des critères (dans l'ordre souhaité) +1,
		# en effet s l'on souhaite trier selon un critère dans l'ordre décroissant, il suffit de noter l'opposé de 
		# son indice majoré de 1 (et donc l'indice 0 n'offrant la possibilité de prendre l'opposé il a été preferable de le retirer)
		if len(self.table) == 0:
			return None
		if elements_de_comparaison == ():
			elements_de_comparaison = range(1,len(self.elements)+1)
		self.trier_r(0,len(self.table)-1,*elements_de_comparaison)

	def afficher_resultats(self,categories = False,rang = False,limite = -1):
		if categories:
			print self.categories
		for i in xrange(len(self.table)):
			if rang :
				print i,':',
			print self.table[i]
			if i == limite : 
				break
	def selectionner(self,*choix):
		if len(self.table) == 0:
			return []
		rangs = []
		for critere in choix:
			r = est_dans(self.categories,critere)
			if r :
				rangs.append(r-1)
			else:
				print critere,"n'est pas dans les catégories proposées"
		resultat = []
		cat = []
		for r in rangs:
			cat.append(self.categories[r])
		self.categories = cat
		for ligne in self.table:
			elements = []
			for r in rangs:
				elements.append(ligne[r])
			resultat.append(copie(elements))
		self.table = resultat
		
	def reduire(self,element_1,sybole,element_2,*autres):
		resultat = []
		conditions = [element_1,sybole,element_2]
		for i in autres : 
			conditions.append(i)
		for i in range(len(conditions)/3):
			if type(conditions[3*i]) == str:
				n = est_dans(self.categories,conditions[3*i])
				if n:
					conditions[3*i] = str(n-1)			
				else:
					print conditions[3*i],"n'est pas dans les criteres"
					return None
			if type(conditions[3*i+2]) == str:
				n = est_dans(self.categories,conditions[3*i+2])
				if n:
					conditions[3*i+2] = str(n-1)			
				else:
					print conditions[3*i+2],"n'est pas dans les criteres"
					print "les criteres sont :",self.categories
					return None
		for ligne in self.table:
			ajouter = True
			j = 0
			while ajouter and not(j>len(conditions)-3) :
				a = conditions[j]
				b = conditions[j+2]
				if type(a) == str:
					a = ligne[int(a)]
				if type(b) == str:
					b = ligne[int(b)]
				ajouter = ajouter and condition(a,conditions[j+1],b)
				j+=3
			if ajouter:
				resultat.append(ligne)
			
		self.table = resultat

	def Est_triee(self,*criteres):
		stable = 0
		for i in range(len(self.table)-1):
			if stable == 0:
				stable = self.compare(self.table[i],self.table[i+1],*criteres)
			elif self.compare(self.table[i],self.table[i+1],*criteres) == -stable:
				return False
		return True
	def rangs(self,elements):
		retour = []
		for i in range(len(elements)):
			if type(elements[i]) == str:
				n = Est_dans(self.categories,elements[i])
				if n :
					elements[i] = n
				elif i[0] == "-":
					n = est_dans(self.categories,i[1:])
					if n:
						elements[i] = -n
					else:
						return i,"n'est pas dans les criteres",self.categories
				else:
					return i,"n'est pas dans les criteres",self.categories
	def compare(self,e1,e2,*elements_de_comparaison):
		for i in elements_de_comparaison:
			c = 1
			if i < 0:
				c = -1
			j = i*c-1
			if e1[j] > e2[j]:
				return -1*c
			if e1[j] < e2[j]:
				return 1*c
		return 0
	def distinguer(self,*criteres):
		if criteres == ():
			criteres = range(1,len(self.categories)+1)
		self.trier(*criteres)
		if not(self.Est_triee(*criteres)):
			print 1
			if len(self.table) == 0:
				return None
		self.afficher_resultats()
		retour = []
		for i in range(len(self.table)):
			if len(retour) == 0 or self.compare(retour[-1],self.table[i],*criteres):
				retour.append(self.table[i])
		self.table = retour
	def somme(self):
		somme = []
		for i in self.categories:
			somme.append(0)
		for ligne in self.table:
			for j in range(len(self.categories)):
				somme[j] += ligne[j]
		return somme  
	def fit(self, X, y=None):
		return self.transformer.fit(X, y)

	def fit_transform(self, X, y=None):
		return self.transformer.fit_transform(X)

	def transform(self, X, y=None):
		return self.transformer.transform(X)		
def main(args):
	print "chargement du tableau..."
	tableau_general = preprocessing()
	tableau_general.importer_fichier("mini projet matrice avec regroupement.csv")
	print "copie"
	table = preprocessing()
	table.copie(tableau_general)
	table.reduire("movie_id","==",1996,"note",">=",2)
	table.selectionner("age_-18","age_18-24","age_25-34","age_35-44","age_45-49","age_50-55","age_56+")
	table.afficher_resultats(True,True,50)
	print table.somme()
	table.distinguer()
	table.afficher_resultats(True,True,50)
	print table.somme()
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
