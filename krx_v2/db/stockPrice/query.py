from krx_v2.db.stockPrice import model

class Query:

    def __init__(self, connect):
        self.con = connect
        self.cur = self.con.cursor()

    def query_dateUniverse(self):
        sql_ = 'SELECT distinct(date) FROM krx.stockPrice'
        self.cur.execute(sql_)
        return model.DateUniverse(universe=[data[0] for data in self.cur.fetchall()])
    
    def query_byTicker(self, ticker):
        sql_ = f"select * from krx.stockPrice where ISU_SRT_CD = '{ticker}'"
        self.cur.execute(sql_)
        keys = list(model.stockPrice.__fields__.keys())
        container = []
        for data in self.cur.fetchall():
            container.append({keys[idx]: value for idx, value in enumerate(data)})
            print(container)
            break
        return model.stockPrices(dataset=container)


if __name__ == '__main__':
    from krx_v2.db.stockPrice import connect 

    con = connect.Connector().get_connect(type='mysql')
    dataset = Query(connect=con).query_dateUniverse()
    print(dataset.universe[-5:])

    dataset = Query(connect=con).query_byTicker('000270').dataset
    print(dataset[-1].json(indent=2))

