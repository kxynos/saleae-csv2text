#!/usr/bin/python3
# 
# Copyright (c) 2019 Konstantinos Xynos
# 
# Version: 1.0 
# 
# saleae-csv2text is a parser for Saleae Logic csv exporter 
# 
# The code will parse csv data in ASCII only format that is 
# exported via Analyzers->Async Serial->Export as text/csv file 
# 
# File format: 
# Time [s],Value,Parity Error,Framing Error 
# 0.062163420000000,b,,
#
events = []

file_name = 'untitled.txt'

with open(file_name) as fp:
    text_list = fp.readlines()

text_list = [s.strip() for s in text_list]

for string in text_list:
    value = string.split(',')[1]
    value=value.replace("' '",' ')
    value=value.replace('\\n','\n')
    value=value.replace('\\r','\r')
    value=value.replace('\\t','\t')
    value=value.replace('COMMA',',')
    events.append(value)

if not 'Value' in events[0]:
    print("This is not the correct format.")
    exit(0)

text_output = ''.join(events[1:])
print(text_output)
