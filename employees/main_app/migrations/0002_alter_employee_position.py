# Generated by Django 4.0.2 on 2022-02-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('A_position', 'A_position'), ('B_position', 'B_position'), ('C_position', 'C_position'), ('D_position', 'D_position')], max_length=10),
        ),
    ]