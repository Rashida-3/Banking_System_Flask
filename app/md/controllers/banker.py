from flask import request, Blueprint, jsonify, session, current_app, make_response, render_template, flash, redirect, url_for
from app.md.models.user_model import User
from app.md.models.transactions_model import Transaction
from app.md import transaction_bp,admin_bp
from app.auth.decorator import token_required
from app.md.controllers.transaction_id import generate_transaction_id
from datetime import datetime
from app import db
from sqlalchemy import not_

# user_accounts_bp = Blueprint('user_accounts',__name__)


@admin_bp.route('/user_profile')
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
    if user.is_admin:
        return render_template('user_profile.html', admin=user)


@admin_bp.route('/transaction')
@token_required
def transaction():
    user_id = session.get('id')
    if not user_id:
        flash("Please log in to view your profile.", 'danger')
        return redirect(url_for('auth.login'))

    user = User.query.get(user_id)
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    if user.is_admin:
        return render_template('user_transaction.html', admin=user, transactions=transactions)


@admin_bp.route('/credit', methods=['GET', 'POST'])
@token_required
def credit_funds():
    user_id = session.get('id')
    user = User.query.get(user_id)

    if not user:
        flash("Please log in to perform this action.", 'danger')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        amount = request.form.get('amount', type=float)

        if not amount or amount <= 0:
            flash('Invalid amount. Please try again.', 'danger')
            return redirect(url_for('transaction.credit_funds'))

        user.balance += amount
        transaction_id = generate_transaction_id()
        transaction = Transaction(
            debit=0,
            credit=amount,
            date=datetime.utcnow().date(),
            time=datetime.utcnow().time(),
            account_balance=user.balance,
            user_id=user.id,
            transaction_id=transaction_id
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Deposit successful!', 'success')
        return render_template('credit.html',admin=user)
    
    return render_template('credit.html', admin=user)



@admin_bp.route('/debit', methods=['GET', 'POST'])
@token_required
def debit_funds():
    user_id = session.get('id')
    user = User.query.get(user_id)# if user_id else None

    if not user:
        flash("Please log in to perform this action.", 'danger')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        amount = request.form.get('amount', type=float)

        if not amount or amount <= 0:
            flash('Invalid amount. Please try again.', 'danger')
            return redirect(url_for('admin.debit_funds'))

        if amount > user.balance:
            flash('Insufficient funds for this transaction.', 'danger')
            return redirect(url_for('admin.debit_funds'),admin=user)

        user.balance -= amount
        transaction_id = generate_transaction_id()
        transaction = Transaction(
            debit=amount,
            credit=0,
            date=datetime.utcnow().date(),
            time=datetime.utcnow().time(),
            account_balance=user.balance,
            user_id=user.id,
            transaction_id=transaction_id
        )
        db.session.add(transaction)
        db.session.commit()
        flash('Withdrawal successful!', 'success')
        return render(url_for("admin.debit_funds"))
    return render_template('debit.html',admin=user)
    # if user.is_admin:
    #     return render_template('debit.html', admin=user)

@admin_bp.route('/users_account',methods=['GET', 'POST'])
@token_required
def users_account():
    session_id = session.get('id')
    if not session_id:
        flash("Please log in to view your profile.", 'danger')
        return redirect(url_for('auth.login'))
    if session_id:
        admin = User.query.get(session_id)
        if admin.is_admin:           
            # Fetch all users except those with is_admin == True
            users = User.query.filter(not_(User.is_admin)).all()
            return render_template('users_account.html',users=users,admin=admin)
        
    return render_template('users_account.html')
