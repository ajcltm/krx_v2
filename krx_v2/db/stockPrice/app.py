from Isql_v2 import dump as dump_
from pathlib import Path
from krx_v2.db.stockPrice import filter, DBM, connect, query
import os

def get_startFileName(dir_):
    con = connect.Connector().get_connect(type='mysql')
    lastDBdate = query.Query(connect=con).query_dateUniverse().universe[-1].strftime(format='%Y%m%d')
    lst = os.listdir(dir_)
    idx = lst.index(f'trdDd_{lastDBdate}.pickle')
    return lst[idx+1] 

def update_db():

    dir_ = Path.home().joinpath('Desktop', 'krx')
    con = connect.Connector().get_connect(type='mysql')
    dbm = DBM.DBM(connect=con)
    dbm.create.execute()
    startFileName=get_startFileName(dir_)
    dump_.DumpApp(folder_path=dir_, filtedDataset=filter.Filter(), dumper=dbm.dump).execute(startFileName=startFileName, chunkNum=100)


if __name__ == '__main__':
    update_db()