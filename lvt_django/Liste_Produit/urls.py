#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('Liste_Produit.views',
	url(r'^accueil/$', 'home'),
	url(r'^redirection/$', 'view_redirection'),
	url(r'^product/(\d+)/$', 'view_product'), # Vue d'un produit
	url(r'^article/(?P<id_product>\d+)/$','view_article'), # Vue d'un article
	url(r'^products/(?P<cat>\d+)/$','list_products'), #affiche la liste selon le type d" roduit choisi
)