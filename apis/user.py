#coding:utf-8
"""
  Author:   --<>
  Purpose: 用户相关模块，包括注册、登录等操作
  Created: 2015/12/1
"""

import BaseHandler
import sys
sys.path.append("..")

from models.Models import User,Token
import common.dao as dao
from sqlalchemy.orm.exc import NoResultFound


from common.config import DEBUG
from utils.utils import Utils
from utils.dateutils import DateUtil

########################################################################
class LoginHandler(BaseHandler.BaseHandler):
    """
    登陆接口示例
    TODO:结构优化
    """     
    def get(self):
        user_id = self.get_argument("user_id","")
        user_pwd = self.get_argument("user_pwd","")
        
        self.session = dao.DBSession()
        try:
            query = self.session.query(User).filter(User.user_id==user_id,User.user_passwd==user_pwd).one() 
            #不要用下面的字符串拼接的方式查询，会造成sql注入。不信你可以试试。
            #query = self.session.query(User).filter('user_id=%s and user_passwd=%s'%(user_id,user_pwd)).one()
                
            #生成token 算法 base64(md5(userid+userpwd) + md5(timestampofnow))
            token = Utils.md5(user_id+user_pwd)+Utils.md5(str(DateUtil.get_now_timestamp()))
            token = Utils.base64(token)
                
            #更新token时间
            starttime = DateUtil.get_token_starttime()
            endtime = DateUtil.get_token_endtime()                
                
            new_token = Token(token=token,user_id=user_id,starttime=starttime,endtime=endtime)
                
            try:
                
                query = self.session.query(Token).filter(Token.user_id==user_id)
                
                #查询数据库中已有token值
                old_token = query.one()
                
                #存在token 更新   不存在则会抛异常
                query.update({Token.token:token,
                              Token.starttime:starttime,
                              Token.endtime:endtime})                
                    
            except Exception,e:
                print type(e)
                if type(e) is  NoResultFound:
                    self.session.add(new_token)                    
                        
            self.session.commit() #注意别忘了commit
                
            dic = dict({"code":0,
                    "user_id":user_id,
                    "user_pwd":user_pwd,
                    "token":token})
  

        except Exception,e:
            if type(e) is NoResultFound:
                dic = dict({"code":1,
                        "reason":"username or passwd error"})     

        finally:
            ret = Utils.dict2json(dic)
            self.write(ret)            
            
        