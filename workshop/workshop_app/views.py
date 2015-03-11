from django.shortcuts import render, redirect
from . import forms as app_forms
from . import models

def my_view(request):
	#Entry.objects.create(text='Hello')
	return render(request, 'home.html')

def my_secound_view(request):
	entries = models.Entry.objects.all()
	return render(request, 'secound_page.html', {"entries": entries})#, {'entries': entries})

def form_view(request):
	form = app_forms.FirstForm()
	if request.method == 'POST':
		form = app_forms.FirstForm(request.POST)
		if form.is_valid():
			text = form['text'].value()
			models.Entry.objects.create(lable=text)
			return redirect('secound_view')
	return render(request, 'form_test.html', {'form': form})

# def form_view(request):
# 	form = app_forms.FirstForm()
# 	if request.method == 'POST':
# 		form = app_forms.FirstForm(request.POST)
# 		if form.is_vlaid():
# 			form.save()
# 			return redirect('secound_view')
# 	return render(request, 'form_test.html', {'form': form})