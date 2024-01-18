from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint("views", __name__) #você precisa passar o nome do blueprint, sempre nessa ordem

@views.route("/")
def home():
    #return render_template("index.html") #para renderizar o arquivo index.html
    return render_template("index.html", name = "Irineu") #para renderizar a variável name no arquivo index.html

'''
@views.route("/profile/<username>")                         #    -> Fazer isso para quando colocar /profile
def profile(username):                                      #    -> views/profile/nomedousuario, a página renderizar 
    return render_template("index.html", name=username)     #    -> o nome do usuário
'''

'''
@views.route("/profile")            #se eu digitar /profile?name=john, vai renderizar o nome depois do =
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)

'''

@views.route("/profile")
def profile():
    return render_template("profile.html") #para renderizar o arquivo profile.html

#Observação-> Só funciona uma rota profile por vez, não tem como o sistema ter rotas diferentes com os mesmos nomes

@views.route("/json")
def get_json():
    return jsonify({'name': 'leo', 'happiness':'100'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

