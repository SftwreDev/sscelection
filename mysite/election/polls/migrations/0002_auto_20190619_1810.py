# Generated by Django 2.2 on 2019-06-19 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='id',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Question'),
            preserve_default=False,
        ),
    ]
