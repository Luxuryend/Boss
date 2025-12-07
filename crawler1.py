import sys
import time
import random
import pymysql
from DrissionPage import ChromiumPage

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

sqlJob = "insert into jobs (jobName, salaryDesc, jobDegree, areaDistrict, businessDistrict, brandName, jobExperience, skills, securityId, encryptJobId) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
sqlCom = "insert into companies (brandName, brandStageName, brandIndustry, brandScaleName, longitude, latitude, welfareList) values (%s, %s, %s, %s, %s, %s, %s)"

browser = ChromiumPage()
browser.listen.start('joblist.json')
browser.get('https://www.zhipin.com/web/geek/jobs?query=python&city=101020100')
time.sleep(3)

with conn.cursor() as cursor:
    for _ in range(20):
        time.sleep(random.uniform(0.5, 2.5))
        r = browser.listen.wait()
        jsData = r.response.body

        if jsData is None:
            print(f'第{_ + 1}次数据采集,json数据未采集到，跳过')
            continue

        jData = []
        cData = []
        jList = jsData['zpData']['jobList']

        for i in jList:
            # jobs表
            jobName = i['jobName']
            salaryDesc = i['salaryDesc']
            jobDegree = i['jobDegree']
            areaDistrict = i['areaDistrict']
            businessDistrict = i['businessDistrict']
            brandName = i['brandName']
            jobExperience = i['jobExperience']
            skills = '//'.join(i['skills'])
            securityId = i['securityId']
            encryptJobId = i['encryptJobId']
            jobLine = [jobName, salaryDesc, jobDegree, areaDistrict, businessDistrict, brandName, jobExperience, skills,
                       securityId, encryptJobId]
            jData.append(jobLine)

            # companies表
            brandStageName = i['brandStageName']
            brandIndustry = i['brandIndustry']
            brandScaleName = i['brandScaleName']
            longitude = i['gps']['longitude']
            latitude = i['gps']['latitude']
            welfareList = '//'.join(i['welfareList'])
            companyLine = [brandName, brandStageName, brandIndustry, brandScaleName, longitude, latitude, welfareList]
            cData.append(companyLine)

        cursor.executemany(sqlJob, jData)
        cursor.executemany(sqlCom, cData)
        conn.commit()

        print(f'已采集第{_ + 1}组的15条数据')
        browser.scroll.to_bottom()

browser.close()
print('over')
