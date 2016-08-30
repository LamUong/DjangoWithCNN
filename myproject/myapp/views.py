from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse
from .forms import ImageUploadForm
from .models import PictureModel
from facedetection import main
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from PIL import Image
##from myproject.myapp.models import Document
#from myproject.myapp.forms import DocumentForm
from django.http import HttpResponse
import urllib, cStringIO
import os
import requests
from StringIO import StringIO
import time
import uuid
import json
import validators
'''
def list(request):
	# Handle file upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
			# Redirect to the document list after POST
			return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
	else:
		form = DocumentForm() # A empty, unbound form
	# Load documents for the list page
	documents = Document.objects.all()
	# Render list page with the documents and the form
	return render_to_response(
		'myapp/list.html',
		{'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)
'''
@csrf_exempt
def fileAttachment(request):
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			m = PictureModel()
			m.model_pic = form.cleaned_data['image']
			m.name = m.model_pic.url
			m.save()
			image = Image.open(m.model_pic)
			width, height = image.size
			if width > 600:
				basewidth = 400
				wpercent = (basewidth/float(image.size[0]))
				hsize = int((float(image.size[1])*float(wpercent)))
				image = image.resize((basewidth,hsize), Image.ANTIALIAS)
			FileName = str(uuid.uuid1())+".png"
			Pathname = "/home/ubuntu/DjangoWithCNN/myproject/media/"+FileName
			image.save(Pathname)
			result = main(Pathname)
			print(result)
			return HttpResponse(result)
		else:
			return HttpResponse(json.dumps({'data':"File uploaded is not an image",'url':"/home/ubuntu/DjangoWithCNN/myproject/media/blank_person.png"}))

@csrf_exempt
def urlLinkSpecified(request):
	if request.method == 'POST':
		url = request.POST.get("url")
		if validators.url(url):
			start_time = time.time()
			response = requests.get(url)
			maintype= response.headers['Content-Type'].split(';')[0].lower()
			if maintype not in ('image/png', 'image/jpeg', 'image/gif'):
				print("a")
				return HttpResponse(json.dumps({'data':"Url is not of image type",'url':"/home/ubuntu/DjangoWithCNN/myproject/media/blank_person.png"}))
			else:
				img = Image.open(StringIO(response.content))		
				FileName = str(uuid.uuid1())+".png"
				Pathname = "/home/ubuntu/DjangoWithCNN/myproject/media/"+FileName
				width, height = img.size
				if width > 600:
					basewidth = 400
					wpercent = (basewidth/float(img.size[0]))
					hsize = int((float(img.size[1])*float(wpercent)))
					img = img.resize((basewidth,hsize), Image.ANTIALIAS)
				img.save(Pathname)
				print("--- %s seconds ---" % (time.time() - start_time))
				result = main(Pathname)
				print(result)
				return HttpResponse(result)
		else:
			return HttpResponse(json.dumps({'data':"Invalid URL",'url':"/home/ubuntu/myproject/media/blank_person.png"}))

def index(request):
	form = ImageUploadForm()
	return render(request, 'webpage.html', {'form': form})

def intro(request):
	return render(request, 'intro.html')



																																																																																


