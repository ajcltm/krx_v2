from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime, date

class stockPrice(BaseModel):
    date: date
    ISU_SRT_CD: Optional[str]
    ISU_CD: Optional[str]
    ISU_ABBRV: Optional[str]
    MKT_NM: Optional[str]
    SECT_TP_NM: Optional[str]
    TDD_CLSPRC: Optional[int]
    FLUC_TP_CD: Optional[int]
    CMPPREVDD_PRC: Optional[int]
    FLUC_RT: Optional[float]
    TDD_OPNPRC: Optional[int]
    TDD_HGPRC: Optional[int]
    TDD_LWPRC: Optional[int]
    ACC_TRDVOL: Optional[int]
    ACC_TRDVAL: Optional[int]
    MKTCAP: Optional[int]
    LIST_SHRS: Optional[int]
    MKT_ID: Optional[str]


    @validator('ISU_SRT_CD', 'ISU_CD', 'ISU_ABBRV', 'MKT_NM', 'SECT_TP_NM', 'TDD_CLSPRC', 'FLUC_TP_CD', 'CMPPREVDD_PRC', 'FLUC_RT', 'TDD_OPNPRC', 'TDD_HGPRC', 'TDD_LWPRC', 'ACC_TRDVOL', 'ACC_TRDVAL', 'MKTCAP', 'LIST_SHRS', 'MKT_ID', pre=True, always=True)
    def integer(cls, v): 
        v = v.replace(',', '')
        if v == ' ':
            return None
        elif v =='-':
            return None
        return v

    @validator('date', pre=True, always=True)
    def string_to_date(cls, v):
        d = datetime.strptime(v,'%Y%m%d')
        return d.date()

class Filter:

    def check_bussiness_day(self, dailyData):
        dataList = [i['TDD_CLSPRC'] for i in dailyData['OutBlock_1'][:10]]
        for i in dataList:
            if not i == '-':
                return True
        return False

    def filt(self, rawDataset):
        container = []
        for data in rawDataset:
            for key, value in data.items():
                if self.check_bussiness_day(dailyData=value):
                    price_list = value.get('OutBlock_1')
                    for i in price_list:
                        try:
                            container.append(stockPrice(date=key[1], **i))
                        except:
                            print(key[1], i)
        return container
