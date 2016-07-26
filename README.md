# Magento To Django Tool
###### Transfer your categories and products from Magento to Django

The tool in itself is composed of a bash script, a python script and a
folder containing a few resources.

-   migrateFromMagento.sh
-   migrationTool.py
-   migrationTool/

## 1 – What does it do?

In a word, this tool will get your Magento database and put it inside
your Django database.

It will then create a new storeMagento application into Django and
create the correct files from your database and from the tools
resources.

You’ll just have to setup a few more things manually and you’re good to
go with your new Django store!

## 2 – About this repository

Before we get started, here is a description of what is in this
repository:

-   The apache file: this is a copy of my apache configuration. It is
    set up so the Django and the Magento websites are accessible through
    localhost/Django and localhost/magento
-   The magentosite directory: contains the whole Magento website
    source files.
-   The djangosite : contains the Django project and the tool files.

## 3 – Setup configuration 

Before starting, let’s make sure we start off with the same
configuration:

-   Python 3 v3.4 (3.5 should work too)
-   Django 1.9 (1.8 should work too)
-   Magento CE 1.9.4.2
-   MySQL 5.5+
-   Apache2 Web server

Make sure you have PyMySql installed so you can use MySQL with Python3.
(add lines 'import pymysql' and 'pymysql.install\_as\_MySQLdb()' in the
\_\_init\_\_.py file of your project application.)

Make sure you have set your STATIC\_ROOT variable in the Django
settings.py, along with a static folder.

Make sure you have a template DIR in you settings.

Configure your wsgi.py

## 4 – Use the tool

Create your new Django project, or use a currently existing setup.

Put the tool inside your project root, where the manage.py file is
located.

Give the two script files and the folder at least 755 permissions.

Edit the config.cfg file with your magento mysql login details.

Execute ./migrateFromMagento.sh

After that you need to make a few more adjustment on your settings.

-   Add ‘magentoStore’ to your INSTALLED\_APPS
-   Add the following urls to your urls.py
'''
    import storeMagento.views
    
    urlpatterns = \[
    
    url(r’\^admin/’, admin.site.urls),
    
    url(r’\^cat/(?P&lt;category\_id&gt;\\d+)/\$’,
    storeMagento.views.categorypage\_view),
    
    url(r’\^item/(?P&lt;item\_id&gt;\\d+)/\$’,
    storeMagento.views.itempage\_view),
    
    url(r’\^\$’, storeMagento.views.homepage\_view),
    
    \]
'''

## 5 – How does it work?

###### Here is a little explanation on how the script works.

-   It dumps the whole magento database and stores the file in the
    migrationTool folder
-   It loads the dump file into the Django database
-   It deploys the files from migrationTool to the application. That
    includes the views.py for the storeMagento app, but also the static
    files and the templates.
-   It extracts a model from the new Django database, and sets it to the
    storeMagento app.
-   It cleans this model so there are no errors on execution
-   It restarts Apache2

That’s all for the migration itself. The whole part about reading and
using the data is managed in the views.py file

## 6 – How it could be improved?

###### In so many ways!

Here are a few possibilities:

-   Isolating the tables that interests us instead of the
    whole database.
-   Rebuild the table relationships by adding actual Foreign Keys,
    ManyToMany and OneToOne to improve database management.
-   If we precisely know which tables to import, then we could stop
    using inspectdb at all.
-   Make a better internal category management by putting them in
    a tree.
-   Add try-catches everywhere so it has a better error management and a
    better flow-control.
-   Edit it so that it doesn’t erase modifications in
    magentoStore/views.py every time you want to update the database.
-   Add checks, everywhere
-   And many more!



