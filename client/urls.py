from django.urls import include, path

from django.shortcuts import redirect

from . import views

def include_interface(view, namespace=None):
    return include(([
        path('create', view, {'method': 'create'}, name='create'),
        path('', view, name='view'),
        path('edit', view, {'method': 'edit'}, name='edit'),
        path('delete', view, {'method': 'delete'}, name='delete'),
        path('activity', view, {'method': 'activity'}, name='activity'),
    ], namespace))

urlpatterns = [
    path('', views.index, name='index'),

    path('Project:<int:project_id>', include_interface(views.project, 'project')),
    path('<int:project_id>', lambda request, project_id : redirect('project:view', project_id=project_id, permanent=True)),
    path('<int:project_id>/<article_title>', include_interface(views.article, 'article')),

    path('Note:<int:note_id>', include_interface(views.note, 'note')),
    path('Entity:<int:entity_id>', include_interface(views.entity, 'entity')),
    path('Attribute_Type:<int:attribute_type_id>', include_interface(views.attribute_type, 'attribute_type')),
]
