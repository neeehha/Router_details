# Router-Details
This is a python Django project based on MVC-MVT framework, which basically performs CRUD application on "router details" table

Router details table fields are
Sapid(18), Hostname(14), Loopback(IPv4), Mac address(17) , is_delete


Main project is containing one single app i.e router_api
Authetication Type - Token Authentication
Router details can be created, updated, viewed, deleted and fetched within an IP range. Database used for the application is SQLite. 

All the Create, update, view, delete and view_in_range methods are defined in routers/views.py

All the application urls are in router/urls.py 

Mutiple Unit tests has been created
