### References 

#### World countries 
http://api.worldbank.org/v2/countries
http://country.io/names.json


#### Search filter component 
https://github.com/silviomoreto/bootstrap-select
https://www.w3schools.com/howto/howto_js_filter_lists.asp


#### Django
1. remove dashes from uuid**
https://docs.python.org/3/library/uuid.html#uuid.UUID.hex

2. request params 
https://docs.djangoproject.com/en/2.0/ref/request-response/

```python 
# request.GET gives you params as a QueryDict 
print(request.GET)
=> 
<QueryDict: {
    'state': ['1994c98a088742daaf879d4f81fceadd'], 
    'error': ['access_denied']}>
```

3. messages
https://docs.djangoproject.com/en/2.0/ref/contrib/messages/

4. setting cookie expiry time 
https://docs.djangoproject.com/en/2.0/topics/http/sessions/


#### Converting timestamps to datetime 
https://docs.python.org/3/library/datetime.html#datetime.date.fromtimestamp

```python
cake_day = datetime.date.fromtimestamp(redditor.created_utc)
```


4. 'partials' for django 
https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#include


#### PRAW
 OAuth2 workflow: 
 + auth_url => 
 + reddit authentication system => 
 + redirect_uri callback + params => 
 + parse params

https://praw.readthedocs.io/en/latest/getting_started/authentication.html#using-refresh-token

```python
# to create a read-only reddit instance, you need:
# client ID, client secret, and user agent 
# to create an authorized reddit instance:
# pass in username and password to the reddit initializer 

# OAUTH2
# 1. obtain authorization url 
# outputted auth url should be accessed by the account that will authorize access to their account  
reddit = praw.Reddit(client_id=client, 
                     client_secret=secret, 
                     user_agent=user_agent, 
                     redirect_uri=uri)


# reddit_instance.auth.url(scopes, state, duration='permanent', implicit=False)
# scopes = [ list of oauth scopes to request authorization for ]
# state = 'rand str, unique to a client for whom the cb URL was generated' 
# duration='temporary' generates a token for 1 hour 
# duration='permanent' generates a refresh token that can be used indefinitely 
# to generate new hour-long access tokens 
auth_url = reddit.auth.url(['identity'], 'survey_state', 'permanent'))

# 2. on completion of that flow, the user's browser will be redirected to the redirect_uri
=>  
https://www.reddit.com/api/v1/authorize?client_id=uHK8FsjEZggwqg&duration=permanent&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauth%2Fr&response_type=code&scope=identity&state=censusdemo

state=censusdemo
code=D3ei8ZQkLL-255kBck0yW07D_OI

# 3. generate refresh token using the code param from the redirect_uri cb
# outputs a refresh token
refresh_token = reddit.auth.authorize(code)
=> 
'130499681391-LVKEgO-4Zt1NDTkscC7kh4nItVY'

# outputs the person who is authenticated
# and associates the reddit instance with that redditor 
redditor = reddit.user.me())
 
# 4. use refresh token to obtain an authorized instance of reddit 
auth_reddit = praw.Reddit(client_id='SI8pN3DSbt0zor',
                     client_secret='xaxkj7HNh8kwg8e5t4m6KvSrbTI',
                     refresh_token='WeheY7PwgeCZj4S3QgUcLhKE5S2s4eAYdxM',
                     user_agent='testscript by /u/fakebot3')

# 5. or find a redditor + cake_day using standard reddit instance 
reddit = praw.Reddit(client_id=client,
                     client_secret=secret,
                     user_agent = user_agent)

redditor = reddit.redditor('brewdo1234')
cake_day = redditor.created_utc
```


#### Bootstrap 
1. Bootstrap4 starter template
https://getbootstrap.com/docs/4.1/getting-started/introduction/
2. Bootstrap3 starter template 

```
# Bootstrap4 
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
  </body>
</html>


# Bootstrap3 
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

```


7. Customizing Boostrap
https://stackoverflow.com/questions/10451317/twitter-bootstrap-customization-best-practices

https://github.com/twbs/bootstrap/blob/v4-dev/dist/css/bootstrap.css

http://twitterbootstrap3buttons.w3masters.nl/?color=%23db2b39

8. Styling forms 
https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html

9. bootstrap-select 
https://silviomoreto.github.io/bootstrap-select/






