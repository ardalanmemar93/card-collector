# Generated by Django 4.2.6 on 2023-11-03 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_apraisal_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='apraisal',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.card'),
            preserve_default=False,
        ),
    ]
