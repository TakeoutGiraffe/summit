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
    #print(query)
    conn=connect()
    cur=conn.cursor()
    cur.execute(query)
    conn.commit()

def get_query(query):
    #print(query)
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
    now = datetime.datetime.now()
    execute(f"INSERT INTO tasks (scriptid, status, runid) VALUES ({id},0,'{runid}')")
    return runid
  
def get_pending_tasks():
    return get_query(f"SELECT taskid, status FROM tasks WHERE status=0")

def get_tasks_for_taskview():
    return get_query(f"SELECT t.taskid, s.name, e.value, t.starttime, t.finishtime FROM tasks t JOIN scripts s ON t.scriptid = s.scriptid JOIN status_strings e on e.table='tasks' and e.field='status' and e.enumid = t.status")

def set_task_start(taskid):
    execute(f"UPDATE tasks SET starttime=now() where taskid={taskid}")

def set_task_finish(taskid):
    execute(f"UPDATE tasks SET finishtime=now() where taskid={taskid}")

def set_task_status(taskid, newstatus):
    execute(f"UPDATE tasks SET status={newstatus} WHERE taskid={taskid}")

def set_task_output(taskid, output):
    execute(f"UPDATE tasks SET output='{output}' WHERE taskid={taskid}")

def get_task_details(taskid):
    return get_query(f"SELECT s.scriptid,s.code FROM scripts s JOIN tasks t ON s.scriptid = t.scriptid WHERE taskid = {taskid}")

def get_task_output(taskid):
    return get_query(f"SELECT t.taskid,t.output,s.name FROM tasks t JOIN scripts s ON t.scriptid = s.scriptid where taskid = {taskid}")

if __name__ == '__main__': 
    k = get_scripts();
    print(k)