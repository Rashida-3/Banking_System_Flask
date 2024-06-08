from flask import request, Blueprint, jsonify, session, current_app, make_response, render_template, flash, redirect, url_for
from app.md.models.user_model import User
from app.md.models.transactions_model import Transaction
from hashlib import sha256
from datetime import datetime, timezone, timedelta
import jwt
from app.md import transaction_bp
from app.auth.decorator import token_required




@transaction_bp.route('/user_profile')
@token_required
def user_profile():
    user_id = session.get('id')
    if not user_id:
        flash("Please log in to view your profile.", 'danger')
        return redirect(url_for('auth.login'))

    user = User.query.get(user_id)
    if not user:
        flash("User not found.", 'danger')
        return redirect(url_for('auth.login'))

    return render_template('user_profile.html', user=user,admin=user)