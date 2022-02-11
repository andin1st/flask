from flask import Blueprint, render_template

auth=Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'ini login page'
@auth.route('/signup')
def signup():
    return render_template('signup.html')
