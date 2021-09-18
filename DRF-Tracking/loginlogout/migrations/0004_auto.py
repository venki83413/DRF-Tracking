from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginlogout', '0003_users_token'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
