#coding=utf-8
import pymysql
import time
from public.common.log import Log
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
success = "SUCCESS   "
fail = "FAIL   "
logger = Log()
#设置数据库用户名和密码
user='root';#用户名
pwd='123456';#密码
host='localhost';#ip地址
port=3306;#port端口
db='test';#所要操作数据库名字
charset='utf8'


def sql_print(msg):
    logger.info(msg)


conn=pymysql.connect(host=host,user=user,passwd=pwd,port=port,db=db,charset=charset)
#设置游标
# cursor = conn.cursor(dictionary=True)
cursor = conn.cursor()
#插入数据
#print(delete('table_name',{'list_name':'\'sddfdsfs\'}))
def mysql_insert(table_name,insert_dict):
  param='';
  value='';
  t1 = time.time()
  try:
      if(isinstance(insert_dict,dict)):
        for key in insert_dict.keys():
          param=param+key+","
          value=value+insert_dict[key]+','
        param=param[:-1]
        value=value[:-1]
        # print  param,value
      sql="insert into %s (%s) values(%s)"%(table_name,param,value)
      cursor.execute(sql)
      id=cursor.lastrowid
      conn.commit()
      print(id)
      sql_print("{0} insert to mysql: <{1}>, Spend {2} seconds".format(success, sql, time.time() - t1))
      return id



  except Exception:
      sql_print("{0} insert to mysql: <{1}>, Spend {2} seconds".format(fail, sql, time.time() - t1))
      raise
#删除数据
#print(insert('gelixi_help_type',{'type_name':'\'sddfdsfs\'','type_sort':'283'}))
def mysql_delete(table_name,where=''):
    t1 = time.time()
    try:
      if(where!=''):
        str='where'
        for key_value in where.keys():
          value=where[key_value]
          str=str+' '+key_value+'='+value+' '+'and'
        where=str[:-3]
        sql="delete from %s %s"%(table_name,where)
        # print sql
        cursor.execute(sql)
        conn.commit()
        sql_print("{0} delete to mysql: <{1}>, Spend {2} seconds".format(success, sql, time.time() - t1))
    except Exception:
        sql_print("{0} delete to mysql: <{1}>, Spend {2} seconds".format(fail, sql, time.time() - t1))
        raise

#取得数据库信息
# print(select({'table':'gelixi_help_type','where':{'help_show': '1'}},'type_name,type_id'))
def mysql_select(param,fields='*'):
    table=param['table']
    t1 = time.time()
    try:
          if ('where' in param):
              thewhere = param['where']
              if (isinstance(thewhere, dict)):
                  keys = thewhere.keys()
                  str = 'where';
                  for key_value in keys:
                      value = thewhere[key_value]
                      str = str + ' ' + key_value + '=' + value + ' ' + 'and'
                  where = str[:-3]
          else:
              where = ''

          sql = "select %s from %s %s" % (fields, table, where)
          # print sql
          cursor.execute(sql)
          result = cursor.fetchall()
          # print  result
          sql_print("{0} select to mysql: <{1}>, Spend {2} seconds".format(success, sql, time.time() - t1))
          return result

    except Exception:
      sql_print("{0} select to mysql: <{1}>, Spend {2} seconds".format(fail, sql, time.time() - t1))
      raise


#显示建表语句
#table string 表名
#return string 建表语句
def mysql_showCreateTable(table):
    sql='show create table %s'%(table)
    # print sql
    cursor.execute(sql)
    result=cursor.fetchall()[0]
    # print result[1]
    return result[1]
    # return result['Create Table']
#print(showCreateTable('gelixi_admin'))
#显示表结构语句
def mysql_showColumns(table):
    sql='show columns from %s '%(table)
    print(sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result[0])
    dict1={}
    for info in result:
        dict1[info['Field']]=info
    print(dict1)
    return dict1

if __name__ == '__main__':
    # mysql_insert('aa',{'a':'\'342134\'','b':'\'123341\''})
    # mysql_delete('aa',{'a':'1'})
    mysql_select({'table':'bb','where':{'a': '3','b': '3',}})
    # mysql_showCreateTable('aa')
    # mysql_showColumns('aa')