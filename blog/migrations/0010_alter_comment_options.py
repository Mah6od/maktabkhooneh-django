# Generated by Django 5.0 on 2024-08-05 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
    ]
