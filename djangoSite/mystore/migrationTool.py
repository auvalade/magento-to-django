#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
project_name = str(sys.argv[1])
os.environ['DJANGO_SETTINGS_MODULE'] = project_name + '.settings'
import django
django.setup()
from django.conf import settings
import fileinput

# functions
def getDbAccess():
    # Get database informations
    mydb = settings.DATABASES['default']

    db_name = str(mydb['NAME'])
    db_user = str(mydb['USER'])
    db_password = str(mydb['PASSWORD'])
    db_host=mydb.get('HOST','')
    db_port=mydb.get('PORT','')
    if not db_host : db_host="localhost"
    if not db_port : db_port="3306"
    return db_name, db_user, db_password, db_host, db_port


def cleanModel():
    old_model = open('storeMagento/models.py', 'r')
    clean_model = open('storeMagento/models2.py', 'w')  
    for line in old_model:
             clean_model.write(line.replace("AutoField", "IntegerField"))
    old_model.close()
    clean_model.close()

def getTemplatesLocation():
    tpl_root = str(settings.TEMPLATES[0]['DIRS'][0])
    path_length = len(tpl_root.split('/'))
    if tpl_root[0] == '/' and path_length < 4:
         tpl_root = tpl_root[1:len(tpl_root)] 
    sys.stdout.write(tpl_root)
    return 0

def getStaticLocation():
    static_root = str(settings.STATIC_ROOT)
    path_length = len(static_root.split('/'))
    if static_root[0] == '/' and path_length < 4:
         static_root = static_root[1:len(static_root)] 
    sys.stdout.write(static_root)
    return 0

def loadDumpToDjango():
    db_name, db_user, db_password, db_host, db_port = getDbAccess()
    cmd_migrate_to_django = "mysql -h %s -P %s -u %s --password=%s %s < migrationTool/dumpMagentoTables.sql"%(db_host,db_port, db_user, db_password, db_name)

    os.system(cmd_migrate_to_django)
    
# Getting the parameters
arg_list=[]
function_dict={
    'loadDumpToDjango' : loadDumpToDjango,
    'getStaticLocation' : getStaticLocation,
    'getTemplatesLocation' : getTemplatesLocation,
    'cleanModel' : cleanModel,
}

for i in range(0,10):
    try:
        if i == 0:
            continue
        elif i == 1:
            fonction = str(sys.argv[i+1])
            continue
        arg_list.append(str(sys.argv[i+1]))
    except:
        break

try:
    function_dict[fonction](*arg_list)
except Exception as e:
    sys.stdout.write(str(e) + " No valid arguments")


