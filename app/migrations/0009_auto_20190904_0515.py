# Generated by Django 2.2.4 on 2019-09-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190902_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.City'),
        ),
    ]
