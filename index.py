from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/acerca')
def acerca():
    return render_template('acerca_de_mi.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/herramientas')
def herramientas():
    return render_template('herramientas.html')

@app.route('/comunidad')
def comunidad():
    return render_template('comunidad.html')
    
if __name__ == '__main__':
    app.run(debug=True)