# Generated by Django 4.2.2 on 2023-06-20 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_workout_profile_workout_logged_workout_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='user',
        ),
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='name',
            field=models.CharField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workout',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.profile'),
            preserve_default=False,
        ),
    ]
