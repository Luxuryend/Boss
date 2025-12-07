import sys
import time
import random
import pymysql
from DrissionPage import Chromium

start_time = time.time()

try:
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='bossdata',
        charset='utf8mb4'
    )
    print('Mysql连接成功')
except pymysql.MySQLError as e:
    print('Mysql连接失败:', e)
    sys.exit(1)

browser = Chromium()
tab = browser.latest_tab

with conn.cursor() as cursor:
    for _ in range(1, 81):
        sql = f'select securityId, encryptJobId from jobs where id = {_}'
        cursor.execute(sql)
        r = cursor.fetchone()
        url = f'https://www.zhipin.com/job_detail/{r[1]}.html?securityId={r[0]}'

        time.sleep(random.uniform(1.5, 4))
        tab.get(url)
        texts = tab.eles('x://div[@class="job-sec-text"]')

        s = ''
        for i in texts:
            s += i.text
        sql2 = f'insert into words (word) values ("{s}");'
        cursor.execute(sql2)
        conn.commit()
        print(f'已写入第{_}条数据')

browser.quit()
end_time = time.time()
print(f'共耗时{end_time - start_time}秒')
print('over')
