# Generated by Django 3.2.7 on 2021-09-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='nationality',
            field=models.CharField(choices=[('1', 'Rwandan'), ('2', 'Kenyan'), ('3', 'Ugandan'), ('4', 'South Sudanese'), ('5', 'Sudanese')], max_length=15, null=True),
        ),
    ]
