#!/usr/bin/python3
# 
# Copyright (c) 2019 Konstantinos Xynos
# 
# Version: 1.0 
# 
# saleae-csv2text-decoded-protocols is a parser for Saleae Logic csv exporter 
# 
# The code will parse csv data in ASCII only format that is 
# exported via Decoded Protocols->Export search results 
# 
# File format: 
# Time [s], Analyzer Name, Decoded Protocol Result 
# 0.062163420000000,Async Serial,b 
#
events = []

file_name = 'untitled.csv'

with open(file_name) as fp:
    text_list = fp.readlines()

text_list = [s.strip() for s in text_list]

for string in text_list:
    value = string.split(',')[-1]
    value=value.replace("' '",' ')
    value=value.replace('\\n','\n')
    value=value.replace('\\r','\r')
    value=value.replace('\\t','\t')
    value=value.replace('COMMA',',')
    events.append(value)

if not 'Decoded Protocol Result' in events[0]:
    print("This is not the correct format.")
    exit(0)

text_output = ''.join(events[1:])
print(text_output)