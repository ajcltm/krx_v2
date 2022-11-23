from pathlib import Path
from krx_v2.webScrap import request, workingList # from 다른 폴더(모듈) import 다른 파일

from pathlib import Path
from webScrap_v2 import apps


class Scraper:

    def execute(self):
        wl = workingList.WorkingList()
        rq = request.Request_price()
        dir_ = Path.home().joinpath('Desktop', 'krx')
        s = apps.FSScraper(IWorkingList=wl, IRequester=rq, save_path=dir_)
        s.execute()
