from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.sample import views

# Partials Requests
urlpatterns = [
    url(r'^partials/list/', views.SampleList.get_partial, name='sample-list-partial'),
]

# API Requests
urlpatterns += format_suffix_patterns([
    url(r'^$', views.SampleList.as_view(), name='sample-list'),
])
