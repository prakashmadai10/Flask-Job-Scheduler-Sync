import pandas as pd
from datetime import datetime
from DB_CONNECT.connect import DBECC,DBCRM

def ecc_pso_fetch():
    db = DBECC()
    sql = """ select query """
    db.connect()
    result = db.cur.execute(sql)
    result2 = result.fetchall()
    db.close()
    return result2

def ecc_pso_insert(res):
    db1=DBCRM()
    db1.connect()

    for row in res:
        sql1="insert into REPORT.DBO.ECC_PSO(SSNDT,CURR_CD,SLAB,STATUS,tot_cnt,tot_amt,sync_date,remarks) values('{}',{},'{}','{}',{},{},'{}','{}');".format(row[0],row[1],row[2],row[3],row[4],row[5],datetime.now().strftime('%d-%b-%y'),'sync_completed')

        db1.cur.execute(sql1)
        db1.cur.commit()
    print('ECC PSO is synced successfully')
    db1.close()
    



