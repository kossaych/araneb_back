from django.db import models
from accounts.models import User
from django.utils import timezone
import uuid
def upload_to(instance,filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return '/'.join([str(instance.cage),filename])
class Malle(models.Model):
    LAPIN_RACES=(
        ('Gaint Flander','Gaint Flander'),
        ('Flemish Giant','Flemish Giant'),
        ('Chinchilla','Chinchilla'),
        ('New Zealand White','New Zealand White'),
        ('California','California'),
        ('Rex','Rex')
        )
    create_at=models.DateField(default=timezone.now)
    img=models.ImageField(upload_to =upload_to,null=True , blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True , blank=True)
    race=models.CharField(choices=LAPIN_RACES ,max_length=200,default='California')
    date_naissance=models.DateField(default=timezone.now)
    state=models.CharField(max_length=50, default='production',choices=[("femalle","femalle"),("mort","mort"),("vendue","vendue"),("production","production")])
    cage=models.CharField(null=True,blank=True,max_length=50)
    date_mort=models.DateField(null=True,blank=True)
    #cause_mort=models.CharField(choices=CAUSE_MORT_LAPIN ,max_length=200,null=True , blank=True)
    prix=models.IntegerField(null=True,blank=True)
    date_vent=models.DateField(null=True,blank=True)
    def __str__(self):
        return str(self.cage)
class Femalle(models.Model):
    LAPIN_RACES=(
        ('Gaint Flander','Gaint Flander'),
        ('Flemish Giant','Flemish Giant'),
        ('Chinchilla','Chinchilla'),
        ('New Zealand White','New Zealand White'),
        ('California','California'),
        ('Rex','Rex')
        )
    create_at=models.DateField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE ,null=True,blank=True)
    cage=models.CharField(max_length=50,null=True,blank=True)
    race=models.CharField(choices=LAPIN_RACES ,max_length=200,null=True,blank=True)
    date_naissance=models.DateField(default=timezone.now)
    state=models.CharField(max_length=50, default='production',choices=[("mort","mort"),("vendue","vendue"),("production","production")])
    date_mort=models.DateField(null=True,blank=True)
    prix=models.IntegerField(null=True,blank=True)
    date_vent=models.DateField(null=True,blank=True)  
    def __str__(self):
        return str(self.cage)

class FemalleStatistique(models.Model):
    date_debut=models.DateField(null=True,blank=True)
    date_fin=models.DateField(null=True,blank=True)
    femalle=models.DateField(null=True,blank=True)
    #infos
    TP=models.IntegerField(null=True,blank=True)
    TM=models.IntegerField(null=True,blank=True)
    TMN=models.IntegerField(null=True,blank=True)
    TPnet=models.IntegerField(null=True,blank=True)
    TPf=models.IntegerField(null=True,blank=True)
    TMf=models.IntegerField(null=True,blank=True)
    TPnetf=models.IntegerField(null=True,blank=True)
    TPm=models.IntegerField(null=True,blank=True)
    TMm=models.IntegerField(null=True,blank=True)
    TPnetm=models.IntegerField(null=True,blank=True)
    TV=models.IntegerField(null=True,blank=True)
    TVm=models.IntegerField(null=True,blank=True)
    TVf=models.IntegerField(null=True,blank=True)
    grandprix=models.IntegerField(null=True,blank=True)
    basprix=models.IntegerField(null=True,blank=True)
    moyprix=models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    MPN=models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    MPS=models.DecimalField(max_digits=20, decimal_places=4,null=True,blank=True)
    TOPPS=models.IntegerField(null=True,blank=True)
    BASPS=models.IntegerField(null=True,blank=True)
    TOPPN=models.IntegerField(null=True,blank=True)
    BASPN=models.IntegerField(null=True,blank=True)
    cons=models.IntegerField(null=True,blank=True)

# liste des  poids des parents
class PoidMalle(models.Model):
    malle=models.ForeignKey(Malle,on_delete=models.CASCADE ,null=True , blank=True)
    date_mesure=models.DateField(null=True,blank=True)
    valeur=models.IntegerField(null=True,blank=True)
    

class PoidFemalle(models.Model):
    femalle=models.ForeignKey(Femalle,on_delete=models.CASCADE ,null=True , blank=True)
    date_mesure=models.DateField(null=True,blank=True)
    valeur=models.IntegerField(null=True,blank=True)    




