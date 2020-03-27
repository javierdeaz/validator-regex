from flask import Flask, render_template, request
from flask import flash, url_for
import re

app = Flask(__name__)
app.secret_key = 'No hay mensaje'


@app.route('/')
def index():
    return render_template('Index.html')


val_patron = re.compile('^([A-Z][0-9]{3}[a-z]+[\W]{3})$')


@app.route('/validar', methods=['GET'])
def validar():
    if request.method == 'GET':
        passw = request.args.get('passw')
        if(val_patron.match(passw)):
            flash("La contraseña es Valida.", "success")
            return render_template('validar.html')
        else:
            flash("La contraseña es Invalida.", "error")
            return render_template('error.html')


if __name__ == '__main__':
    # Metodo Run
    app.run(debug=True, port=8000)
