#Online-Shopping
--------------------------------

This web application develope by using django


To run locally, do the usual:

#. Create a Python 3.6 virtualenv

#. Install dependencies::

	``pip install -r requirements.txt```

#. Create database:: 
	online_shopping
	
#. Create tables::
	
	``python manage.py migrate``

#. Create a superuser::

	``python manage.py createsuperuser``

#. Finally run the server::

	``python manage.py runserver