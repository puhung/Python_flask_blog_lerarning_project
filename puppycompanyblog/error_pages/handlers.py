# serve the views ot the error pages

from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

# this is the main approach for setting up your own templates to be served for a particular errors
@error_pages.app_errorhandler(404) #use app_errorhandler to handle general error, then we pass the error we  want it to connect to.
def error_404(error):
    # error_pages/404.html is a specific folder under the general templates folder

    # the return value is a tuple
    return render_template('error_pages/404.html'), 404

@error_pages.app_errorhandler(403) 
def error_404(error):
    return render_template('error_pages/404.html'), 404