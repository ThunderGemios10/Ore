# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields

def create_home_pages(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Page = apps.get_model('projects', 'Page')

    for project in Project.objects.all():
        # Rather hacky way, but is DRY
        home_page = Page.objects.create(
            project=project,
            parent=None,
            title='Home',
            content='Welcome to your new project!'
        )
        project.home_page = home_page
        home_page.save()
        project.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(no_check_for_status=True, max_length=100, default='active', choices=[('active', 'active'), ('deleted', 'deleted')])),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('content', models.TextField()),
                ('html', models.TextField()),
                ('parent', models.ForeignKey(blank=True, to='projects.Page', null=True, related_name='children')),
                ('project', models.ForeignKey(to='projects.Project', related_name='pages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('project', 'slug'), ('project', 'title')]),
        ),
        migrations.AddField(
            model_name='project',
            name='home_page',
            field=models.OneToOneField(related_name='home_project', to='projects.Page', null=True),
            preserve_default=False,
        ),
        migrations.RunPython(
            create_home_pages
        ),
        migrations.AlterField(
            model_name='project',
            name='home_page',
            field=models.OneToOneField(related_name='home_project', to='projects.Page', null=False),
            preserve_default=False,
        ),
    ]
