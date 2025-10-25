from django.db import migrations, models
# CRUCIAL FIX: Import settings here so the migration file knows what it is.
from django.conf import settings 


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        # This RemoveField operation was deleted because the underlying 
        # database table never existed, causing the previous OperationalError.
        # It is now just removed to prevent issues.

        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(
                blank=True, 
                # Use settings.AUTH_USER_MODEL, which is now properly imported
                related_name='followers', 
                to=settings.AUTH_USER_MODEL 
            ),
        ),
    ]
