import json

dados_json = '{ "nome":"ana", "idade":25,"cidade": "sao paulo"}'

dados_python = json.loads(dados_json)

print (dados_python["nome"])
print (dados_python["idade"])