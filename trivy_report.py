import json
import requests
import argparse
 
url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def upload(file_report, type_scan):
    headers = {
        'accept': 'application/json',
        'Authorization': api_key

    }
    report = {
    'file': open(file_report, 'rb')
    }
    body = {
    'product_name': 'WebGoat',
    'engagement_name': 'mariano',
    'product_type_name': 'Research and Development',
    'active': True,
    'verified': True,
    'scan_type': type_scan
    }

    r = requests.post(url_api.format(method = 'import-scan/'), files = report, data = body, headers = headers, verify = False) 
    print(r.status_code)
    if r.status_code == 201:  # Check the appropriate status code
        print(json.dumps(r.json(), indent=4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f',dest='file', help='Nombre del reporte', required=True)
    parser.add_argument('--type-scan', '-t', dest='type_scan', help='Nombre del escaner', required=True)
    args = parser.parse_args()
    upload(args.file, args.type_scan)