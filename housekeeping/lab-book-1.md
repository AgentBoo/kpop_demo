#### psql 
```
createdb kpop 
psql kpop

CREATE USER kpop WITH PASSWORD 'kpop';
ALTER ROLE kpop SET client_encoding TO 'utf8';
ALTER ROLE kpop SET default_transaction_isolation TO 'read committed';
ALTER ROLE kpop SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE poems TO poems;
\q
```

<br>

#### Settings 
1. There are no extra statifiles directories outside of staticfiles  
```python
STATIC_URL = '/static/' 
STATIC_ROOT = STATIC_DIR = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []
```

2. Whitenoise
Use whitenoise in both dev and prod, but do NOT EVER USE THE WHITENOISE STORAGE 
https://stackoverflow.com/questions/26829435/collectstatic-command-fails-when-whitenoise-is-enabled/32347324#32347324
https://docs.djangoproject.com/en/1.11/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.ManifestStaticFilesStorage.manifest_strict

3. Databases 
Comment out or delete preconfigured DATABASES and define your own  

4. DEBUG 
Keep DEBUG False by default
export DJANGO_DEBUG=True for development 

```python
DEBUG = bool(os.getenv('DJANGO_DEBUG', False))
```

<br>

#### Models 
Survey 
age 
country -- choices 
favorite_artist -- choices 

<br>

#### Forms 
**Forms**
age                 text input 
country             select 
favorite_artist     select

<br>

#### Views 
**Views**
authenticate with reddit 
show form 
post form 
main page = results page 

<br>

#### Templates 
landing:index.html 
survey:pre_survey.html 
survey:survey_form.html 
survey:post_survey.html

<br>




<br>

#### Color palette 
+ #51c1ba serpent
+ #eb5e55 sunset 
+ #3a3335 jet 
+ #989788 spanishgray
+ #f2efea isabelline
+ #2364aa lapis 
+ #fec601 golden 
+ #ff6b35 tangelo 
+ #db2b39 carmine 
+ #29335c koamaru 

<br>

