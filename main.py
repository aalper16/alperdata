from flask import Flask, render_template, request, redirect
import pymysql.cursors
import random

db = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

con = db.cursor()




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/veri_gir', methods = ['GET'])
def veri_gir():
    return render_template('veri_gir.html')

@app.route('/veri_kaydet',methods = ['POST'])
def veri_kaydet():
    global islemId
    islemId = random.randint(1, 10000000)
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        col1 = request.form.get('col1')
        col2 = request.form.get('col2')
        col3 = request.form.get('col3')
        col4 = request.form.get('col4')
        col5 = request.form.get('col5')

        con.execute('INSERT INTO alperdata VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', (islemId, name, password, col1, col2, col3, col4, col5))
        db.commit()

        return redirect('basarili')
@app.route('/basarili')
def basarili():
    global islemId
    return render_template('basarili.html', islemId = islemId)



if __name__ == "__main__":
    app.run(debug=True)