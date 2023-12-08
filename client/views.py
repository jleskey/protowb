from django.shortcuts import render

from .models import AttributeRevision, DocumentRevision, Entity, Document, AttributeType, Project

def renderDefault(request, path, method='view', options={}):
    option_throughput = {
        'project_list': Project.objects.all(),
        'method': method,
    }

    for key, value in options.items():
        option_throughput[key] = value

    return render(request, path, option_throughput)

def index(request, project_id=None):
    return renderDefault(request, "client/index.html", 'view', {
        'project_id': project_id,
        'entity_list': Entity.objects.filter(project_id=project_id),
        'document_list': Document.objects.filter(project_id=project_id),
        'attribute_type_list': AttributeType.objects.filter(project_id=project_id),
    })

def project(request, project_id, method='view'):
    return renderDefault(request, "client/project.html", method, {
        'project_id': project_id,
        'project': Project.objects.get(pk=project_id),
    })

def article(request, project_id, article_title, method='view'):
    # NOTE: If a title existed in the path, but the page was renamed, we
    # could automatically display the contents of the new page. That being
    # said, it may make more sense to allow users to do this manually.

    return renderDefault(request, "client/article.html", method, {
        'project_id': project_id,
        'article_title': article_title,
        'article': DocumentRevision.objects.get(
            article_title=article_title,
            documentstate__isnull=False,
        ),
    })

def note(request, note_id, method='view'):
    return renderDefault(request, "client/note.html", method, {
        'note_id': note_id,
        'note': DocumentRevision.objects.get(
            document__pk=note_id,
            is_article=False,
            documentstate__isnull=False,
        ),
    })

def entity(request, entity_id, method='view'):
    return renderDefault(request, "client/entity.html", method, {
        'entity_id': entity_id,
        'entity': Entity.objects.get(pk=entity_id),
        'attribute_list': AttributeRevision.objects.filter(
            entity__pk=entity_id,
            attributestate__isnull=False,
        )
    })

def attribute_type(request, attribute_type_id, method='view'):
    return renderDefault(request, "client/attribute_type.html", method, {
        'attribute_type_id': attribute_type_id,
        'attribute_type': AttributeType.objects.get(pk=attribute_type_id),
    })
