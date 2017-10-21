mysqltools遵循的标准明细

- [mysqltools遵循的标准](#mysqltools遵循的标准)
    - [mysql遵循的标准](#mysql遵循的标准)
        - [mysql安装标准](#mysql安装标准)
        - [mysql配置文件标准](#mysql配置文件标准)
        - [mysql数据目录标准](#mysql数据目录标准)
        - [mysql其它文件标准](#mysql其它文件标准)
    

# mysql遵循的标准

## mysql安装标准
- 为了方便自动化处理，mysql在安装介质上使用的是通用二进制包(Linux - Generic)
- 软件安装在/usr/local/目录下

## mysql配置文件标准
- 配置文件使用默认的/etc/my.cnf

## mysql数据目录标准
- 默认mysql数据目录为/database/mysql/data/3306

## mysql其它文件标准
- 除socket文件保存在/tmp/目录下处，所有的其它文件都保存在数据目录下