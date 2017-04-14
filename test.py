#-*- coding: utf-8 -*- 
#author: orangleliu date: 2014-11-12 
#python2.7.x ip_scaner.py
  
import platform 
import sys 
import os 
import time 
import _thread 
  
def get_os(): 
  ##��ȡ����ϵͳ����
  os = platform.system() 
  if os == "Windows": 
    return "n"
  else: 
    return "c"
    
def ping_ip(ip_str): 
  cmd = ["ping", "-{op}".format(op=get_os()), 
      "1", ip_str] 
  #os.popen�Ϳ��Զ���ִ�е����� readlines��ȡ�����ļ�
  output = os.popen(" ".join(cmd)).readlines() 
    
  flag = False
  #��Ԫ��ת��Ϊ�б�
  for line in list(output): 
    if not line: 
      continue
      #upper:���ַ����е�Сд��ĸתΪ��д��ĸ find:����λ��
    if str(line).upper().find("TTL") >=0: 
      flag = True
      break
  if flag: 
    print("ip: %s is ok ***"%ip_str)
  
def find_ip(ip_prefix): 
  for i in range(1,256): 
    ip = '%s.%s'%(ip_prefix,i) 
    #����һ���µ��߳�
    _thread.start_new_thread(ping_ip, (ip,)) 
    time.sleep(0.3) 

#�����Ŀ�ʼ���� 10.0.1.38
if __name__ == "__main__": 
#time.ctime��ȡ��ǰʱ��, Tue Feb 17 10:00:18 2014
  print("start time %s"%time.ctime())
  commandargs = sys.argv[1:] 
#join�ַ����Ӳ���
  args = "".join(commandargs)   
#splitָ���ָ������ַ���������Ƭ|line[:-1]ȥ�������һ���ַ���ʣ�µĲ��֡�
  ip_prefix = '.'.join(args.split('.')[:-1]) 
  find_ip(ip_prefix) 
  print("end time %s"%time.ctime())