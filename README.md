# Boss直聘数据可视化项目
## python配置
python3.12.10  
`pip install pyecharts pymysql SQLAlchemy pandas DrissionPage`
## Mysql数据库配置
新建bossdata数据库，打开console  

jobs表

`create table jobs (
    id int unsigned not null auto_increment primary key comment '职位ID，自增主键',
    jobName varchar(100) not null comment '职位名称，如：python数据分析',
    salaryDesc varchar(50) comment '薪资描述，如：6-8K',
    jobDegree varchar(50) comment '学历要求，如：本科',
    areaDistrict varchar(50) comment '区域区，如：杨浦区',
    businessDistrict varchar(50) comment '商圈，如：五角场',
    brandName varchar(100) not null comment '公司品牌名称',
    jobExperience varchar(50) comment '工作经验要求，如：1年以内',
    skills text comment '所需技能列表 (存储为JSON或逗号分隔)',
    securityId varchar(255) comment '安全ID',
    encryptJobId varchar(100) unique comment '加密职位ID'
) engine=InnoDB default charset=utf8mb4 comment='职位信息表';`

companies表

`create table companies (
    id int unsigned not null auto_increment primary key comment '职位ID，自增主键',
    brandName varchar(20) not null comment '品牌名称',
    brandStageName varchar(50) comment '品牌阶段名称',
    brandIndustry varchar(100) comment '品牌所属行业',
    brandScaleName varchar(50) comment '品牌规模名称',
    longitude decimal(10, 7) comment '品牌办公地点经度',
    latitude decimal(10, 7) comment '品牌办公地点纬度',
    welfareList text comment '品牌提供的福利列表'
) engine=InnoDB default charset=utf8mb4 comment='企业信息表';`

words表

`create table words (
    id int unsigned not null auto_increment primary key comment 'ID，自增主键',
    word longtext comment '存储用于生成词云的长文本内容'
) engine=InnoDB default charset=utf8mb4 comment='词云数据存储表';`

## 启动爬虫
crawler1.py启动前需要给DrissionPage配置cookies (crawler2.py不用)    
数据入库截图
<img width="1336" height="799" alt="image" src="https://github.com/user-attachments/assets/309bd1e6-2055-4abd-8ced-ad0290d2d224" />

## 最终效果
<img width="1903" height="607" alt="image" src="https://github.com/user-attachments/assets/ef8f8e2e-d65a-47d2-8baf-680d2b6a958d" />

<img width="1903" height="603" alt="image" src="https://github.com/user-attachments/assets/5d21d926-1bb3-4133-b224-1f1a88ed29f0" />

## 预览网页
`https://luxuryend.github.io/Boss/boss%E7%9B%B4%E8%81%98%E6%95%B0%E6%8D%AE%E5%8F%AF%E8%A7%86%E5%8C%96.html`
