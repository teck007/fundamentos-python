from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/listas')

def renderizar_listas():
   #Próximamente estas listas serán extraidas de la base de datos
   numero_azar = random.randint(0, 20)
   listado_estudiantes = [
       {'nombre': 'Florencia', 'edad': 25},
       {'nombre': 'Valentina', 'edad': 30},
       {'nombre': 'José', 'edad': 27},
       {'nombre': 'Patricio', 'edad': 21}
   ]
   listado_estudiantes2 = [
       {'nombre': 'Jaime', 'edad': 30},
       {'nombre': 'Carlos', 'edad': 28},
       {'nombre': 'Marcelo', 'edad': 22},
       {'nombre': 'Nicolas', 'edad': 19}
   ]
   return render_template('listas.jinja', numero = numero_azar, estudiantes=listado_estudiantes)

if __name__ == '__main__':
   app.run(debug=True)