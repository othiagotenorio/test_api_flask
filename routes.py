from os import stat_result
from flask import Flask, request

from database import insertUser

app = Flask("API")

@app.route("/OláMundo", methods=["GET"])
def olaMundo():
    return {"Olá": "Mundo"}

@app.rout("/cadastrar/usuario", methods=["POST"])
def cadastrarUsuario():

    body = request.get_json()

    if("name" not in body):
        return geraResponse(400, "O parametro name é obrigatorio")

    if("email" not in body):
        return geraResponse(400, "O parametro email é obrigatorio")

    if("password" not in body):
        return geraResponse(400, "O parametro password é obrigatorio")        

    user = insertUser(body["name"], body["email"], body["password"])

    return geraResponse(200, "Usuário criado", "user", user)

    def geraResponse(status, message, name_response=False, content=False):
        response = {}
        response["status"] = status
        response["message"] = message

        if(name_response and content):
            response[name_response] = content
        return response    


app.run()

