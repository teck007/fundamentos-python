from flask import Flask, render_template
import random

app = Flask(__name__)    

@app.route('/')         
def hola_mundo():
   return render_template('index.jinja') 

@app.route('/bienvenido')
def bienvenido():
   resultado = random.randint(1, 10)
   return render_template('bienvenida.jinja', valor=resultado) 

if __name__=="__main__":   
   app.run(debug=True)    
