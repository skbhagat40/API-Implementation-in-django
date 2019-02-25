# Generated by Django 2.1.4 on 2019-01-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('opens', models.FloatField()),
                ('closes', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]