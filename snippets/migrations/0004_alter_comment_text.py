# Generated by Django 3.2.7 on 2021-10-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, verbose_name='コメント'),
        ),
    ]