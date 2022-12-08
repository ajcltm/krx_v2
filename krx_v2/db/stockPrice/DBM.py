from krx_v2.db.stockPrice import dump

class DBM:

    def __init__(self, connect):
        self.con = connect
        self.create = dump.Create(connect = self.con)
        self.dump = dump.Dump(connect = self.con)