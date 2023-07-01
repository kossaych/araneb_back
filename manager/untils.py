# calculer l'age d'un lapin retourner le nombre de jour a partir du date de naissance (str!!) il retourne un entier
from datetime import date ,datetime
from django.utils import timezone
#import pandas as pd


def age(naissance):
        """ naissance=str(naissance)
        année_naissance =int(naissance[:naissance.index('-')])
        month_naissance =int(naissance[naissance.index('-')+1:naissance.index('-',naissance.index('-')+1)])
        jour =int(naissance[naissance.index('-',naissance.index('-',naissance.index('-')+1))+1:])
        today = timezone.now() 
        nb_months=today.month-month_naissance # nombre des months
        jours_month=0 # le nombre des jours correspondant au nombre des months
        if nb_months>0:
            for month in range(month_naissance,today.month):
                if month in [1,3,5,7,8,10,12]:
                    jours_month=jours_month+31
                elif month in [4,6,5,9,8,10,11]  :
                    jours_month=jours_month+30
                else:    
                    if (année_naissance%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if année_naissance%400==0:
                                jours_month=jours_month+29
                            else:
                                jours_month=jours_month+28
                    else:
                            if année_naissance%4==0:
                                jours_month=jours_month+29
                            else:
                                jours_month=jours_month+28
        elif nb_months<0:
            for month in range(month_naissance,today.month,-1):
                if month in [1,3,5,7,8,10,12]:
                    jours_month=jours_month-31
                elif month in [4,6,5,9,8,10,11]  :
                    jours_month=jours_month-30
                else :
                    if (année_naissance%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                        if année_naissance%400==0:
                            jours_month=jours_month-29
                        else:
                            jours_month=jours_month-28
                    else:
                        if année_naissance%4==0:
                            jours_month=jours_month-29
                        else:
                            jours_month=jours_month-28
        nb_anné=today.year-année_naissance  # nombre des annés
        jours_anné=0 # le nombre des  jours correspondant au nombre des annés
        if nb_anné>0:
            for année in range(année_naissance,today.year):
                    if (année%1000)%100==0:  # si le disaine et l'unité de nobre de l'anné est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier année bissextile qabissa)
                        if année%400==0:
                            jours_anné=jours_anné+366
                        else:
                            jours_anné=jours_anné+365
                    else:
                        if année%4==0:
                            jours_anné=jours_anné+366
                        else:
                            jours_anné=jours_anné+365
        elif nb_anné<0:
            for année in range(année_naissance,today.year,-1):
                    if (année%1000)%100==0:  # si le disaine et l'unité de nobre de l'anné est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier année bissextile qabissa)
                        if année%400==0:
                            jours_anné=jours_anné-366
                        else:
                            jours_anné=jours_anné-365
                    else:
                        if année%4==0:
                            jours_anné=jours_anné-366
                        else:
                            jours_anné=jours_anné-365 
        age = jours_anné+jours_month+ (today.day - jour)
        return  age """
        str_d1 = str(naissance)
        aujourdhui_date=str(date.today())
        
        try:
            d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        except:
            str_d1 = str_d1[:str_d1.find(" ")] # sa por séparer le date et l'heure
            d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(aujourdhui_date, "%Y-%m-%d")
        age = str(d2 - d1)
        try :    
            age=int(age[:age.index('d')])
        except:
            age=0
        return  age

# retourner l'age en anné months et jours sous forme str a partir du date de naissance
def age_handler(naissance):
        """today=timezone.now()
                if age >=0:
                    #for an in range(today.year-(age//365),today.year):
                    nb_anné=0
                    while (age>=365):
                        if (today.year-nb_anné%1000)%100==0:  # si le disaine et l'unité de nobre de l'anné est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier année bissextile qabissa)
                            if today.year-nb_anné%400==0:
                                age-=366
                            else:
                                age-=365
                        else:
                            if today.year-nb_anné%4==0:
                                age-=366
                            else:
                                age-=365
                        nb_anné+=1        
                    #nb_months=age


                    nb_months=0
                    while (age>=30):
                        if today.month-nb_months in [1,3,5,7,8,10,12]:
                            age-=31
                        elif today.month-nb_months in [4,6,5,9,8,10,11]  :
                            age-=30
                        else:    
                            if (today.year-nb_anné%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                    if today.year-nb_anné %400==0:
                                        age-=29
                                    else:
                                        age-=28
                            else:
                                    if today.year-nb_anné %4==0:
                                        age-=29
                                    else:
                                        age-=28
                        nb_months+=1        
                    
                return str(nb_anné)+" ans "+str(nb_months)+" months "+str(age)+" jours "  
        """

        str_d1 = str(naissance)
        aujourdhui_date=str(date.today())
        d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(aujourdhui_date, "%Y-%m-%d")
        age=str(d2-d1)
        try :    
            age=(age[:age.index('d')])+" j"
        except:
            age="0 j"
        return str(age)     

# retourner une liste contenant les dates succésivement a partir du intial_date jusqu'a final_date
def list_dates(initial_date,final_date):

    initial_date=datetime.strptime(initial_date, "%Y-%m-%d")
    final_date=datetime.strptime(final_date, "%Y-%m-%d")
    initial_year=int(initial_date.year)
    final_year=int(final_date.year)
    for year in range(initial_year,final_year+1):
            initial_month=1
            final_month=12
            if year == final_year :
                final_month=final_date.month
            if year == initial_year:
                initial_month=initial_date.month
                 
            for month in range(initial_month,final_month+1):
                if month in [4,6,9,11]:
                                initial_day =1
                                final_day = 30
                                if year == final_year and month == final_month  :
                                    final_day =final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 

                                for jour in range(initial_day,final_day+1):
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    
                                    if month in [4,6,9]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)

                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    yield date
                                    
                elif month in [1,3,5,7,8,10,12]:   
                                initial_day =1
                                final_day = 31
                                if year == final_year and month == final_month  :
                                    final_day =final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    if month in [1,3,5,7,8]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    yield date                                   
                                    
                if month == 2 :
                    if (year %1000)%100==0:  # si le disaine et l'unité de l'nannée  est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                            if year % 400 == 0:
                                initial_day =1
                                final_day = 29
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    yield date                                   
                                    
                            else:
                                initial_day =1
                                final_day = 28
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    month_date=str(month)
                                    jour_date=str(jour)
                                     
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    yield date                                   
                                    
                    else:
                            if year %4==0:
                                initial_day =1
                                final_day = 29
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    month_date=str(month)
                                    jour_date=str(jour)
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    yield date                                   
                                                                
                                    
                            else:
                                initial_day =1
                                final_day = 28
                                if year == final_year and month == final_month  :
                                    final_day = final_date.day 
                                if year == initial_year and month == initial_month:
                                    initial_day =initial_date.day 
                                for jour in range(initial_day,final_day+1):
                                    month_date=str(month)
                                    jour_date=str(jour)
                                     
                                    if month in [2]:
                                        month_date="0"+str(month)
                                    if jour in [1,2,3,4,5,6,7,8,9]:
                                        jour_date="0"+str(jour)
                                    date=str(year)+"-"+(month_date)+"-"+(jour_date)    
                                    yield date        


def age_revers(age_jours):
        if age_jours >= 364 :
            for an in range((timezone.now().year-(age_jours//365))-1,(timezone.now().year-(age_jours//365))+1):
                for month in range(1,13):                       
                                if month in [4,6,9,11]:
                                                for jour in range(1,31):
                                                    if age(str(an)+"-"+str(month)+"-"+str(jour)) == age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                                
                                elif month in [1,3,5,7,8,10,12]:   
                                                for jour in range(1,32):
                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                                                              
                                if month == 2 :
                                    if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                            if an%400==0:
                                                for jour in range(1,30):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                              
                                            else:
                                                for jour in range(1,29):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                               
                                    else:
                                            if an%4==0:
                                                for jour in range(1,30):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                            
                                            else:
                                                for jour in range(1,29):

                                                    if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                        date=str(an)+"-"+str(month)+"-"+str(jour)
                                                        if len(str(month))==1 and len(str(jour))==1:
                                                            date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                        else :    
                                                            if len(str(month))==1:
                                                                date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                            if len(str(jour))==1:
                                                                date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                        
                                                        return date                                     
        else:      
            if (int(age(str(timezone.now().year)+"-01-01"))>=age_jours):#pour assurer que les dates doit  etre dans cette anné
                    an = timezone.now().year   
            else:
                    an = timezone.now().year-1                   
            for month in range(1,13):                       
                            if month in [4,6,9,11]:
                                            for jour in range(1,31):
                                                if age(str(an)+"-"+str(month)+"-"+str(jour)) == age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                                
                            elif month in [1,3,5,7,8,10,12]:   
                                            for jour in range(1,32):
                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                                                              
                            if month == 2 :
                                if (an%1000)%100==0:  # si le disaine et l'unité de nobre de l'nannée_naissancené est null on virifier avec la division sur 400 sinon sur 4 (règle pour virifier nannée_naissancenée bissextile qabissa)
                                        if an%400==0:
                                            for jour in range(1,30):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                              
                                        else:
                                            for jour in range(1,29):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                               
                                else:
                                        if an%4==0:
                                            for jour in range(1,30):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                            
                                        else:
                                            for jour in range(1,29):

                                                if age(str(an)+"-"+str(month)+"-"+str(jour))==age_jours:
                                                    date=str(an)+"-"+str(month)+"-"+str(jour)
                                                    if len(str(month))==1 and len(str(jour))==1:
                                                        date=str(an)+"-0"+str(month)+'-0'+str(jour)
                                                    else :    
                                                        if len(str(month))==1:
                                                            date=str(an)+"-0"+str(month)+"-"+str(jour)
                                                        if len(str(jour))==1:
                                                            date=str(an)+"-"+str(month)+"-0"+str(jour)
                                                    
                                                    return date                                     






# serializing data
class Serializer:
    """
    aClsse Serializer pour la sérialisation personnalisée des objets.

    Cette classe permet de sérialiser des objets en utilisant différentes configurations de champs.

    Usage:
        serializer = Serializer(data, **fields)
        serialized_data = serializer.serialize()

    Arguments:
        data (queryset object ou list[object]): L'objet ou la liste d'objets à sérialiser.
        **fields (dict): Les champs (colunms) de tableau de l'objet dans la base de données à inclure dans la sérialisation.
        chaque field est un dict contien une seule valeur (key:'value') le key represente le non du champ retourné par la fonction serilaze et value represente le non du champ dans le class model de l'objet sa sert pour get la data 
        la valeur peut etre de différente type (chaque type représente un champ {field} speciale ) :
                *string : ce string représente un champ (field) dans le class model de l'objet passé , un champ non relationelle (il ne represente pas une relation avec un autre model) quelque soit un date un string un int ...
                ou un champ de relation mais les données retournées ne serent pas un objet contient des données de l'autre objet relié le valeur retourné sera une valeur primitive (string date int floot bool ... qui represente l'objet relié , et cette valeur précise par la fonction __str__ du class model de l'objet relié) 
                en tout les cas tu n'aura pas un objet tu aura une valeur primitive (string int floot bool date ...)
                
                *tuple : (le tuple doit contient seule  une valeur len = 1) la fonction comprent le tuple que tu veux les données dans le tuples reste la meme et elle ne s'effectue aucune traitement sur les données donc les données mait dans un tuple quel que soit son type (dict list string int floor bool ...)  n'est pas un field d'un objet dans la base de données elles sont des données statiques

                *dict : le dict ne represente pas un fields dans le class model de l'objet il represente une method dans le class model de l'objet
                et il contient des informations sur la fonction le non de fonction 
                les valeurs des params de la fonction ( sous la forme d'une liste ou cas ou la fonction n'a pas des params on passe une liste vide )
                et les champ demandé ou cas ou la fonction retourne un objet du base de données (optionell sous la forme d'un dict contien des key value represente les nom des champ et ces valeur)
                    
                
                * SerializerRelatedFieldRelationKeyInObject : se type est un class représente un champ de relation dans l'objet et il contient le model relié a travers ce champ et les champ demandé 
             
                * SerializerRelatedFieldRelationkeyInRelatedObject : se type est un class represente un champ de relation sité dans un autre model relié a l'objet 

                il contient le nom du model qui contient le champ de relation , le nom de champ de relation (relié a l'objet) ,filtres (dict qui contient key : le nom du champ et value : la valeur pour effectuer des filtre )
                et les champ demandé de les objet relié 

    Méthodes:
        serialize() : Sérialise les objets en utilisant les champs spécifiés.

    Méthodes statiques:
        is_iterable(obj): Vérifie si l'objet est itérable.
        get_default_fields(obj): Récupère les champs par défaut depuis l'objet.
        handle_dictionary_value(obj, value): Gère une valeur de type dictionnaire.
        handle_tuple_value(value): Gère une valeur de type tuple.
        handle_basic_type(obj, value): Gère une valeur de type basique.
        handle_serializer_related_field_in_instance(obj, value): Gère un champ de relation dans l'objet.
        handle_serializer_related_field_in_related_object(obj, value): Gère un champ de relation dans l'objet lié.
        is_dict(obj): Vérifie si l'objet est un dictionnaire.
        is_tuple(obj): Vérifie si l'objet est un tuple.
        is_basic_type(obj): Vérifie si l'objet est d'un type basique.
        is_serializer_related_field_relation_key_in_object_instance(obj): Vérifie si l'objet est une clé de relation de champ de sérialiseur dans l'objet.
        is_serializer_related_field_relation_key_in_related_object(obj): Vérifie si l'objet est une clé de relation de champ de sérialiseur dans l'objet lié.

    Exemple:

    ```python
    # Créer un objet MyObject
    my_object = MyObject(field1='valeur1', field2='valeur2')

    # Définir les champs pour la sérialisation
    fields = {
        'field1': 'field1',  # Champ basique
        'field2': ('field2',),  # Champ tuple


        'field3': {
            'function': 'custom_function',  # Champ dictionnaire avec une fonction personnalisée
            'params': [my_object.field1],
            'fields': {'nested_field': 'nested_field'}  # Champs imbriqués dans le dictionnaire
        },


        'field4': SerializerRelatedFieldRelationKeyInObject(related_field='related_field'),  # Champ de relation dans l'objet
        
        'field5': SerializerRelatedFieldRelationkeyInRelatedObject(
            object_model=RelatedModel,
            related_field='related_field',
            filters={'filter_field': 'filter_value'},
            related_field_fields={'related_field1': 'related_field1', 'related_field2': 'related_field2'}
        )  # Champ de relation dans l'objet lié
    }

    # Instancier la classe Serializer et appeler la méthode serialize()
    serializer = Serializer(my_object, **fields)
    serialized_data = serializer.serialize()

    print(serialized_data)
    ```

    """
    def __init__(self, data, **fields):
        """
        Initializes the Serializer with data and fields.
        :param data: The data to be serialized.
        :param fields: Optional field specifications for serialization.
        """
        self.data = data
        self.fields = fields
        self.json_data = []

    def serialize(self):
        """
        Serializes the data based on the specified fields.
        :return: The serialized JSON data.
        """

        if not self.is_iterable(self.data):
            self.data = [self.data]

        for obj in self.data:            
            json_object = {}
            
            # préciser les champs demander
            if self.fields == {}:
                selected_fields = self.get_default_fields(obj)
            else:
                selected_fields = self.fields.items()

            for field_name, field_config in selected_fields:

                if   self.is_dict(field_config):
                     json_object[field_name] = self.handle_dictionary_value(obj, field_config)         
                elif self.is_tuple(field_config):
                     json_object[field_name] = self.handle_tuple_value(field_config)
                elif self.is_basic_type(field_config):
                     json_object[field_name] = self.handle_basic_type(obj, field_config)
                elif self.is_related_field_in_object_instance(field_config):
                     json_object[field_name] = self.handle_related_field_in_instance(obj, field_config)
                elif self.is_related_field_in_related_object(field_config):
                     json_object[field_name] = self.handle_related_field_in_related_object(obj, field_config)

            self.json_data.append(json_object)

        if len(self.json_data) == 1 :
            return self.json_data[0]     
        return self.json_data

    @staticmethod
    def is_iterable(obj):
        """
        Checks if the object is iterable.
        :param obj: The object to check.
        :return: True if the object is iterable, False otherwise.
        """
        try:
            iter(obj)
            return True
        except TypeError:
            return False

    @staticmethod
    def get_default_fields(obj):
        """
        Retrieves the default fields from the object.
        :param obj: The object.
        :return: The default fields as a dictionary.
        """
        return {field.name: field.name for field in obj._meta.fields}.items()

    def handle_dictionary_value(self, obj, field_config):
        """
        Handles a dictionary value in the field configuration.
        :param obj: The object.
        :param field_config: The dictionary value in the field configuration.
        :return: The serialized value.
        """
        function_name = field_config.get('function')
        if function_name and hasattr(obj, function_name) and callable(getattr(obj, function_name)):
            function = getattr(obj, function_name)
            if self.is_basic_type(function(*field_config['params'])):
                return function(*field_config['params'])
            else:
                serializer = Serializer(function(*field_config['params']), **field_config['fields'])
                return serializer.serialize()
        return None

    @staticmethod
    def is_tuple(obj):
        """
        Checks if the object is a tuple.
        :param obj: The object to check.
        :return: True if the object is a tuple, False otherwise.
        """
        return isinstance(obj, tuple)

    @staticmethod
    def handle_tuple_value(field_config):
        """
        Handles a tuple value in the field configuration.
        :param field_config: The tuple value in the field configuration.
        :return: The serialized value.
        """
        return field_config[0]

    @staticmethod
    def is_basic_type(obj):
        """
        Checks if the object is a basic type (int, float, str, bool).
        :param obj: The object to check.
        :return: True if the object is a basic type, False otherwise.
        """
        basic_types = (int, float, str, bool)
        return isinstance(obj, basic_types)

    @staticmethod
    def handle_basic_type(obj, field_config):
        """
        Handles a basic type value in the field configuration.
        :param obj: The object.
        :param field_config: The basic type value in the field configuration.
        :return: The serialized value.
        """
        return str(getattr(obj, str(field_config)))

    @staticmethod
    def is_related_field_in_object_instance(obj):
        """
        Checks if the object is a SerializerRelatedFieldRelationKeyInObject instance.
        :param obj: The object to check.
        :return: True if the object is a SerializerRelatedFieldRelationKeyInObject, False otherwise.
        """
        return isinstance(obj, SerializerRelatedFieldRelationKeyInObject)

    def handle_related_field_in_instance(self, obj, field_config):
        """
        Handles a related field in the object instance.
        :param obj: The object.
        :param field_config: The related field configuration.
        :return: The serialized value.
        """
        related_object = getattr(obj, field_config.related_field)
        serializer = Serializer(related_object, **field_config.get_related_field_fields())
        return serializer.serialize()

    @staticmethod
    def is_related_field_in_related_object(obj):
        """
        Checks if the object is a SerializerRelatedFieldRelationkeyInRelatedObject instance.
        :param obj: The object to check.
        :return: True if the object is a SerializerRelatedFieldRelationkeyInRelatedObject, False otherwise.
        """
        return isinstance(obj, SerializerRelatedFieldRelationkeyInRelatedObject)

    def handle_related_field_in_related_object(self, obj, field_config):
        """
        Handles a related field in the related object.
        :param obj: The object.
        :param field_config: The related field configuration.
        :return: The serialized value.
        """
        related_object = field_config.object_model.objects.filter(
            **{field_config.related_field: obj},
            **field_config.get_filters()
        )
        serializer = Serializer(related_object, **field_config.related_field_fields)
        return serializer.serialize()

    @staticmethod
    def is_dict(obj):
        """
        Checks if the object is a dictionary.
        :param obj: The object to check.
        :return: True if the object is a dictionary, False otherwise.
        """
        return isinstance(obj, dict)


class SerializerRelatedFieldRelationKeyInObject:
    def __init__(self, related_field, **related_field_fields):
        """
        Initializes a related field in the object instance.
        :param related_field: The name of the related field.
        :param related_field_fields: Optional field specifications for serialization.
        """
        self.related_field = related_field
        self.related_field_fields = related_field_fields

    def get_related_field_fields(self):
        """
        Retrieves the field specifications for the related field.
        :return: The field specifications.
        """
        return {**self.related_field_fields}


class SerializerRelatedFieldRelationkeyInRelatedObject:
    def __init__(self, related_field, object_model, filters, **related_field_fields):
        """
        Initializes a related field in the related object.
        :param related_field: The name of the related field.
        :param object_model: The related object model.
        :param filters: Optional filters to apply when querying the related object.
        :param related_field_fields: Optional field specifications for serialization.
        """
        self.related_field = related_field
        self.object_model = object_model
        self.filters = filters
        self.related_field_fields = related_field_fields

    def get_filters(self):
        """
        Retrieves the filters for querying the related object.
        :return: The filters.
        """
        return {str(k): v for d in self.filters for k, v in d.items()}


# images proccesing 
from PIL import Image

class ImageProcessor:
    def verify_image(self, image):
        try:
            img = Image.open(image)
            img.verify()
            return True
        except (IOError, SyntaxError) as e:
            return False

    def resize_image(self, image_path, width, height):
        basewidth = width
        baseheight = height

        # Open the image using Pillow
        img = Image.open(image_path)

        # Calculate the aspect ratio
        aspect_ratio = img.size[0] / img.size[1]

        # Calculate the new height while maintaining the aspect ratio
        hsize = int(basewidth / aspect_ratio)

        # Resize the image using Lanczos resampling algorithm
        resized_img = img.resize((basewidth, hsize), Image.LANCZOS)

        # Crop the image to the desired height
        left = 0
        top = (hsize - baseheight) // 2
        right = basewidth
        bottom = top + baseheight
        cropped_img = resized_img.crop((left, top, right, bottom))

        # Save the resized and cropped image back to the same location
        cropped_img.save(image_path, optimize=True)










