#!/usr/bin/env python3
import sys
import re
import ipaddress
import subprocess

def unique(list1):
  unique_list = []
  for x in list1:
    if x not in unique_list:
      unique_list.append(x)
  return unique_list

def return_ips(iplist):
  cidr_list=[]
  ip_list=re.findall( r'(\d+\.\d+\.\d+\.\d+)\s-\s(\d+\.\d+\.\d+\.\d+)',str(iplist),re.M|re.I)
  for ip in ip_list:
    startip = ipaddress.IPv4Address(ip[0])
    endip = ipaddress.IPv4Address(ip[1])
    cidr=re.findall( r'(\d+\.\d+\.\d+\.\d+/\d+)',str([ipaddr for ipaddr in ipaddress.summarize_address_range(startip,endip)]),re.I)
    cidr_list.append(cidr[0])
  return cidr_list

keyword=sys.argv[1]


# Search ARIN
cmd="whois -h whois.arin.net 'z / *"+ keyword  +"*'"
r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
result,err=r.communicate()

cidrs=[]
cidrs=return_ips(result)

#print(cidrs)

#Search RIPE
cmd="whois -h whois.ripe.net -T inetnum "+ keyword
r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
result,err=r.communicate()

temp_cidrs=return_ips(result)

cidr_list=cidrs+temp_cidrs
f_list=unique(cidr_list)
for cidr in f_list:
  print(cidr)
