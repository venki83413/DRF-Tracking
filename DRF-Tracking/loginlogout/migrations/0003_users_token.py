from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginlogout', '0002_users_iflogged'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='token',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
