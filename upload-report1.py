import requests
import json

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def create_product ():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': api_key
    }
    body = {
        "id": 42,
        "name": "Michis",
        "description": "GAtit0s",
        "prod_numeric_grade": 2147483648,
        "business_criticality": "very high",
        "platform": "web service",
        "lifecycle": "construction",
        "origin": "third party library",
        "user_records": 2147483648,
        "revenue": "39.",
        "external_audience": True,
        "internet_accessible": True,
        "enable_product_tag_inheritance": True,
        "enable_simple_risk_acceptance": True,
        "enable_full_risk_acceptance": True,
        "disable_sla_breach_notifications": True,
        "product_manager": 0,
        "technical_contact": 0,
        "team_manager": 0,
        "prod_type": 0,
        "sla_configuration": 0,
        "regulations": [
          0
        ]
    }


    
    
    r = requests.post(url_api.format(method = 'product/add'), headers = headers, json = body, verify = False)
    print (r.status_code)
    if r.status_code == 201:  # HTTP 201 means the resource was created
        body = r.json()
        print('Product created successfully.')
    else:
        print ('Fail XD')
        
if __name__ == '__main__':
    create_product()
    
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