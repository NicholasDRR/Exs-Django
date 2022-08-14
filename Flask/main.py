from flask import Flask, render_template

app = Flask(__name__)


# route seria o caminho depois do seu domínio
# www.youtube.com/teste/teste
@app.route('/')
def homepage():
    return render_template('index.html', meunome='Nicholas Ribeiro')

@app.route('/contatos')
def contatos():
    return 'Nossos contatos são: E-mail: teste@gmail.com e Telefone: 119102834'






if __name__ == '__main__':
    # Coloca o site no 'ar'
    app.run(debug=True)  # debug vai atualizar o site a cada mudança no código
