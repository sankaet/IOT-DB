from django.conf.urls import patterns, include, url
from iot import v1_views
from django.views.generic import TemplateView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/schemas$', v1_views.schemas, name='schemas'),
    url(r'^v1/schemas/(?P<schema_id>[-\w]+)$', v1_views.schema_by_id, name='schema_by_id'),
)
