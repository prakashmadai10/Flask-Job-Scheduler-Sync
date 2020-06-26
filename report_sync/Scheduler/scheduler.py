from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import atexit
import time
import pandas as pd
from Sync.ICC.test_slab import test_slab_fetch,test_slab_insert
from Sync.ICC.test_pso import test_pso_fetch,test_pso_insert
from datetime import datetime


scheduler = BackgroundScheduler()

def sync_date():
    today = datetime.today()
    return today

@scheduler.scheduled_job('cron',hour='8',minute ='25',misfire_grace_time=120)
def ecc_Sync():
      
  print("Sync Started at",sync_date())
 
  result8 = test_slab_fetch()
  test_slab_insert(result8)    
  result9 = test_pso_fetch()
  test_pso_insert(result9)
  print("-------ALL ECC SYNC COMPLETED ---------")
   
  return 0

