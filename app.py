from distutils.log import debug
# This is the convention of structure a large application
from puppycompanyblog import app # import app from puppycompanyblog/__init__.py

if __name__ == '__main__':
    app.run(debug=True)