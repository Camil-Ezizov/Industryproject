from app import app
from app import db
from flask import render_template,redirect,request,url_for
@app.route('/')
def adminIndex():
    return render_template('/admin/index.html',title='Dashboard')

@app.route('/icons')
def adminicons():
    return render_template('/admin/icons.html')


class Myicon:
    def __init__(self, title, text):
        self.title=title
        self.text=text


@app.route('/icons/add', methods=['POST'])
def addicons():
    if request.method == 'POST':
        title=request.form['icontitle']
        text=request.form['icontext']
        mydata=Myicon(title,text)
        db.session.add(mydata)
        db.session.commit()
        return redirect(url_for('adminicons'))
