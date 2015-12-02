#coding:utf-8

"""
配置文件
"""



DEBUG = True

DB_USERNAME = "arche" #数据库用户名
DB_PASSWD = "zzf778546" 

DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "test"
DB_USERTABLENAME = "users" #User实体类对应的数据库表名
DB_TOKENTABLENAME = "token" #Token实体类对应的数据库表名

TOKEN_VALID_TIME = 60*60 #token有效时间 单位为秒
