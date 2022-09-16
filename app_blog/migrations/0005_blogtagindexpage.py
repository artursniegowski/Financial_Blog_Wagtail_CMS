# Generated by Django 4.1.1 on 2022-09-12 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0076_modellogentry_revision'),
        ('app_blog', '0004_blogpagetag_blogpage_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTagIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
