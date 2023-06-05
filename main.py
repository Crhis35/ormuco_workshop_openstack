import requests
import json

base_url = 'https://api-uat-001.ormuco.com'


req = requests.post('{}:5000/v3/auth/tokens'.format(base_url),json={
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "ILOVECLOUD2022"
                }
            }
        }

}
    
                    })
token = req.json()['token']['id']
print(token)

images = requests.get("{}:9292/v2/images".format(base_url), headers={
                          'X-Auth-Token': token
                      })
print(json.dumps(images.json(), sort_keys=True, indent=4))
