from typing import Dict
import requests

from webScrap_v2 import util

class Request_price:

    @util.randomSleep
    def request(self, work:Dict):
        trdDd = work.get('trdDd')

        URL = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'

        data = {
            'bld': 'dbms/MDC/STAT/standard/MDCSTAT01501',
            'locale': 'ko_KR',
            'mktId': 'ALL',
            'trdDd': trdDd,
            'share': '1',
            'money': '1',
            'csvxls_isNo': 'false',
        }

        r = requests.post(url=URL, data=data)

        return r.json()

