from django.db import models

# Create your models here.


class Costomer(models.Model):
    company_name =  models.CharField(max_length=50)
    robot_page   = models.CharField(max_length=250)
    robot_key    = models.CharField(max_length=100)
    contact =  models.CharField(max_length=20);
    contact_title = models.CharField(max_length=30);
    tel = models.CharField(max_length=20);
    mobile = models.CharField(max_length=15);
    fax = models.CharField(max_length=20);
    address = models.CharField(max_length=100);
    post_code = models.CharField(max_length=10);
    website = models.CharField(max_length=100);
    create_time = models.DateTimeField('date')
    update_time =  models.DateTimeField('date')
    def __unicode__(self):
        return self.company_name
    class Meta:
        db_table = 'costomer'