from flask import Blueprint, request, render_template, redirect, url_for, flash
from marshmallow import ValidationError
from hashlib import sha256
from app.md.models.user_model import User
from app.md.serde.user_schema import userschema
from app import db
from app.auth import auth_bp
from .generate_account_number import generate_account_number

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Collect form data
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        pin = data.get('pin')

        # Validate the presence of all required fields
        if not name or not email or not password or not pin:
            flash('All fields are required!', 'danger')
            return render_template('signup.html')

        # Validate PIN length
        if len(pin) != 4:
            flash('PIN must be exactly 4 digits.', 'danger')
            return render_template('signup.html')

        # Create data dictionary for validation
        user_data = {
            'name': name,
            'email': email,
            'password': password,
            'pin': pin,
            'is_admin': 0  # Assuming default user is not an admin
        }

        try:
            validated_data = userschema.load(user_data)
        except ValidationError as e:
            flash('Validation Error: ' + str(e.messages), 'danger')
            return render_template('signup.html')

        # Check if the email is already registered
        if User.query.filter_by(email=validated_data['email']).count():
            flash('Email already registered. Please login to continue.', 'warning')
            return render_template('signup.html')

        # Hash the password
        hashed_password = sha256(validated_data['password'].encode('utf-8')).hexdigest()
        account_no = generate_account_number()

        # Create a new user instance
        new_user = User(
            name=validated_data['name'],
            email=validated_data['email'],
            password=hashed_password,
            is_admin=validated_data['is_admin'],
            pin=validated_data['pin'],
            account_no=account_no,
        )

        # Save the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("Signup successful. Please log in.", 'success')
        return render_template('login.html')  # Redirect to login page after successful signup

    return render_template('signup.html')