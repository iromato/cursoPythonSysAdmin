#!/usr/bin/env python3

import requests as r 
import json

url = 'http://gen-net.herokuapp.com/api/users'

#Lembrando que o r se refere ao modulo requests
res = r.get(url) #Requisicao via metodo get
# print (dir (res)) // ver todos os atributos e metodos

# users = res.json()

# for user in users:
#     print (user['name'])

# dados = {

#     "name": "Renato",
#     "email": "renato.mori@fabricads.com.br",
#     "password": "@23Mudar"
    
# }

# res = r.post(url=url,json=dados)
# print(res.json())


# pesquisa = {
#     "id": "323"

# }

# res = r.get(url,params=pesquisa)
# print(res.json())



atualizacao = {
    "id":"323",
    "name":"Batata"
}

res = r.put(url,params=atualizacao)
print (res.json())