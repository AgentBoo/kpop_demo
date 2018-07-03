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

