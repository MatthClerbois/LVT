#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, Http404

def home(request):
	text = """<h1>Bienvenue sur mon blog !</h1>
				<p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
	return HttpResponse(text)

def view_product(request, id_product):
	""" Vue qui affiche un article selon son identifiant (ou ID,
	ici un numéro). Son ID est le second paramètre de la fonction
	(pour rappel, le premier paramètre est TOUJOURS la requête de
	l'utilisateur) """

	text = "Vous avez demandé le produit n°{0} !".format(id_product)
	return HttpResponse(text)

def list_products(request,cat):
	"""liste des produits du type recherché."""
	text ="Vous avez demandé les produits de type {0} ".format(cat)
	return HttpResponse(text)

def view_article(request, id_product):
	if int(id_product) > 100: 	#Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
		raise Http404
	return HttpResponse('<h1>Mon article ici</h1>')

def redirect_to(request,id_product):	
	if int(id_product) > 100: 	#Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
		raise Http404
	return redirect(view_redirection)

def view_redirection(request):
	return HttpResponse(u"Vous avez été redirigé.")