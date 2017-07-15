from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
	""" Exemple de page HTML non vvalide pour que l'Exemple soit concis """
	text = """<h1>Bienvenus sur ce presque site..</h1>
				<p>J'espère qu'on se retrouvera assez vite</p>"""
	return HttpResponse(text)
