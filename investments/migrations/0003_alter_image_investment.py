# Generated by Django 3.2.7 on 2021-09-15 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='investment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investments.investment'),
        ),
    ]