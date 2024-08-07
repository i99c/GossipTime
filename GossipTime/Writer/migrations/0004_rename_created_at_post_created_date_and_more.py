# Generated by Django 5.0.7 on 2024-07-15 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
        ('Writer', '0003_alter_dislike_create_date_alter_like_create_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='updated_date',
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='Login.writer', verbose_name='Yazar'),
        ),
    ]
