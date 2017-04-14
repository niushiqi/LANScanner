#-*- coding: utf-8 -*- 
#author: orangleliu date: 2014-11-12 
#python2.7.x ip_scaner.py
  
import platform 
import sys 
import os 
import time 
import _thread 
  
def get_os(): 
  ##获取操作系统类型
  os = platform.system() 
  if os == "Windows": 
    return "n"
  else: 
    return "c"
    
def ping_ip(ip_str): 
  cmd = ["ping", "-{op}".format(op=get_os()), 
      "1", ip_str] 
  #os.popen就可以读出执行的内容 readlines读取整个文件
  output = os.popen(" ".join(cmd)).readlines() 
    
  flag = False
  #将元组转换为列表
  for line in list(output): 
    if not line: 
      continue
      #upper:将字符串中的小写字母转为大写字母 find:返回位置
    if str(line).upper().find("TTL") >=0: 
      flag = True
      break
  if flag: 
    print("ip: %s is ok ***"%ip_str)
  
def find_ip(ip_prefix): 
  for i in range(1,256): 
    ip = '%s.%s'%(ip_prefix,i) 
    #创建一个新的线程
    _thread.start_new_thread(ping_ip, (ip,)) 
    time.sleep(0.3) 

#函数的开始部分 10.0.1.38
if __name__ == "__main__": 
#time.ctime获取当前时间, Tue Feb 17 10:00:18 2014
  print("start time %s"%time.ctime())
  commandargs = sys.argv[1:] 
#join字符连接操作
  args = "".join(commandargs)   
#split指定分隔符对字符串进行切片|line[:-1]去除了最后一个字符后剩下的部分。
  ip_prefix = '.'.join(args.split('.')[:-1]) 
  find_ip(ip_prefix) 
  print("end time %s"%time.ctime())