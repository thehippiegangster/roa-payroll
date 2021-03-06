# Generated by Django 3.0.5 on 2020-06-30 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payrollsite', '0002_auto_20200630_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='installationrate',
            name='employee_id',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.PROTECT, to='payrollsite.Employee'),
        ),
        migrations.AlterField(
            model_name='installationrate',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
