# Generated by Django 4.1.1 on 2022-09-12 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0076_modellogentry_revision'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSpecificSocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(blank=True, max_length=100)),
                ('facebook', models.URLField(blank=True, max_length=100)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Site-specific social media settings',
            },
        ),
    ]
