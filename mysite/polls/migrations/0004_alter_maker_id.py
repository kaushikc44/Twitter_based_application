# Generated by Django 3.2.5 on 2022-04-14 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_maker_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maker',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
