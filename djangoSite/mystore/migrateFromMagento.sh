#!/bin/bash
# My migration script

source migrationTool/config.cfg
echo "Hello !"
echo "Before we start, please make sure of the following:"
echo "- You are using Python 3 (3.4 or 3.5) and Django 1.9i, you have pip3 installed"
echo "- You are using a MySQL database (> v5)"
echo "- You have pymysql installed (pip3 install pymysql)"
echo "- The config file is correctly setup with database information"
echo ""
echo -n  "Continue ? (y/n)"

read -r confirmation

if [ $confirmation != 'y' ]; then 
    echo "Giving up"
    exit 1
fi 
echo -n "Dumping magento tables ..."
mysqldump -h $cfg_host -P $cfg_port -u $cfg_user -p$cfg_password $cfg_dbname  > migrationTool/dumpMagentoTables.sql
echo " OK"

echo "The next step will update your current django MySQL database with the magento dump. If you have done this before, the previous tables are going to be erased.Please dump your database before proceeding."
echo ""
echo -n "Are you ready ? (y/n)"
read -r confirmation
if [ $confirmation != 'y' ]; then 
    echo "Giving up"
    exit 1
fi
echo -n "Loading Magento dump into Django Database ... "
python3 migrationTool.py $cfg_project_name loadDumpToDjango
echo "OK"
echo -n "Creating new store Application 'storeMagento' ... "
python3 manage.py startapp storeMagento
if [ -d 'storeMagento' ]; then
    echo "OK"
    echo -n "Getting static and template folders location ... "
    static_location=$(python3 migrationTool.py $cfg_project_name getStaticLocation)
    templates_location=$(python3 migrationTool.py $cfg_project_name getTemplatesLocation)
    echo "OK"
    echo -n "Moving files to their new location ... "
    cp migrationTool/djangoApp/storeMagento/__init__.py storeMagento/
    cp migrationTool/djangoApp/storeMagento/views.py storeMagento/
    cp -a migrationTool/djangoApp/static/. $static_location
    cp -a migrationTool/djangoApp/templates/. $templates_location
    echo "OK"
fi
echo -n "Generating model from database ... "
python3 manage.py inspectdb > storeMagento/models.py
echo "OK"
echo -n "Cleaning model ... "
touch storeMagento/models2.py
python3 migrationTool.py $cfg_project_name cleanModel > storeMagento/models2.py
rm storeMagento/models.py
mv storeMagento/models2.py storeMagento/models.py 
echo "OK"
echo -n "Making migrations ... "
service apache2 restart
echo "DONE ! Plase add storeMagento to your installed apps and change database  and check apache configuration for the links to be correctly loaded, puis faire les migrations de tout"


