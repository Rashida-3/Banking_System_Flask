from flask import request, Blueprint, jsonify, session, current_app, make_response, render_template, flash, redirect, url_for
from app.md.models.user_model import User
from app.md.models.transactions_model import Transaction
from hashlib import sha256
from datetime import datetime, timezone, timedelta
import jwt
from app.auth import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'id' in session:
            print(session)
            return redirect(url_for('transaction.user_profile')) 
    if request.method == 'POST':
        data = request.form           

        if not data:
            flash("Login fields can't be empty..!!", 'danger')
            return render_template('login.html')

        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            flash("Both name and password fields are required.", 'danger')
            return render_template('login.html')

        user = User.query.filter_by(name=name).first()
        if user and sha256(password.encode('utf-8')).hexdigest() == user.password:
            # Check if user is already logged in
            # id_in_session = session.get('id')
            # if id_in_session == user.id:
            #     flash("You are already logged in..", 'info')
            #     return redirect(url_for('transaction.user_profile'))

            # Set user_id in session
            session['id'] = user.id

            # Generate JWT token
            expiry = datetime.now(timezone.utc) + timedelta(minutes=10)
            payload = {'id': user.id, 'email': user.email, 'exp': expiry}
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

            if user.is_admin:
                response = make_response(redirect(url_for('admin.user_profile')))

            # Create response with token as cookie
            else:
                response = make_response(redirect(url_for('transaction.user_profile')))
            response.set_cookie('token', token, httponly=True)

            return response

        flash("Invalid credentials.", 'danger')
        return render_template('login.html')

    return render_template('login.html')

