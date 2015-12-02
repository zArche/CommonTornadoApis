#coding:utf-8
"""
  Author:   --<>
  Purpose: 日期操作工具
  Created: 2015/12/2
"""

import datetime
import time
import sys
sys.path.append("..")

from common.config import TOKEN_VALID_TIME


########################################################################
class DateUtil:

    token_starttime = 0
    
    @staticmethod
    def get_now(format):
        '''
        以format格式返回当前时间字符串
        '''
        t = datetime.datetime.now()
        return t.strftime(format)
    
    @staticmethod
    def get_now_timestamp():
        """
        获取当前时间的时间戳
        """
        return int(time.time())
    
    @staticmethod
    def get_token_starttime():
        """
        获取token开始时间
        """
        return DateUtil.get_now_timestamp()

    @staticmethod
    def get_token_endtime():
        """
        获取token结束时间
        """
        return DateUtil.get_now_timestamp() + TOKEN_VALID_TIME


if __name__ == "__main__":
    format = '%Y-%m-%d %X'
    print DateUtil.get_now(format)
    print DateUtil.get_now_timestamp()
    print DateUtil.get_token_starttime()
    print DateUtil.get_token_endtime()
    