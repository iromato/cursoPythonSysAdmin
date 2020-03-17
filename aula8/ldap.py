#!/usr/bin/env python3

import ldap3
from hashlib import md5
from binascii import b2a_base64

username = 'admin'
password = 'admin'

server = ldap3.Server('ldap://localhost:389')
client = ldap3.Connection(server,f'cn={username},dc=example,dc=org',password)

client.bind()
print(client)

#inserindo um usuario
md5json = md5('!23mudar'.encode('utf-8')).digest()

user = {
        'cn':'Renato',
        'sn':'silva',
        'mail':'renato.mori@aol.com',
        'uidNumber':'1000',
        'gidNumber':'1000',
        'uid':'renato.silva',
        'homeDirectory':'/home/renato',
        'userPassword':'{MD5}' + b2a_base64(md5json).decode('utf-8')

        }

objectClass = ['top','person','organizationalPerson','inetOrgPerson','posixAccount']

print(client.add(
   f'uid={user["uid"]},dc=example,dc=org',
   objectClass,
   user,
   ))

dn = f'uid={user["uid"]},dc=example,dc=org'
# #pesquisar
# client.search(dn,'(objectclass=person)',attributes=['cn','mail','sn'])
# print(client.entries)
# #alterar
# changes = {
#             'mail':[(ldap3.MODIFY_REPLACE,['xuxa@meneguel.com'])]
#           }

# #client.modify(dn,changes)

# print(client.result)


# #deletar registro
# print(client.delete(dn))
