from django.conf import settings
from django.db import models

class DataObject(models.Model):
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Project(DataObject):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)

class ProjectObject(DataObject):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Entity(ProjectObject):
    pass

class Document(ProjectObject):
    pass

class AttributeType(ProjectObject):
    name = models.TextField()
    type = models.CharField(max_length=10)

class Attribute(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    attribute_type = models.ForeignKey(AttributeType, on_delete=models.CASCADE)

class Relationship(models.Model):
    pass

class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserRevision(models.Model):
    activity = models.ForeignKey(UserActivity, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class AttributeRevision(UserRevision):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

class AttributeState(models.Model):
    attribute = models.ForeignKey(Attribute, primary_key=True)
    revision = models.ForeignKey(AttributeRevision)

class RelationshipRevision(UserRevision):
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    entity_a = models.ForeignKey(Entity, related_name='entity_a', on_delete=models.CASCADE)
    entity_b = models.ForeignKey(Entity, related_name='entity_b', on_delete=models.CASCADE)
    type = models.TextField(null=True, blank=True)

class RelationshipState(models.Model):
    relationship = models.ForeignKey(Relationship, primary_key=True)
    revision = models.ForeignKey(RelationshipRevision)

class DocumentRevision(UserRevision):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    is_article = models.BooleanField()
    article_title = models.CharField(128)
    content = models.TextField(null=True, blank=True)

class DocumentState(models.Model):
    document = models.ForeignKey(Document, primary_key=True)
    revision = models.ForeignKey(DocumentRevision)

class DocumentLink(models.Model):
    document_revision = models.ForeignKey(DocumentRevision, on_delete=models.CASCADE)
    linked_document = models.ForeignKey(Document, on_delete=models.CASCADE)
