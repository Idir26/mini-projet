#!/usr/bin/env python
# -*- coding: utf-8 -*-

def copie(liste):
	if type(liste) == list:
		retour = []
		for i in liste:
			retour.append(copie(i))
	else :
		retour = liste
	return retour
	
def condition(element_1,symbole,element_2):
	if symbole == "==" or symbole == "=":
		return element_1 == element_2
	if symbole == ">":
		return element_1 > element_2
	if symbole == "<":
		return element_1 < element_2
	if symbole == "<=" or symbole == "=<":
		return not(element_1 > element_2)
	if symbole == ">=" or symbole == "=>":
		return not(element_1 < element_2)
	if symbole == "<>" or symbole == "!=":
		return not(element_1 == element_2)

def compare(e1,e2,*elements_de_comparaison):
	for i in elements_de_comparaison:
		print i
		c = 1
		if i < 0:
			c = -1
		j = i*c-1
		if e1[j] > e2[j]:
			return -1*c
		if e1[j] < e2[j]:
			return 1*c
	return 0
def est_dans(table,element):
	#Attention, cette fonction retourne l'indice qui suit la première occurence de l'element dans la self.table
	# et 0 si l'element n'est pas dans la self.table afin de pouvoir être utilisée direcctement comme un boolen
	# il faut donc retrancher 1 au resultat pour l'utiliser comme indice.
	for i in xrange(len(table)):
		if table[i] == element:
			return i+1
	return 0
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
