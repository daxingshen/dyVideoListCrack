# -*- coding: utf-8 -*-
import json
import os

import sys
import thriftpy
from thriftpy.rpc import make_server
from thriftpy.thrift import TProcessor
from thriftpy.protocol import TCyBinaryProtocolFactory
from thriftpy.transport import TCyBufferedTransportFactory
from dolphin.service.douyin.kol import kol
from settings import PRO_DIR


class KolDispatcher(object):
    def ping(self):
        return "pong"

    def fetch_all_works(self, uid):
        kol.set_user(uid)
        return json.dumps(kol.fetch_all_video())

    def checkout_user_agent(self):
        return kol.checkout_user_agent()


if sys.platform == 'win32':
    kol_thrift = thriftpy.load(os.path.join(PRO_DIR, '.\\dolphin\\service\\douyin\\data\\kol_thrift.thrift'), module_name='kol_thrift_thrift')
else:
    kol_thrift = thriftpy.load(os.path.join(PRO_DIR, './dolphin/service/douyin/data/kol_thrift.thrift'), module_name='kol_thrift_thrift')

app = TProcessor(kol_thrift.KolServer, KolDispatcher())

#
if __name__ == '__main__':
    server = make_server(kol_thrift.KolServer, KolDispatcher(), '0.0.0.0', 6000, proto_factory=TCyBinaryProtocolFactory(), trans_factory=TCyBufferedTransportFactory())
    server.serve()

    # gunicorn_thrift dolphin.service.douyin.kolserver:app -k thriftpy_sync -b 0.0.0.0:6000 -w 4 --thrift-protocol-factory thriftpy.protocol:TCyBinaryProtocolFactory --thrift-transport-factory thriftpy.transport:TCyBufferedTransportFactory --thrift-client-timeout=5