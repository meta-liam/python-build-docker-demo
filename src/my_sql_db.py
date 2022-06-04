import my_config as my_config
from mysqldb import *
import datetime

def insert_ads_data(list,cursor,task_id):
    l = len(list)
    isCommit =False
    for i in range(l): # 100
        li= list[i]
        sql3 = 'INSERT INTO `ads_bing_location_report` (`TimePeriod`,`AccountId`,`AccountName`,`CampaignId`,`CampaignName`,`AdGroupId`,`AdGroupName`,`LocationId`,`Country`,`Clicks`,`Impressions`,`DeviceType`,`Network`,`Ctr`,`AverageCpc`,`Spend`,`Conversions`,`Revenue`,`SaveTime`) ' \
        'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (li[0],ii(li[1]),li[2],ii(li[3]),li[4],ii(li[5]),li[6],ii(li[7]),li[8],ii(li[9]),ii(li[10]),li[11],li[12],li[13],flo(li[14]),flo(li[15]),ii(li[16]),flo(li[17]),task_id)
        #print(values)
        cursor.insert(sql3,values=values)
        if i % 500 == 0:
            cursor.conn.commit()  # 分批入库
            isCommit = True
            print('[INFO]commit sql:',i)
        else:
            isCommit = False 
    if l> 0 and not isCommit:  
        cursor.conn.commit()

def insert_log(cursor,task_id):
    date = datetime.datetime.now()
    # insert log
    sql1 = 'INSERT INTO `task_ads_bing`( `created_at`, `query_options`, `status`, `type`, `task_id`, `get_num`) VALUES (%s, %s, %s, %s,%s, %s);'
    values1 =(date, my_config.query_options, 0, "",task_id, 0)
    #print(sql1)
    cursor.insert(sql1,values=values1)
    cursor.conn.commit()

def update_log(cursor,num,result,task_id):
    # update log
    sql8 = f'update `task_ads_bing` set `updated_at`="{datetime.datetime.now()}" , `status`=1 , `get_num`={num} ,result="{result}"  where `task_id`= {task_id} ;'
    #print(sql8)
    cursor.execute(sql8)

def delete_old_ads(cursor,num,task_id):
    # 删除 TimePeriod
    if (num> 0):
        sql2 = f'delete from `ads_bing_location_report` WHERE `TimePeriod` >= "{my_config.start_time}" and `TimePeriod` <= "{my_config.end_time}" and `SaveTime` <> "{task_id}" ; '
        #print(sql2)
        cursor.execute(sql2)

# int
def ii(s):
    return int(s)

def flo(s):
    ss = s.replace(",", "")
    return float(ss)
