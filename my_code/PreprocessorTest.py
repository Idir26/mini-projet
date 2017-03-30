#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mini_projet import *

print "chargement du tableau..."
tableau_general = importer_fichier("mini projet matrice avec regroupement.csv")
print "fait"
def test_trier():
	global tableau_general
	a = copie(tableau_general)
	trier(a)
	afficher_resultats(a,50)
	a = copie(tableau_general)
	trier(a,2,1)
	afficher_resultats(a,50)
	a = copie(tableau_general)
	trier(a,-1,-2)
	afficher_resultats(a,50)
def test_selection():
	global tableau_general
	a = selectionner(tableau_general,"user_id","age_18-24","movie_id","note")
	trier(a,-2,1,3)
	afficher_resultats(a,500)
def test_distinguer():
	global tableau_general
	a = selectionner(tableau_general,"user_id","age_18-24","movie_id","note")
	afficher_resultats(distinguer(a,-2,1),500)
	b = distinguer(selectionner(a,"user_id"),1)
	c = distinguer(selectionner(a,"movie_id"),1)
	print "nombre de personnes:",len(b)-1
	print "nombre de films:",len(c)-1
def test_reduire():
	global tableau_general
	a = selectionner(tableau_general,"user_id","age_18-24","movie_id","note")
	b = reduire(a,"age_18-24",'=',1)
	afficher_resultats(b,50)
	b = reduire(a,"age_18-24",'<>',1,"user_id",">=","movie_id")
	afficher_resultats(b,50)
	b = reduire(a,"user_id",'=',"movie_id")
	afficher_resultats(b,50)
	
	
	



def main(args):
	test_trier()
	test_selection()
	test_distinguer()
	test_reduire()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
