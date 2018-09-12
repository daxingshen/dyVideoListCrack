#coding=utf-8
import os
import thriftpy
from settings import PRO_DIR
from thriftpy.rpc import make_client
import json

if __name__ == '__main__':
    kol_thrift = thriftpy.load(os.path.join(PRO_DIR, "./dolphin/service/douyin/data/kol_thrift.thrift"), module_name="kol_thrift_thrift")

    client = make_client(kol_thrift.KolServer, '127.0.0.1', 6000)
    data = client.fetch_all_works('58495581596')
    for item in json.loads(data):
        print(item)