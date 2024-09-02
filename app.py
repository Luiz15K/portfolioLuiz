from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('about.html')

@app.route('/projetos')
def projetos():
    return render_template('projects.html')

@app.route('/experiencia')
def experiencia():
    return render_template('experience.html')

@app.route('/habilidades')
def habilidades():
    return render_template('skills.html')

@app.route('/contato')
def contato():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
