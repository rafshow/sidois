from flask import Flask, render_template, request, redirect, make_response, url_for, redirect, Response
import csv
import time

app = Flask(__name__)

# Rota para exibir a página inicial com a votação
@app.route("/", methods=['GET'])
def exibir_votacao():
    color = request.cookies.get("color")
    return render_template('index.html',cookieColor = color)

# Rota para processar o voto quando enviado por POST
@app.route("/votar", methods=['POST'])
def votar():
    candidato = request.form['candidato']
    atualizar_votos(candidato)
    time.sleep(1.2)
    return redirect('/')

# Função para atualizar o número de votos do candidato
def atualizar_votos(candidato):
    votos = get_votos()
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1
    set_votos(votos)

# Função para obter os votos a partir do arquivo CSV
def get_votos():
    votos = {}
    with open('votos.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            candidato = row['candidato']
            num_votos = int(row['votos'])
            votos[candidato] = num_votos
    return votos

# Função para salvar os votos no arquivo CSV
def set_votos(votos):
    header = ['candidato', 'votos']
    with open('votos.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for candidato, num_votos in votos.items():
            writer.writerow({'candidato': candidato, 'votos': num_votos})

# Rota para exibir os resultados da votação
@app.route("/resultados", methods=['GET'])
def resultados():
    votos = get_votos()
    return render_template('resultados.html', votos=votos)


# Adicionei a rota de login, quando formos pro root o background color muda
@app.route("/login",methods=["GET","POST"])
def setcookie():
    resp = make_response(render_template("login.html"))
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        color = request.form["color"]
        resp.set_cookie("password",password)
        resp.set_cookie("username",user)
        resp.set_cookie("color",color)
    
    return resp
    

def getcookie():
    color = request.cookies.get("color")
    cookieName = request.cookies.get("name")
    return render_template('index.html', cookieColor=color)

# A rota logout exclui os cookies
@app.route('/logout', methods=['GET'])
def logout():
    resp = make_response(render_template("login.html"))
    resp.set_cookie('username', expires=0)
    resp.set_cookie('password', expires=0)
    resp.set_cookie('color', expires=0)
    return resp
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)