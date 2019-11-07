# -*- coding: utf-8 -*-
import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import sys
import thriftpy2 as thriftpy
from thriftpy2.rpc import make_server
from thriftpy2.thrift import TProcessor
from thriftpy2.protocol import TCyBinaryProtocolFactory
from thriftpy2.transport import TCyBufferedTransportFactory
from dolphin.service.douyin.kol import kol
from settings import PRO_DIR


class KolDispatcher(object):
    def ping(self):
        return "pong"

    # def fetch_all_works(self, uid):
    #     return json.dumps(kol.fetch_all_video(uid))

    def fetch_sig_and_dytk(self, uid, dytk=None, tac=None):
        try:
            sig, dytk, ua = kol.get_sig_dytk(uid, dytk=dytk, tac=tac)
            r = {
                'sig': sig,
                'dytk': dytk,
                'ua': ua
            }
        except BaseException as e:
            import traceback
            traceback.print_exc()
            return json.dumps({'msg': str(e)})
        return json.dumps(r)

    def checkout_user_agent(self):
        return kol.checkout_user_agent()


if sys.platform == 'win32':
    kol_thrift = thriftpy.load(os.path.join(PRO_DIR, '.\\dolphin\\service\\douyin\\data\\kol_thrift.thrift'), module_name='kol_thrift_thrift')
else:
    kol_thrift = thriftpy.load(os.path.join(PRO_DIR, './dolphin/service/douyin/data/kol_thrift.thrift'), module_name='kol_thrift_thrift')

app = TProcessor(kol_thrift.KolServer, KolDispatcher())
# server = TProcessor(kol_thrift.KolServer, KolDispatcher())
#
if __name__ == '__main__':
    server = make_server(kol_thrift.KolServer, KolDispatcher(), '0.0.0.0', 7000, proto_factory=TCyBinaryProtocolFactory(), trans_factory=TCyBufferedTransportFactory())
    server.serve()

    # gunicorn_thrift dolphin.service.douyin.kolserver:app -k thriftpy_sync -b 0.0.0.0:6000 -w 4 --thrift-protocol-factory thriftpy.protocol:TCyBinaryProtocolFactory --thrift-transport-factory thriftpy.transport:TCyBufferedTransportFactory --thrift-client-timeout=5
    # gunicorn_thrift dolphin.service.douyin.kolserver:app --bind 0.0.0.0:7000 -w 10 -k thriftpy_gevent  --timeout 10  --thrift-protocol-factory thriftpy2.protocol:TCyBinaryProtocolFactory --thrift-transport-factory thriftpy2.transport:TCyBufferedTransportFactory --error-logfile aa.log -D -p douyin_server.pid