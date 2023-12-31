# Generated by Django 4.2.7 on 2023-11-29 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipRevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.useractivity')),
                ('entity_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_a', to='client.entity')),
                ('entity_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_b', to='client.entity')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.relationship')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='entity',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project'),
        ),
        migrations.CreateModel(
            name='DocumentRevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_article', models.BooleanField()),
                ('content', models.TextField(blank=True, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.useractivity')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.documentrevision')),
                ('linked_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project'),
        ),
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.TextField()),
                ('type', models.CharField(max_length=10)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeRevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.useractivity')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.attributetype'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.entity'),
        ),
    ]
