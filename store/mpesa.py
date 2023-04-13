import requests
from requests.auth import HTTPBasicAuth
import json
request = ""
a
def getAccessToken(request):
    consumer_key = 'hg2GWeg83LVGb9dlzXMGEEEcDCAqzTfr'
    consumer_secret = 'FubIWAfCAFqGoVrY'
    api_URL = ''
    r = request.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    print(validated_mpesa_access_token)
    
getAccessToken(request)