from django.db import models
import uuid
def upload_to(instance,filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/'.join([str(instance.titre),filename])
# Create your models here.
class Cour(models.Model):
    titre=models.CharField(max_length=50,null=True,blank=True)
    intro=models.TextField(blank = True)
    img=models.ImageField(null=True , blank=True)
class Part(models.Model):
    cour=models.ForeignKey(Cour,on_delete=models.CASCADE,null=True , blank=True)
    titre=models.CharField(max_length=50,null=True,blank=True)
    content=models.TextField(blank = True)
    img=models.ImageField(upload_to =upload_to,null=True , blank=True)
    code=models.TextField(blank = True)
