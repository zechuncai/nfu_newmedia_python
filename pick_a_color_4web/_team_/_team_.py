# -*- coding: utf-8 -*-
import csv
with open('_team_.tsv', encoding='utf8') as f:
    
        print ('\t'.join([r[k] for k in reader.fieldnames]) )
