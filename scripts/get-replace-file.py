import re
import sys
import os

def replace_file(src_path, dst_path, host_ip_list):
  try:
    src_file = open(src_path, 'r')
    dst_file = open(dst_path, 'w')
    for line in src_file:
      for host, ip_addr in host_ip_list.items():
        line = re.sub('{' + host + '}', ip_addr, line)
      dst_file.write(line)
  finally:
    src_file.close()
    dst_file.close()
