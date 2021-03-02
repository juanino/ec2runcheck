#!/usr/bin/env python3
import boto3

#ec2 = boto3.resource('ec2')
#tag = ec2.Tag('resource_id','key','value')

import csv
import pprint

def check_running(instance,name):
    ec2_resource = boto3.resource('ec2', region_name='us-east-1')
    try:
        instance = ec2_resource.Instance(instance)
        if instance.state['Name'] == 'running':
            print(instance, "running", name)
        else:
            print(instance, "not running", name)
    except:
        print(instance, "not found", name)



pp = pprint.PrettyPrinter(indent=4)
with open('somefile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #pp.pprint(row)
        # assumes 10 items, we only care about the first 3
        (instance,name,service,d,e,f,g,h,l,q) = row
        line_count += 1
        check_running(instance,name)
    print(f'Processed {line_count} lines.')

