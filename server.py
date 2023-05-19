from flask import Flask, render_template, request, redirect
import csv
import time

app = Flask(__name__)

# Rota para exibir a página inicial com a votação
@app.route("/", methods=['GET'])
def exibir_votacao():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)