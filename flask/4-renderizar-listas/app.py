from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/listas')

def renderizar_listas():
   #Próximamente estas listas serán extraidas de la base de datos
   numero_azar = random.randint(0, 20)
   listado_estudiantes = [
       {'nombre': 'Florencia', 'apellido':'Rojas', 'edad': 25},
       {'nombre': 'Mauricio', 'apellido':'Gonzalez', 'edad': 20},
   ]
   return render_template('listas.jinja', numero = numero_azar, estudiantes=listado_estudiantes)

if __name__ == '__main__':
   app.run(debug=True)