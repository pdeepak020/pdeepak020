from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Expense
from . import db
from sqlalchemy import func

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        amount = request.form.get('amount')
        description = request.form.get('description')
        category = request.form.get('category')

        if not amount:
            flash('Amount is required!', category='error')
        else:
            new_expense = Expense(amount=float(amount), description=description, 
                                category=category, user_id=current_user.id)
            db.session.add(new_expense)
            db.session.commit()
            flash('Expense added!', category='success')

    # Get all expenses for the current user
    expenses = Expense.query.filter_by(user_id=current_user.id).order_by(Expense.date.desc()).all()
    
    # Calculate total expenses
    total = db.session.query(func.sum(Expense.amount)).filter_by(user_id=current_user.id).scalar() or 0

    return render_template("home.html", user=current_user, expenses=expenses, total=total)

@views.route('/delete-expense/<int:id>')
@login_required
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    if expense.user_id != current_user.id:
        flash('You do not have permission to delete this expense.', category='error')
        return redirect(url_for('views.home'))
    
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted!', category='success')
    return redirect(url_for('views.home')) 