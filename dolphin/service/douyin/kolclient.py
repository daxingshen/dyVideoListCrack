# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import thriftpy2 as thriftpy
from thrift_connector import ClientPool, ThriftPyCyClient

from settings import PRO_DIR






kol_thrift = thriftpy.load(os.path.join(PRO_DIR, "./dolphin/service/douyin/data/kol_thrift.thrift"), module_name="kol_thrift_thrift")
connection_pool = ClientPool(
    kol_thrift.KolServer,
    '192.168.1.12',
    7000,
    timeout=6,
    connection_class=ThriftPyCyClient
)


if __name__ == '__main__':
    data = connection_pool.fetch_all_works('89852104754')
    print(data)
    for item in json.loads(data):
        print(item)
