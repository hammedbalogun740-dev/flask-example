import json
import jwt
import requests

URL = "http://localhost:5000/resend-otp" 
payload = { 
    'email': 'hammedbalogun740@gmail.com'
}

response = requests.post(url=URL, data=json.dumps(payload))
print(response.json())




# token = jwt.encode({"name":"sean", 'height': 1.98, 'iasAdmin': False}, 
#            "secret-key", 
#            algorithm="HS256"
# )

# print(token)
 

# new_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.KMUFsIDTnFmyG3nMiGM6H9FNFUROf3wh7SmqJp-QV30"
# decoded_data = jwt.decode(
#     new_token,
#     key='a-string-secret-at-least-256-bits-long',
#     algorithms=["HS256"]
#     )
# print(decoded_data)