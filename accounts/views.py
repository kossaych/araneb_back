from .models import*
from manager.models import*
from .models import*
from .serializers import*
from django.contrib.auth import authenticate
from django.utils import timezone
import random
import string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import hashlib
# fonction genere un code de virification pour l'envoiyer au l'email
def generate_code():
    code=''
    letters=string.ascii_lowercase+string.digits
    for i in range(8):
        code=code+random.choice(letters)
    return code  
# virifier l'existance d'un email dans la base de donné
def verif_email(email):
    for user in User.objects.all() :
        if email == user.email :
            return True
    return False          
def have_code(user):
    for code in CodeVirif.objects.all():
        if code.username == user : 
            return True
    return False        
# virifier la validité du password
def check_password(password):
    if password != "":
        digits=0
        letters=0
        carecters=0
        for letter in password :
            if letter in string.digits:
                digits=digits+1
            elif letter in string.ascii_letters:
                letters=letters+1
            else :
                carecters=carecters+1    

        if len(password) < 8 or digits<3 or letters<3 or carecters<2:
                return False
        return True 
# virifier la validité du last_name
def check_last_name_or_first_name(name):
        if len(name) < 3 :
            return False
        for letter in name :
            if letter in string.ascii_uppercase :
                return False
            if letter in string.digits :
                return False
            elif letter == " ":
                return False
            elif letter in string.punctuation:
                return False
        return True 
# virifier la validité du code au raport du temps 
def check_code_time(created_at):
        year=created_at.year
        month=created_at.month
        day=created_at.day
        hour=created_at.hour
        minute=created_at.minute
        if year == timezone.now().year:
            if month == timezone.now().month:
                if day == timezone.now().day:
                    if hour == timezone.now().hour:
                        if (timezone.now().minute-minute)<=3: 
                            return True 
                    elif hour == timezone.now().hour+1:# for minutes between 2 hours
                        if (timezone.now().minute)<=3 and minute>=57 and (60-minute)+timezone.now().minute <= 3: 
                            return True 
        return False
class RegisterView(APIView):
    ######################deux fonction pour asurer la generation des nevaux username#############
    def virif_user_number(self,first,last,number):
        users=User.objects.filter(first_name=first,last_name=last)
        for user in users:
                if int(user.username[user.username.index("_")+1:])==number:
                    return False
        return True            
    def generate_username(self,first,last):
        username=first+"-"+last
        for i in range(1,len(User.objects.filter(first_name=first,last_name=last))+1):
                if self.virif_user_number(first,last,i):
                    return username+"_"+str(i)
        return username+"_"+str(len(User.objects.filter(first_name=first,last_name=last))+1)
    ###############################################################################################
    def post(self,request):
            email=request.data.get('email')
            password1=request.data.get('password1')
            password2=request.data.get('password2')
            first_name=request.data.get('first_name').strip()
            last_name=request.data.get('last_name').strip()
            if check_password(password1) and password1 == password2:
                if check_last_name_or_first_name(first_name):
                    if check_last_name_or_first_name(last_name):
                        if  verif_email(email):
                            user=User.objects.get(email=email)
                            if not user.is_active:
                                user.delete()
                            else :
                                return Response('this email is alredy used try with an author email',status=status.HTTP_400_BAD_REQUEST)      
                        username=self.generate_username(first_name,last_name).strip()
                        user=User(first_name=first_name,last_name=last_name,username =username, email=email,password=password1,is_active=False)
                        user.save() 


                        code=generate_code()  
                        CodeVirif.objects.filter(username=user).delete  
                        code_hashed = hashlib.md5() 
                        code_hashed.update(code.encode('utf-8'))
                        CodeVirif.objects.create(username=user,code=code_hashed.hexdigest(),created_at=timezone.now())  
                        email = EmailMessage('Activate your account.',code, to=[request.data.get('email')])
                        email.send()


                                                     
                        return Response('Please confirm your email address to complete the registration',status=status.HTTP_200_OK)
                    else: return Response('invalid last name',status.HTTP_400_BAD_REQUEST)    
                else: return Response('invalid first name',status.HTTP_400_BAD_REQUEST)    
            else: return Response('invalid password',status.HTTP_400_BAD_REQUEST)    
class ActivateUser(APIView):
    def post(self,request):
                email = request.data.get('email')
                code = request.data.get('code')
                if verif_email(email): 
                    user=User.objects.get(email=email)
                    if have_code(user):   
                            code_registed=CodeVirif.objects.get(username=User.objects.get(email=email))                 
                            code_hashed = hashlib.md5() 
                            code_hashed.update(code.encode('utf-8'))
                            if code_hashed.hexdigest() == code_registed.code :
                                if check_code_time(code_registed.created_at):
                                    code_registed.delete()
                                    user=User.objects.get(username=user.username)
                                    user.is_active=True
                                    user.save()
                                    return Response(Token.objects.get(user=user).key,status=status.HTTP_200_OK)
                                else:return Response('invalid code time',status=status.HTTP_400_BAD_REQUEST)
                            else:return Response('False code',status=status.HTTP_400_BAD_REQUEST)
                    else:return Response('code not sended for your email',status=status.HTTP_400_BAD_REQUEST)
                else:return Response('user not registed',status=status.HTTP_400_BAD_REQUEST)
class Login(APIView):       
    def post(self,request):
        email=request.data.get('email')
        if verif_email(email):
            username=User.objects.get(email=request.data.get('email'))
            password = request.data['password']
            user = authenticate(username=username,password=password)#authenticate return the username of user
            if user is not None: 
                if user.is_active:
                    return Response(Token.objects.get(user=user).key,status=status.HTTP_200_OK)
                else :return Response('account not active',status=status.HTTP_400_BAD_REQUEST)
            else :return Response('false data',status=status.HTTP_400_BAD_REQUEST) 
        else:return Response('email not regested',status=status.HTTP_400_BAD_REQUEST)    
class ResetPassword(APIView):
    def post(self,request):
        email=request.data['email']
        if verif_email(email) :
            user=User.objects.get(email=email)
            code=generate_code()  
            code_hashed = hashlib.md5() 
            code_hashed.update(code.encode('utf-8'))
            CodeVirif.objects.filter(username=user).delete()
            CodeVirif.objects.create(username=user,code=code_hashed.hexdigest(),created_at=timezone.now())  
            email = EmailMessage(
                'Reset password', 
                code,
                to=[request.data.get('email')])
            email.send()
            return Response('check your email',status=status.HTTP_200_OK)
        return Response('email not registed',status=status.HTTP_400_BAD_REQUEST)    
class CheckCode(APIView):    
    def post(self,request):
        email = request.data.get('email')
        code = request.data.get('code')
        code_hashed = hashlib.md5() 
        code_hashed.update(code.encode('utf-8'))
        if verif_email(email):
            user = User.objects.get(email=email)
            if have_code(user):
                code_registed=CodeVirif.objects.get(username=user.id) 
                if code_hashed.hexdigest() == code_registed.code:
                        if check_code_time(code_registed.created_at):
                            return Response(True,status=status.HTTP_200_OK)
                        else : return Response('invalid code time',status=status.HTTP_400_BAD_REQUEST)
                else :return Response('False code',status=status.HTTP_400_BAD_REQUEST)
            else :return Response("code not sended to your email",status=status.HTTP_400_BAD_REQUEST)
        else:return Response('user not found',status=status.HTTP_400_BAD_REQUEST) 
class SetPassword(APIView):
    def post(self,request):
        email = request.data.get('email')
        code = request.data.get('code')
        code_hashed = hashlib.md5() 
        code_hashed.update(code.encode('utf-8'))
        new_password=request.data.get('password')
        if verif_email(email):
            user = User.objects.get(email=email)
            if have_code(user):
                code_registed=CodeVirif.objects.get(username=user.id)
                if code_hashed.hexdigest() == code_registed.code:
                    if check_code_time(code_registed.created_at):
                        if check_password(request.data.get('password')) == True:
                            code_registed.delete()
                            user.set_password(new_password)
                            user.save()
                            #pour activer les user not active
                            user.is_active=True
                            user.save()
                            return Response(Token.objects.get(user=user).key,status=status.HTTP_200_OK)
                        else :return Response('invalid new password',status=status.HTTP_400_BAD_REQUEST)
                    else : return Response('invalid code time',status=status.HTTP_400_BAD_REQUEST)
                else :return Response('False code',status=status.HTTP_400_BAD_REQUEST)
            else :return Response("code not sended to your email",status=status.HTTP_400_BAD_REQUEST)
        else:return Response('user not registed',status=status.HTTP_400_BAD_REQUEST)
class ChangePassword(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        old_password=request.data.get('old_password')
        new_password1=request.data.get('password1')
        new_password2=request.data.get('password2')
        user=authenticate(password=old_password,username=request.user.username)
        if user != None:
                    if check_password(new_password1) and new_password1 == new_password2 :
                            user.set_password(new_password1)
                            user.save()
                            return Response(status=status.HTTP_200_OK)  
                    else :return Response('invalid new password',status.HTTP_400_BAD_REQUEST)
        else :return Response('user not found',status.HTTP_400_BAD_REQUEST)                           
