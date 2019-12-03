from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,'home.html',{'hello': 'This is Hermawan'})

def eggs(request):
	return HttpResponse("<h1>EGGS</h1>")

def count(request):
	fulltext = request.GET['fulltext']
	count = fulltext.split()
	worddict = {}
	for c in count:
		if c in worddict:
			worddict[c] += 1
		else:
			worddict[c] = 1

	maxs = max(worddict, key=worddict.get)
	print(len(count))
	return render(request, 'count.html',{'fulltext':fulltext, 'count':len(count), 'max':maxs})

def about(request):
	return render(request, 'aboutme.html')