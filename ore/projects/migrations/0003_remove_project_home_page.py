# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_create_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='home_page',
        ),
    ]
