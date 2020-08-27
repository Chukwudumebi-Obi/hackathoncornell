from flask import Flask, redirect, url_for, render_template
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests 

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# class ReusableForm(Form): 
#     name = TextField('Name:', validators=[validators.required()])
    
#     def __init__(self, Form):
#         self.Form = Form

#     @app.route("/", methods=['GET', 'POST'])
#     def hello():
#         form = ReusableForm(requests.form)
    
#         print(form.errors)
#         if requests.method == 'POST':
#             name=requests.form['name']
#             print(name)
    
#         if form.validate():
#             # Save the comment here.
#             flash('Hello ' + name)
#         else:
#             flash('All the form fields are required. ')
    
#         return render_template('hello.html', form=form)

#     hello()

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

