from flask import Flask,request,redirect, render_template
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/resultados')
def resultados():
    resultados = get_resultados()
    return render_template('resultados.html', resultados=resultados)

# Função para salvar o voto em um arquivo CSV
def salvar_voto(candidato_id):
    with open('votos.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([candidato_id])

# Função para get os resultados da votação a partir do arquivo CSV
def get_resultados():
    resultados = {}
    with open('votos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            candidato_id = row[0]
            if candidato_id in resultados:
                resultados[candidato_id] += 1
            else:
                resultados[candidato_id] = 1
    return resultados



if __name__ == '__main__':
    app.run(port=5000)
    app.run(debug=True)