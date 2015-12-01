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

from common.config import DEBUG
from utils.utils import Utils

########################################################################
class LoginHandler(BaseHandler.BaseHandler):
    """
    登陆接口示例
    TODO:token生成、功能提取，结构优化
    """     
    def get(self):
        user_id = self.get_argument("user_id","")
        user_pwd = self.get_argument("user_pwd","")
        
        self.session = dao.DBSession()
        try:
            user = self.session.query(User).filter(User.user_id==user_id,User.user_passwd==user_pwd).one() 
            #不要用下面的字符串拼接的方式查询，会造成sql注入。不信你可以试试。
            #user = self.session.query(User).filter('user_id=%s and user_passwd=%s'%(user_id,user_pwd)).one()
            if user:
                #生成token 算法 base64(md5(userid+userpwd) + salt)
                token = Utils.md5(user_id+user_pwd)+Utils.md5("arche")
                token = Utils.base64(token)
                new_token = self.session.query(Token).filter(Token.token==token).one()
                
                if not new_token:
                    new_token = Token(token=token,user_id=user_id,starttime=100,endtime=200)
                    self.session.add(new_token)
                else: #存在token
                    #更新时间
                    new_token = Token(token=token,user_id=user_id,starttime=200,endtime=300)
                    self.session.merge(new_token)
                self.session.commit() #注意别忘了commit
                
                dic = dict({"code":0,
                            "user_id":user_id,
                            "user_pwd":user_pwd,
                            "token":token})
            else:
                dic = dict({"code":1,
                            "reason":"username or passwd error"})      
            ret = Utils.dict2json(dic)
            self.write(ret)
        except Exception,e:
            print e
            dic = dict({"code":1,
                        "reason":"username or passwd error"})     
            ret = Utils.dict2json(dic)
            self.write(ret)
            
        