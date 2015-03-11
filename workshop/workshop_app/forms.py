from django import forms

class FirstForm(forms.Form):
	text = forms.CharField(30, label='Entry', required=True)

	def clean_text(self):
		super(FirstForm, self).clean()
		if 'bla' not in self['text'].value():
			return self.cleaned_data['text']
		raise forms.validationError('"bla" was found')

# from django import forms
# from . import models
# from django.http import HttpResponse
# from django.views.generic import View

# class FirstForm(forms.Form):
# 	class Meta:
# 		model = models.Entry	
# 		fields = ['label']

# 	def clean_text(self):
# 		super(FirstForm, self).clean()
# 		if 'bla' not in self['text'].value():
# 			return self.cleaned_data['text']
# 		raise forms.validationError('"Bla" was found')

# class MyView(View):
# 	def get(self, request):
# 		result = render(request, 'home.html')
# 		return HttpResponse('result')