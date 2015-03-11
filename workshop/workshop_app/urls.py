from django.conf.urls import patterns, url

urlpatterns = patterns('',

	url(r'^$', 'workshop_app.views.my_view', name = 'my_view'),
	url(r'^secound_page', 'workshop_app.views.my_secound_view', name = 'secound_view'),
	url(r'^form_test', 'workshop_app.views.form_view', name='form_view'),

	)
