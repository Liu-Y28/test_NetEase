##########################################################
#读取数据，查阅
test = open('D:/test_Yi.log').read()
#print(test)
#获得数据集中{}里包括的内容，并将其str属性转换为dict
trans_a = eval(test[test.index('{'):])
#提取所需信息
role_id = trans_a['role_id']
vip = trans_a['vip']
#设置vip字段缺失时赋默认值0
if not vip:
    vip = 0
#结果输出    
print("role_id =", role_id)
print("vip =" , vip)

print(type(dict_a))

##################################################################

#加载pakage
import pandas as pd
import numpy as np
import sqlite3
#创建样本表
db1 = sqlite3.connect("db1.db")
#conn = sqlite3.connect(db1)
c = db1.cursor()
create_table_sql = """ CREATE TABLE IF NOT EXISTS ods_p1_day (
                                        newaccount_dt str,
                                        account_id str NOT NULL,
                                        day_pay str,
                                        dt str
                                    ); """
c.execute(create_table_sql)
#插入虚拟数据
new_data = [(20180623,1,25,20180624),
             (20180622,2,0,20180624),
             (20180623,3,2,20180628),
             (20180622,4,0,20180624),
             (20180623,5,2,20180623)
            ]
c.executemany('INSERT or IGNORE INTO ods_p1_day VALUES (?,?,?,?)', new_data)
db1.commit()
#检查表
check = pd.read_sql('select * from ods_p1_day', db1)
print(check)
#now we can sql
#执行语句
sql1 = """select newaccount_dt date, count(newaccount_dt) 当日新增账号数,
count( case when (dt - newaccount_dt) <=1 then newaccount_dt end) 次日还有登录的账号数,
sum(case when (dt - newaccount_dt) =0 then day_pay else 0 end)/count(distinct newaccount_dt) ltv1,
sum(case when (dt - newaccount_dt) <=1 then day_pay else 0 end)/count(distinct newaccount_dt) ltv2
from ods_p1_day
group by newaccount_dt"""

#查看结果
result = pd.read_sql(sql1, db1)
print(result)


############################################################################






