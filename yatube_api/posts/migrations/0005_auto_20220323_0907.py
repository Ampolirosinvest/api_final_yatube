# Generated by Django 2.2.16 on 2022-03-23 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20220323_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('title',)},
        ),
    ]