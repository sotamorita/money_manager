# Generated by Django 3.1.5 on 2021-03-04 05:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journalentryapp', '0002_auto_20210302_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentrymodel',
            name='cr_class',
            field=models.CharField(choices=[('assets', '資産'), ('liabilities', '負債'), ('equity', '純資産'), ('expenses', '費用'), ('revenue', '収益')], default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalentrymodel',
            name='dr_class',
            field=models.CharField(choices=[('assets', '資産'), ('liabilities', '負債'), ('equity', '純資産'), ('expenses', '費用'), ('revenue', '収益')], default='assets', max_length=30),
            preserve_default=False,
        ),
    ]
