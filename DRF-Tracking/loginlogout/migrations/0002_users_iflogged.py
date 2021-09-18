from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginlogout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='ifLogged',
            field=models.BooleanField(default=False),
        ),
    ]
