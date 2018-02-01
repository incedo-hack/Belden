from django.conf.urls import url
from . import views
#app_name = "myapp"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^AddNewPlugin', views.add_new_plugin, name='Add Plugin'),
    url(r'^ViewPlugins', views.view_rules, name='All Rules'),
    url(r'^AddLogs', views.upload_file, name='Upload Files')
]