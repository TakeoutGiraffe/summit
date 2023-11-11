#!/usr/bin/python 
from configparser import ConfigParser 
import psycopg2 
import uuid
import datetime
  
  
def config(filename='database.ini', section='postgresql'): 
    # create a parser 
    parser = ConfigParser() 
    # read config file 
    parser.read(filename) 
  
    # get section, default to postgresql 
    db = {} 
    if parser.has_section(section): 
        params = parser.items(section) 
        for param in params: 
            db[param[0]] = param[1] 
    else: 
        raise Exception('Section {0} not found in the {1} file'.format(section, filename)) 
  
    return db
  
def connect(): 
    """ Connect to the PostgreSQL database server """
    conn = None

    # read connection parameters 
    params = config() 
  
    # connect to the PostgreSQL server 
    conn = psycopg2.connect(**params) 
          
    return conn
       
def execute(query):
    print(query)
    conn=connect()
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()

def get_query(query):
    print(query)
    conn=connect()
    cur=conn.cursor()
    cur.execute(query)
    ds=cur.fetchall()
    conn.close()
    return ds

def get_script_with_id(id):
    return get_query(f"SELECT scriptid,name,code FROM Scripts WHERE scriptid = {id}")

def get_scripts():
    return get_query("SELECT scriptid,name FROM Scripts")

def save_script(id, code):
    return execute(f"UPDATE scripts SET code='{code}' where scriptid={id}")

def add_task(id):
    runid = uuid.uuid4()
    now = datatime.datetime.now()
    return execute(f"INSERT INTO tasks (scriptid, starttime, status, runid) VALUES ({id,now,0,runid})")
  
if __name__ == '__main__': 
    k = get_scripts();
    print(k)