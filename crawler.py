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
        database='t',
        charset='utf8mb4'
    )
    print('Mysql连接成功')
except pymysql.MySQLError as e:
    print('Mysql连接失败:', e)
    sys.exit(1)

sqlJob = "INSERT INTO jobs (film_name, director, initialReleaseDate, rating_num) VALUES (%s, %s, %s,%s)"
sqlCom = "INSERT INTO companies (film_name, director, initialReleaseDate, rating_num) VALUES (%s, %s, %s,%s)"

browser = ChromiumPage()
browser.listen.start('joblist.json')
browser.get('https://www.zhipin.com/web/geek/jobs?query=python&city=101020100')
time.sleep(3)

for _ in range(5):
    time.sleep(random.uniform(0.5, 2.5))
    r = browser.listen.wait()
    jsData = r.response.body

    if jsData is None:
        print(f'第{_ + 1}次数据采集,json数据未采集到，跳过')
        continue

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
        skills = "//".join(i['skills'])
        jobLine = [jobName, salaryDesc, jobDegree, areaDistrict, businessDistrict, brandName, jobExperience, skills]

        # companies表
        brandStageName = i['brandStageName']
        brandIndustry = i['brandIndustry']
        brandScaleName = i['brandScaleName']
        companyLine = [brandName, brandStageName, brandIndustry, brandScaleName]

        print(jobLine)
        print(companyLine)

    print(f'已采集第{_ + 1}组的15条数据')
    browser.scroll.to_bottom()

browser.close()
