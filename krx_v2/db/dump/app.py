from Isql_v2 import dump
from pathlib import Path
from krx_v2.db.dump import dump_data, filter

def main():
    dir_ = Path.home().joinpath('Desktop', 'krx')
    con = dump_data.Connector().get_connect()
    dbm = dump_data.DBM(connect=con)
    dbm.create.execute()
    dump.DumpApp(folder_path=dir_, filtedDataset=filter.Filter(), dumper=dbm.dump).execute()


if __name__ == '__main__':
    main()