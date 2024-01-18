from flask import Flask
from views import views

app = Flask(__name__) #inicia a aplicação
app.register_blueprint(views, url_prefix="/views") #se digitarmos /views no endereço no navegador, vamos para a 
#rota / de @views definida no views.py, por exemplo. Se quisermos alterar para /home, em vez de /views, é 
#só mudar no url_prefix

if __name__ == '__main__':
    app.run(debug=True, port=8000) #habilita o debug e configura a porta do servidor que o Flask vai rodar


