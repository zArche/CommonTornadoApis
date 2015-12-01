
#coding:utf-8
"""
  Author:   --<>
  Purpose: 数据库操作类
  Created: 2015/12/1
"""

from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

import sys
sys.path.append("..")

from common.config import DB_HOST,DB_PORT
from common.config import DB_USERNAME,DB_PASSWD
from common.config import DB_NAME,DB_USERTABLENAME,DB_TOKENTABLENAME
from common.config import DEBUG


DB_CONNECT_STRING = 'mysql+mysqlconnector://%s:%s@%s:%s/%s'%(DB_USERNAME,DB_PASSWD,DB_HOST,DB_PORT,DB_NAME)

Base = declarative_base()

engine = create_engine(DB_CONNECT_STRING,echo=DEBUG)

DBSession = sessionmaker(bind=engine)