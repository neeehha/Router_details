# Assignment 1 - Router-Details
This is a python Django project based on MVC-MVT framework, which basically performs CRUD application on "router details" table

Router details table fields are
Sapid(18), Hostname(14), Loopback(IPv4), Mac address(17) , is_delete

Main project is containing one single app i.e router_api
Authetication Type - Token Authentication
Database - SQLite.
All the Create, update, view, delete and view_in_range methods are defined in routers/views.py
All the application urls are in router/urls.py 


Router details can be created, updated, viewed, deleted and fetched within given IP ranges. 
APIs are as listed below -
1) create-router  - to create new router details with unique Sapid, Hostname, Loopback and Mac address
2) update-router - Update existing router details based on unique Loopback
3) router-details - Get the list of all routers with details
4) retrieveRouterDetailsbyIPrange - Get the list of routers as per given IP range values
5) delete-router - Soft delete existing router details based on unique Loopback 


Mutiple Unit tests has been created


# Assignment 2 - Netmiko library
Using netmiko library to
i) SSH to the server. Run a command(ls) on the server and save its output to an 
external text file
ii) File transfer to the server(FTP)
