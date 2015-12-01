
#coding:utf-8
"""
  Author:   --<>
  Purpose: 实体类
  Created: 2015/12/1
"""
import sys
sys.path.append("..")

from common.dao import *

########################################################################
class User(Base):
    """"""
    __tablename__ = DB_USERTABLENAME
    user_id = Column(Integer,primary_key=True)
    user_name = Column(String(20))
    user_passwd = Column(String(45))

    
########################################################################
class Token(Base):
    """
    接口token值
    """
    __tablename__ = DB_TOKENTABLENAME
    token = Column(String(45),primary_key=True)
    user_id = Column(Integer)
    starttime = Column(Integer)
    endtime = Column(Integer)

        
        
    
    
    

if __name__ == "__main__":

    if DEBUG:
        print DB_CONNECT_STRING
    #session = DBSession()
    #user = User(id=4,name="arche1")
    #session.add(user)
    #session.commit()
    #session.close()
    
    session = DBSession()
    user = session.query(User).filter(User.user_id==1).one()
    print user.user_name
    session.commit()
    session.close()
    
    
    session = DBSession()
    token = session.query(Token)[0]
    print token.token
    session.commit()
    session.close()
            

        
        
    
    