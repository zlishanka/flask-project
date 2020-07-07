import os
import sys
import time
import subprocess
from datetime import datetime

def print_info(msg):
    print (str(datetime.now()) + ' [Info] ' + msg)
    sys.stdout.flush()

def print_warning(msg):
    print (str(datetime.now()) + ' [Warning] ' + msg)
    sys.stdout.flush()

def print_error(msg):
    print (str(datetime.now()) + ' [Error] ' + msg)
    sys.stdout.flush()

def wait_for_next_run(time_secs): 
    time.sleep(time_secs)

def is_number(s):
    """ check if input string is numeric """
    """ s: string """
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_file_extention(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension

def get_file_name(file_path):
    tokens = file_path.split('/')
    if len(tokens) == 0:
        return None
    return tokens[-1]

def exec_command(cmd): 
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    text = p.stdout.read()
    retcode = p.wait()
    return retcode, text

def get_epoch_now():
    return int(time.time())

def get_epoch_now_ms():
    return int(round(time.time() * 1000)) 

def get_local_time_now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_utc_time_now():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def get_local_time_from_epoch(epoch_time): 
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time)) 

