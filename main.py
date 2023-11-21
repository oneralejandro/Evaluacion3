from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')





@app.route('/Notas', methods=['GET', 'POST'])
def Notas():
    if request.method == 'POST':
        res =None
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        resultado = (nota1 + nota2 + nota3 )/ 3
        if asistencia >= 75 and resultado >= 40:
            res = "APROBADO !"
        else:
            res = "REPROBADO !"

        return render_template('Notas.html', resultado=resultado, nota1=nota1, nota2=nota2, nota3= nota3, asistencia=asistencia, res=res)
    return render_template('Notas.html')




@app.route('/ContadorCaracteres', methods=['GET', 'POST'])
def ContadorCaracteres():
    if request.method == 'POST':
        resultado= ''

        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        contador1 = nombre1
        contador2 = nombre2
        contador3 = nombre3
        resultado1 = len(contador1)
        resultado2 = len(contador2)
        resultado3 = len(contador3)

        if resultado1 > resultado2 and resultado1 > resultado3:
            resultado = "El Nombre con mayor cantidad de caracteres es : " +nombre1 +"  y tiene  " +str(resultado1)+ "caracteres  "


        elif resultado2 > resultado1 and resultado2 > resultado3:
            resultado = "El Nombre con mayor cantidad de caracteres es : " +nombre2+ " y tiene  " +str(resultado2)+ "caracteres "

        elif resultado3 > resultado1 and resultado3 > resultado2:
            resultado = "El Nombre con mayor cantidad de caracteres es : " +nombre3+ "  y tiene  " +str(resultado3)+ "caracteres "




        return render_template('ContadorCaracteres.html', resultado=resultado)
    return render_template('ContadorCaracteres.html')










if __name__ == '__main__':
    app.run(debug=True)