"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os

from app import app
from flask import render_template, request, redirect, url_for, flash, send_from_directory, abort
from werkzeug.utils import secure_filename
from app.form import AddPropertyForm
from app.models import Properties, db
from .config import Config


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


# Route for listing properties
@app.route('/properties/')
def properties():
    props = Properties.query.all()
    print("Properties fetched:", props)
    return render_template('properties.html', properties=props)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/properties/<int:property_id>')
def property_detail(property_id):
    props = Properties.query.get(property_id)
    if props is None:
        abort(404)
    return render_template('property.html', property=props)


# Route for uploading new properties
@app.route('/properties/create', methods=['GET', 'POST'])
def new_property():
    form = AddPropertyForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_property = Properties(
            title=form.property_name.data,
            nofrooms=form.number_of_rooms.data,
            nofbrooms=form.number_of_bathrooms.data,
            location=form.location.data,
            image=filename,
            price=form.price.data,
            description=form.description.data,
            type=form.type.data
        )
        db.session.add(new_property)
        db.session.commit()
        flash('Property successfully added', 'success')
        return redirect(url_for('home'))

    return render_template('create_property.html', form=form)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
