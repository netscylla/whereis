#!/usr/bin/env python3
#
# Whereis - Whois netrange miner
# Netscylla 2019 (c)
# GPLv3

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

if len(sys.argv) != 2:
  print("[-] Error: expected a keyword to search for...\n whereis.py [keyword]")
  exit(2)

keyword=sys.argv[1]

# Search ARIN
cmd="whois -h whois.arin.net 'z / *"+ keyword  +"*'"
r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
result,err=r.communicate()

arin_cidrs=return_ips(result)

#Search RIPE
cmd="whois -h whois.ripe.net -T inetnum "+ keyword
r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
result,err=r.communicate()

ripe_cidrs=return_ips(result)

#Search AFRINIC
cmd="whois -h whois.afrinic.net -T inetnum "+ keyword
r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
result,err=r.communicate()

afrinic_cidrs=return_ips(result)

#Search APNIC
cmd="whois -h whois.apnic.net -T inetnum "+ keyword
r = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
result,err=r.communicate()

apnic_cidrs=return_ips(result)

#add all cidrs together & uniq
cidr_list=arin_cidrs+ripe_cidrs+afrinic_cidrs+apnic_cidrs
f_list=unique(cidr_list)
for cidr in f_list:
  print(cidr)
