# Generated by Django 2.0.7 on 2018-07-26 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0003_auto_20180721_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fav',
            new_name='mood',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
