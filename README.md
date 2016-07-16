# CommonTornadoApis
使用python tornado框架编写后台api  
封装一个通用型模板，编写python tornado接口时，可以快速进行项目逻辑开发  
* 1.内容:  
    * 目前主要实现了User、Token实体类,token机制,以及用户注册、登录、详情等示例接口  
* 2.项目结构：  
    * main.py为服务器主程序,后续改动不大  
    * urls.py为所有接口访问路径和请求处理类的映射关系  
    * utils文件夹下为已经提取和将要提取的工具类集合  
    * models文件夹下为实体类  
    * common文件夹下为项目要用到的通用性文件,包括配置文件、数据库dao类  
    * apis文件夹下放的是所有接口模块  
* 3.TODO  
    * 项目结构优化、更多功能的完善  
    
   
    由于比较少编写后台接口,全都是自己所摸索出来的东西,实现逻辑仅做参考作用  
   
    部署教程: http://www.arche.name/?p=173
