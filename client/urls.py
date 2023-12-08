from django.urls import include, path

from . import views

def include_interface(view):
    return include([
        path('create', view, {'method': 'create'}),
        path('', view),
        path('edit', view, {'method': 'edit'}),
        path('delete', view, {'method': 'delete'}),
        path('activity', view, {'method': 'activity'}),
    ])

urlpatterns = [
    path('', views.index, name='index'),

    path('Project:<int:project_id>', include_interface(views.project)),
    path('<int:project_id>/<article_title>', include_interface(views.article)),

    path('Note:<int:note_id>', include_interface(views.note)),
    path('Entity:<int:entity_id>', include_interface(views.entity)),
    path('Attribute_Type:<int:attribute_type_id>', include_interface(views.attribute_type)),
]
