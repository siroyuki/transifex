from django.conf.urls.defaults import *
from django.views.generic import create_update 
from models import *
from feeds import LatestProjects


project_list = {
    'queryset': Project.objects.all(),
}

feeds = {
    'latest': LatestProjects,
}

urlpatterns = patterns('',
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

urlpatterns += patterns('django.views.generic',
    url(
        regex = '^add/$',
        view = 'create_update.create_object',
        name = 'project_add',
        kwargs = {'model' : Project}),
    url(
        regex = '^edit/(?P<slug>[-\w]+)/$',
        view = 'create_update.update_object',
        name = 'project_edit',
        kwargs = {'model' : Project, 'slug_field': 'slug'}),
    url(
        regex = '^delete/(?P<slug>[-\w]+)/$',
        view = 'create_update.delete_object',
        name = 'project_delete',
        kwargs = {'model' : Project, 'slug_field': 'slug',
                  'post_delete_redirect': '/projects'}),
    url(
        regex = '^(?P<slug>[-\w]+)/$',
        view = 'list_detail.object_detail',
        kwargs = project_list,
        name = 'project_detail'),
    url (
        regex = '^$',
        view = 'list_detail.object_list',
        kwargs = project_list,
        name = 'project_list'),
    url(
        regex = '^component/add$',
        view = 'create_update.create_object',
        name = 'component_add',
        kwargs = {'model' : Component}),
)

