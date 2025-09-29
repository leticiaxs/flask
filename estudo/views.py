
from estudo import app
from flask import render_template, redirect, url_for    

@app.route('/')
def homepage():
    usuario = 'Leticia'
    idade = 25

    context = {
        'usuario': usuario,
        'idade': idade
    }

    return render_template('index.html', context=context)

@app.route('/contatos/')
def nova_pagina():
    return "<p>Esta é uma nova página!</p>"