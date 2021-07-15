from django.db import models
from django.db import migrations, models  

# Create your models here.

class register(models.Model):  
    id      = models.CharField(max_length=20)  
    fname    = models.CharField(max_length=100)
    lname    = models.CharField(max_length=100)  
    password = models.CharField(max_length=15)
    email    = models.CharField(max_length=100)  
    class Meta:  
        db_table = "user"  


class Migration(migrations.Migration):  
    initial = True  
    dependencies = [  
    ]  
    operations = [  
        migrations.CreateModel(  
            name='register',  
            fields=[  
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  
                ('fname', models.CharField(max_length=100)),  
                ('lname', models.CharField(max_length=100)),  
                ('email', models.CharField(max_length=15)),  
            ],  
            options={  
                'db_table': 'user',  
            },  
        ),  
    ]  