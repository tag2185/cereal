from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from main.models import Manufacturer, Cereal

# Create your views here.


def cereal_list_view(request):

	manufacturers = Manufacturer.objects.all()

	cereal_string = ""

	for manufacturer in manufacturers:

		cereal_string += "<h4>%s</h4>" % manufacturer
		
		for cereal in manufacturer.cereal_set.all():
			cereal_string += "%s </br>" % cereal.name

	return HttpResponse(cereal_string)

def cereal_list_template(request):

	manufacturers = Manufacturer.objects.all()

	context = {}

	context['manufacturers'] = manufacturers
	
	return render(request, 'cereal_list.html', context)


def cereal_list_template2(request):

	manufacturers = Manufacturer.objects.all()

	context = {}

	manufacturer_cereal = {}

	for manufacturer in manufacturers:
		cereals = manufacturer.cereal_set.filter(name__contains="A")

		manufacturer.name = { manufacturer.name : cereals }

		manufacturer_cereal.update(manufacturer.name)		

	context['manufacturer_cereal'] = manufacturer_cereal
	
	#return render(request, 'cereal_list2.html', context)
	return render_to_response('cereal_list2.html', context, context_instance=RequestContext(request))


def cereal_search(request, cereal):

	cereals = Cereal.objects.filter(name__istartswith=cereal)

	cereal_string = ""

	for cereal in cereals:
		cereal_string += "<b>Cereal:</b>%s, <b>Manufacturer:</b>%s, <b>Protine</b>%s</br>" % (cereal.name, cereal.manufacturer, cereal.nutritionfacts.protein)


	return HttpResponse(cereal_string)


def get_cereal_search(request):

	print request.GET

	#cereal = request.GET['cereal']

	cereal = request.GET.get('cereal', 'None')

	cereals = Cereal.objects.filter(name__istartswith=cereal)

	cereal_string = """  
	<form action='/get_cereal_search/' method='GET'>

	Cereal:
	</br>
	<input type="text" name="cereal" >

	</br>
	<input type="submit" value="Submit" >

	</form>
	"""

	for cereal in cereals:
		cereal_string += "<b>Cereal:</b>%s, <b>Manufacturer:</b>%s </br>" % (cereal.name, cereal.manufacturer)
		for neutrition in cereal.nutritionfacts.nutrition_list():
			cereal_string += "%s </br>" % neutrition

	return HttpResponse(cereal_string)





