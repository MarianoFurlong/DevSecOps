import requests
import json

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def get_products ():
    headers = {
        'accept': 'application/json',
        'Authorization': api_key
    }
    
    r = requests.get(url_api.format(method = 'products'), headers = headers, verify = False)
    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))
        
if __name__ == '__main__':
    get_products()