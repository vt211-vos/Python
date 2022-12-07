

from flask import Flask, flash, render_template, redirect, request, g, abort
import sqlite3
import os

DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'di&l594&$89mfh$&h$g4'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,"lfsite.db")))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

from FDataBase import FDataBase
# Клас для роботи з бд

@app.route('/')
def index():
    return render_template("index.html")




@app.route("/albums", methods=["POST", "GET"])
def showPost():
    db = get_db()
    dbase = FDataBase(db)
    post = dbase.getAllPost()


    return render_template('albums.html', post=post)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/album-page/<int:id>')
def album_page(id):
    db = get_db()
    dbase = FDataBase(db)
    post = dbase.getPost(id)
    return render_template('album-page.html', post=post)


@app.route('/admin-page', methods=["POST", "GET"])
def admin_page():
    db = get_db()
    dbase = FDataBase(db)
    post = dbase.getAllPost()

    if request.method == "POST":
         if len(request.form['name'])>1:
            res = dbase.AddAlbum(request.form['name'], request.form['year'], request.form['info'], request.form['info2'])
            if not res:
                flash('Помилка додавання альбому', category="error")
            else:
                flash('Альбом додано успішно', category='success')
         else:
             flash('Помилка додавання альбому', category='error')


    return render_template('admin-page.html', post=post)


@app.route('/edit-page/<int:id>', methods=["POST", "GET"])
def edit_page(id):
    db = get_db()
    dbase = FDataBase(db)
    post = dbase.getPost(id)
    if request.method == "POST":
         if len(request.form['name'])>1:
            res = dbase.updatePost(id, request.form['name'], request.form['year'], request.form['info'], request.form['info2'])
            if not res:
                flash('Помилка додавання альбому', category="error")
            else:
                flash('Альбом додано успішно', category='success')
         else:
             flash('Помилка додавання альбому', category='error')
    return render_template('edit-page.html', post=post)



@app.route('/history')
def history():
    return render_template('history.html')




@app.route('/login', methods=["POST", "GET"])
def login():
    message = ""
    if request.method == "POST":
        #Сторінка аміна тільки адміну
        if request.form['name'] == 'admin' and request.form['password'] == 'admin':
            return redirect("/admin-page")
        message = "Ви не адмін"
    return render_template('login.html', message=message)


@app.route('/photos')
def photos():
    example_photos = ['slider-2.jpg', 'slider-1.jpg', 'slider-2.jpg', 'slider-3.jpg', 'slider-2.jpg']
    return render_template('photos.html', photos=example_photos)




if __name__ == '__main__':
    app.run(debug=True)
