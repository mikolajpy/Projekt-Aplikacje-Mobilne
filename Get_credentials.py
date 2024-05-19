import requests

# Adres URL endpointu dla logowania
url = 'http://127.0.0.1:8000/A/api-token-auth/'

# Dane użytkownika
credentials = {
    'username': 'mikolajs',
    'password': 'mikolaj'
}

# Wysyłanie zapytania POST z danymi logowania
response = requests.post(url, data=credentials)

# Wyświetlenie odpowiedzi serwera
print("\n",response.text,"\n")


#curl.exe -X GET -H "Authorization: Token 38a6a5cf7e7ca917204d3bbccd4f4b12d19e5fb6" http://127.0.0.1:8000/A/ENDPOINT

"""
W CMD 

curl.exe -X POST "http://localhost:8000/A/storeID=9/coms" -H "Content-Type: application/json" -H "Authorization: Token 38a6a5cf7e7ca917204d3bbccd4f4b12d19e5fb6" -d "{\"parent\": 35, \"store\": 9, \"comment\": \"This is a second main comment.\", \"Ocena\": null}"

Post tokenu
curl -X POST -H "Authorization: Token 38a6a5cf7e7ca917204d3bbccd4f4b12d19e5fb6" -d "token=oGytCoMt" http://127.0.0.1:8000/A/visit/
"""