from pymongo import MongoClient


#Fazer conexao
mongo_con = MongoClient()
#Usar Banco
db = mongo_con['flask-app']
