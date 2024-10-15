from flask import Flask, render_template, request

from bot import processar_produto

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template(r'index.html')


@app.route('/processar_formulario', methods=['POST'])
def processar_formulario():
    nome = request.form['nome']
    preco = float(request.form['preco'])
    qtd = int(request.form['qtd'])
    
    produto = {
        'nome' : nome,
        'preco' : preco,
        'qtd' : qtd
    }
    
    processar_produto(produto)
    
    return formulario()


if __name__ == "__main__":
    app.run(debug=True)