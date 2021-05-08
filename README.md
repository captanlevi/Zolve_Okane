# Zolve_Okane
Assignment for zolve internship

The following is my django implementation for a e-wallet named Okane (japanese for money), I have attached a requirements.txt and documentation for requests.  
The code should run after setting up django and django-restframework.  
Race conditions are implicitly handled as the dataBases that are supporeted in django have concurrency control , additionally ATOMICITY has been set to true in  
Django itself.  

For rest of the documentation refer to the comments in the code. Please let me know if there are any issues.  

To start the server just do python manage.py runserver.
