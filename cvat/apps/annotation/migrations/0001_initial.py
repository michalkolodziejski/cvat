# Generated by Django 2.1.9 on 2019-07-24 08:39

import cvat.apps.annotation.models
import cvat.apps.engine.models
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import os

def create_builtins(apps, schema_editor):
    AnnotationDumperModel = apps.get_model('annotation', 'AnnotationDumper')
    AnnotationParserModel = apps.get_model('annotation', 'AnnotationParser')

    path_prefix = os.path.join("cvat", "apps", "annotation", "builtin")

    AnnotationDumperModel(
        name="cvat_xml_for_images",
        display_name="CVAT XML for images",
        extension="xml",
        handler_file=os.path.join(path_prefix, "cvat", "dumper.py"),
        owner=None,
    ).save()

    AnnotationDumperModel(
        name="cvat_xml_for_videos",
        display_name="CVAT XML for videos",
        extension="xml",
        handler_file=os.path.join(path_prefix, "cvat", "dumper.py"),
        owner=None,
    ).save()

    AnnotationParserModel(
        name="cvat_xml",
        display_name="CVAT XML",
        extension="xml",
        handler_file=os.path.join(path_prefix, "cvat", "parser.py"),
        owner=None,
    ).save()

    AnnotationDumperModel(
        name="pascal_voc_xml",
        display_name="Pascal VOC XML",
        extension="zip",
        handler_file=os.path.join(path_prefix, "pascal_voc", "dumper.py"),
        owner=None,
    ).save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationDumper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('extension', models.CharField(max_length=32)),
                ('display_name', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('handler_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=settings.BASE_DIR), upload_to=cvat.apps.annotation.models.upload_dumper_handler)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='AnnotationParser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('extension', models.CharField(max_length=32)),
                ('display_name', cvat.apps.engine.models.SafeCharField(max_length=256)),
                ('handler_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=settings.BASE_DIR), upload_to=cvat.apps.annotation.models.upload_parser_handler)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.RunPython(create_builtins),
    ]
