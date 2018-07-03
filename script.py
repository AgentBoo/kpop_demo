# write an array of countries into countries.py 
# import requests 
# import json

# url = 'https://restcountries.eu/rest/v2/all'
# req = requests.get(url)

# if req.status_code == 200:
# 	countries = [ country['name'] for country in req.json() ]
# 	print(countries)

# 	with open('countries.py', 'w+') as file:
# 		file.write(str(countries)) 

# 		file.close()


# check countries.py 
# from countries import countries 
# print(countries)