#mehr 1403
#haji ma omadim social ro start zadim enshaa inam bezaram to git hub

#setting.py hasttim alan ->

#haji man miam file local_settings.py ijad miknm bara tanzimat dakhli khodm

#bad miam ino git ignore miknm dige ama ye file dige miazsam ke format nadare k age kasi khast az on estfade kne bara in project



# brim data base ro brim b postgresql

# pip install psycopg2 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': BASE_DIR / 'social_db',
        'USER':'social_admin',
        'PASSWORD':'1234',
        'HOST':'localhost',
        'PORT':'',
    }
}

#SQL SHELL 
password =1234

#CREATE DATABASE social_db;

#brim to database jdid
\c 

#ijad karbar
CREATE ROLE social_admin WITH LOGIN PASSWORD '1234';

#dadn dast resi b karbar az database 
GRANT ALL PROVILEGES ON ALL TABLES IN SCHEMA public TO social_admin

#اعمال تغیرات 
\q 



#دادن مالکیت یک پایگاه داده به یک یوزر دیگر

# ALTER DATABASE social_db OWNER TO social_admin;\
    
    
    
#in az database

# superuser ro misazam 



#################################################################################
# project 2 part 2 

#emroz ino ba ravesh jadid jolo mirim

#agha ma mikhayem user bznim pas register kardan va sath dastrsi on karbar bara ma mohme

#step1
 
# startapp accounts

#haji ma class profile ro mizanim bara in app ke tosh ye user dare az one to one rell dare va bara ine k ma baara har user ye prof dashte bashim . hala bejay inke az User django arsbari knim mizanim az conf import setting ro miarim to kar va setting.AUTH.USER.MODEL karo dar miarim
# on delete mizarimesh 
user - phone country avatar

# phone number ro big int mizanim  -> uniqe blank null = true mizanma k ejbari nabashe tekrari nabashe 

#step2
# to class badi country user ro migirim ba :
# name - abbr -created tim update time isactiva
#ye class meta darim bara verbos name ba db_table ke esme hashe khodt bezan mashti 
#MIN 21

#step 3 
# hamin counrty ke alan create kardim add miaznam to prfile  ba forekey   
ye avatar ham add miknm


#step 4
# class device
#agha inja model version harchi niaz hast az in kabar migiram ke beshe estfade kard


#step 5 brim app ro install to setting knim va migrate knim

#############################################################

#step 6 mirim soragh views ha  
#ba api mizanam 

#haji ma aval miam file serializers ro ijad miknim chon karmon ba api hast to views.py miam az restframework.views import miknm apiview ro k bara class ham estfade knm

#seralizer.py 
#aghaa inja man field hamo mikham jadid bznm masaln email-> khonb in bayad ye email bire va bayad chek knm k email uniqe bashe tekrari nabashe 

# mim az django.auth getusermodel ro imoprt miknm ye shey ijad miknm bahash hala midamesh be validator k az restframework import kardm requeire = true -> por kardan ejbari 
#yani chi?> email ejbari hast por kardanesh

#haji 2ta password migiram ba charfied
#username migiran 
# claas meta ijad miknm to in field haro migiram az class user khode djnango 
# mese fristname lastname 

#ye tabe validator ham miaznam bara :
# chek kardan password ke 2 bar pass ro dosrt vard karde ?


# ye tabebznim bara create 
    def create(self,validate_data):
        user = User.objects.create(#aln mire cearte mikne
            username = validate_data['username'],#aval chek mikne data username haro
            email = validate_data['email'],#data email ro
            first_name =  validate_data.get('first_name',''),#inja avale mire firstname ro migire bad chek mikne  
            last_name =  validate_data.get('last_name',''),  
            
        )\
            
    
#brim dige barash views.py bznim haji
# views.py 
#hatmn user ro be getusermodel pass midam ba genrics ham mikham api ro vard knm


class RegisterView(generics):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

#urls.py 
# haji brmi bznim dige in kari nadare 

#brim to postman test knim dastano
{
    "username": "amin",
    "email": "amin@gmail.com",
    "password_1":"amin123amin",
    "password_2":"amin123amin"
}

#agha to in url =>http://127.0.0.1:8000/api/register/
#GET 
# miknm json ro behesh midam test mikne hala chon email username ro ma uniqe dade bodim alan dige kamel test mishe aval validator anjam mishe age moshkel dasht error mide 


#haji brim login bznim bara in user ha ke dorostm mishe

Authentication =>احراز هویت
#sabtnam va  login kardan
#sakht yek system bara login va ehrazhoviat

Authorization = > مجوز
#dastresi be ghesmat ha  mesle post gozashtan 

#hatman inja ro chek kn kamel
# https://www.django-rest-framework.org/api-guide/authentication/

#ma alan mikhaym yadgiri JWT ro start bznim 
#hala jwt chie? haji ye tokene bara ehraz kardan va dadn mojavez hast hala bayad yad bgiri ke chtori be project ezafe knim va estfade knim 

#inja site amozesh hast 
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

#step1
# INSTALL 

pip install djangorestframework-simplejwt

#step 2
#add to setting.py

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

#step3
#GET token -> bara gereftan token az jwt niaz be view khodesh darim
#urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
#step 4
#INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]

#step 5
#runserver and start curl dar terminal
#bash ro baz kn

curl \
  -X POST \ # method 
  -H "Content-Type: application/json" \#header
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \#body
  http://localhost:8000/api/token/ #url 

#alan in dastor ro midi
{"detail":"No active account found with the given credentials"}
# in ro barmigardone

#hala brim hamin ro to postman ejra knim
#bala jolo har khat neveshtam bara chie vard kn oskol !
#toye body 
{
    "username": "social",
    "password": "123"
}
# ino ke vard kni
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODE0NTUxMCwiaWF0IjoxNzI4MDU5MTEwLCJqdGkiOiIxYzFhMjQxMGU0ZmE0MzU2ODMxNmE2NjhlZTIxMjMxOSIsInVzZXJfaWQiOjF9.39-P4r2SybIbvi3x6bQub5K0eyFwbTIsXrCBNAlPJVo",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4MDU5NDEwLCJpYXQiOjE3MjgwNTkxMTAsImp0aSI6ImIzOGQ5Y2UwZWQ2ZTQ1NWZiY2RhNGE2MGUzNzQyMzNiIiwidXNlcl9pZCI6MX0.u36fW9ck34gsPlBx2Da3kapSap9S6qq3SfFkKcD5izw"
}
#yedone access ye refresh migiri ke mishe token jwt ma
#az in be bad har api ke mikhay bgiri to hearder bayad in token access ro bedi ke mishe mojavez man to site

#hala in access expire mishe ma bayad to on yki url khodemon refresh ro bdim ke ye token dige bgirim
# mirim to postman url->
#   curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/token/refresh/


#miri to in url token refresh ro midi in behet ye accesss dige mide 
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4MDU5NjQzLCJpYXQiOjE3MjgwNTkxMTAsImp0aSI6IjAzNGFmOTlhNDVkYzRkNjBiNGUzZDkyY2QwNDEwMzdiIiwidXNlcl9pZCI6MX0.qijWuGEQxa14UUVExccaxoSXGVWcH-bEPwBawfdPrPI"
}

#hala to hamon site simpel jwt ye khat code daraim bara setting.py project khodemone mitonam addd knim tanzimat defalt jwt ro taghir bedim 
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
}
#masaln timedelata 5min expire token access ma hast !

#haji kolan in bara ine man 100 bar niam login konam userpass bedam 
#masaln didi miri to blubank age 2min az app biron bashi beri tosh login nmikhad vali 10 min beshe login bayad kni ine bara injor jaha hast hala acc aparat jaye 10 min 10day mizaran chon hasas nist   


###########################################################
#PROJECT PART 4

#agha ba mikham ye app jadid besazim bara in project ke Post hamon ro bezarim tosh

#step 1
#avalin kari ke miknim model.py 
#agha ma 3ta model niaz darm to in app avali k 100% post hast comments va like hast
# ina   toye in app hastan 

# toye post ma [title - caption -is active - is public - created time -update time -] mavared ro ma niaz darim 
#
#hala toye class meta verbose_name . verbose_name_plural ijad miknim

#hala haji yek seri data niaz dare in model man miam to ye model jadid[postfile] ino gharar midam va badan link mikonam be in

#hala chon in ghare be model post vasl beshe az foreigenkey estfade miknim va be post link mikonam


#    Psotfile ---> Post <---- Postfile

#                   ^
#                   |
#                 Postfile


#be sort bala postfile ha be post asli link shodan to data base
#dige ye image file va tarikh midim behesh ba class meta
post= models.ForeignKey(to='posts,Post' , on_delete=models.CASCADE)

#ye nokte ei k vojod dare to='posts.Post' agha in yani az app posts model Post

#brim ino install knim 

#felan kafie brim makemigrations migrate bznim 

#ye admin.py ham brim 2ta rgister knim

#ghabl az in ke brim soragh views ha in oskol zad rid
# be post user nadade bodim
user = models.ForeignKey(to=settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
#injori mishe rabete ba user ba import kadan setting 



#brim soraghe views.py 
#step 1 ijad serializer.py va urls.py 
# dash dige inaro kam kam beri codesho nega kni mifahmi dari chi mizani 

#brim to postman test knim api ro

**#boro to setting.py asli simpel jwt ro add kn time bara toke bede 1day

#haji ye token migiram miram to roote api/posts/
# bbin alan user va posts bayad bfrsti barash post k ba value key mizanim mimone user
# miri to postmn

#step 1
#Authorazation
# type ->  bearer Token
#ya to header miam Authorization token ra gharar midam
# ama bazam az man taeed user mikhad 
#haal age man az restfamework biam permission isauth roadd bzn to views.py khodam ye erro 401
# ke hamon access toke nhast mide

# pas moshkel to  serializer.py hast
 extra_kwargs = {
            'user':{'read_only':True}
        }
 #inja midam ke user fgh read kne
 
#  miam to views.py user ro moghe save kardan serializer midam behesh

# alan dare in post ro misaze  pas man daram 
# to body :
{
    "title":"test postman",
    "caption":"test caption",
    "is_active":false,
    "is_public":false
}
# in ro midam 
# token midam  ke agha ba in user va tokeni k dare in post ro to database man besaz     

#brim get ro bznim to views.py
    def get(self,request,post_pk):
        try:#inja migam boro post ba in id ro biar age nabod 404 neshon bede
            post = Post.objects.get(pk=post_pk,user=request.user)#user inja yani fght har user har posti  zade ro inja bebine be baghie user ha 404 mide
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)


###############################
# brim ye view bzim post haro neshon bede 
PostListView
#urls ham mizanam barash

http://127.0.0.1:8000/api/posts-list/

#alan har posti  k active inja be man bar migarde

###########################################################
#PROJECT PART 5
