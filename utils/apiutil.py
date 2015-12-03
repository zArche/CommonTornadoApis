#coding:utf-8
"""
  Author:   --<>
  Purpose: 接口工具类
  Created: 2015/12/2
"""

from functools import wraps
import time
import dateutils
import sys
sys.path.append("..")
from models.Models import Token
from dateutils import DateUtil



########################################################################  
def logger(func):
    """
    函数修饰器，打印函数名字、参数、结果和执行所花时间
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        ts = time.time()
        result = func(*args,**kwargs)
        te = time.time()
        print "function      = %s" %func.__name__
        print "    arguments = %s %s" %(args,kwargs)
        print "    return    = %s" %result
        print "    time      = %.6f sec" %(te - ts)
        return result
    return wrapper



#----------------------------------------------------------------------
def isTokenValid(session,token,user_id):
    """
    判断token是否失效
    """
    ret = False
    try:
        token = session.query(Token).filter(Token.token==token,Token.user_id==user_id).one()
        if token.endtime > DateUtil.get_now_timestamp():
            ret =  True
    except:
        pass
    finally:
        return ret
    
        
        
    
    


        
    
    