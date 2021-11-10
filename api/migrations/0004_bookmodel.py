# Generated by Django 3.2.9 on 2021-11-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_authordtomodel_authormodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('edition', models.CharField(max_length=10)),
                ('publication_year', models.CharField(max_length=4)),
                ('authors', models.ManyToManyField(to='api.AuthorModel')),
            ],
        ),
    ]
