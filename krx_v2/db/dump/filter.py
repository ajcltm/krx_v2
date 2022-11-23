from typing import Optional
from pydantic import BaseModel, validator

class stockPrice(BaseModel):
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

    @validator('*', pre=True)
    def integer(cls, v):
        v = v.replace(',', '')
        return v


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
                    container += [stockPrice(**i) for i in price_list]
        return container
