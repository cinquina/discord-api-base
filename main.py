import requests
import json

API_URL = "https://discord.com/api/v9/auth/login"
EMAIL = "youremail@provider.domain"
PASSWORD = "yourpassword"

jparams = {
    'login': EMAIL, 
    'password': PASSWORD, 
    'undelete': False
}

request = requests.post(API_URL, json=jparams)
if request.status_code == 200:
    result = json.loads(request.text)
    print('Account is valid! Token: ' + result['token'])
    # your code
else:
    print('Account is invalid')
    # your code