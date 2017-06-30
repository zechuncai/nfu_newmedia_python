# -*- coding: utf-8 -*- 

class shenxiao_from_to (object):

    def __init__(self, fn='data/shengxiao_data.tsv'):
       import csv
       with open(fn, 'r', encoding='utf8') as csvfile:
           reader = csv.DictReader(csvfile, fieldnames=['shenxiao_from', 'shenxiao_to'], delimiter='\t')
           fieldnames = reader.fieldnames

           list_dict_shenxiao = []
           for row in reader:
                  list_dict_shenxiao.append(dict(row))

           self.find_shenxiao = {d['shenxiao_from']:d['shenxiao_to'] for d in list_dict_shenxiao}

    def country_name(self, shenxiao_from=''):
        shenxiao_to =  self.find_shenxiao.get(shenxiao_from, None)
        return (shenxiao_to)