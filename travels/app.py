from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Travel, app
from forms import TravelForm

@app.route('/')
def index():
    travels = Travel.query.all()
    return render_template('index.html', travels=travels)

@app.route('/add', methods=['GET', 'POST'])
def add_travel():
    form = TravelForm()
    if form.validate_on_submit():
        travel = Travel(
            destination=form.destination.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            budget=form.budget.data,
            services=form.services.data
        )
        db.session.add(travel)
        db.session.commit()
        flash('Travel added successfully!')
        return redirect(url_for('index'))
    return render_template('add_travel.html', form=form)

@app.route('/edit/<int:travel_id>', methods=['GET', 'POST'])
def edit_travel(travel_id):
    travel = Travel.query.get_or_404(travel_id)
    form = TravelForm(obj=travel)
    if form.validate_on_submit():
        travel.destination = form.destination.data
        travel.start_date = form.start_date.data
        travel.end_date = form.end_date.data
        travel.budget = form.budget.data
        travel.services = form.services.data
        db.session.commit()
        flash('Travel updated successfully!')
        return redirect(url_for('index'))
    return render_template('edit_travel.html', form=form, travel=travel)

@app.route('/delete/<int:travel_id>')
def delete_travel(travel_id):
    travel = Travel.query.get_or_404(travel_id)
    db.session.delete(travel)
    db.session.commit()
    flash('Travel deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)