#!/usr/bin/env python3
import requests

projetos = requests.get('http://localhost/api/v4/projects' data={
    'private_token': 'token'
})

print(projetos.json())