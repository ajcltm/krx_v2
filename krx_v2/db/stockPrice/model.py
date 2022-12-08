from typing import List
from pydantic import BaseModel
from datetime import date


class DateUniverse(BaseModel):
    universe: List[date]
    
class stockPrice(BaseModel):
    date: date
    ISU_SRT_CD: str
    ISU_CD: str
    ISU_ABBRV: str
    MKT_NM: str
    SECT_TP_NM: str
    TDD_CLSPRC: int
    FLUC_TP_CD: int
    CMPPREVDD_PRC: int
    FLUC_RT: int
    TDD_OPNPRC: int
    TDD_HGPRC: int
    TDD_LWPRC: int
    ACC_TRDVOL: int
    ACC_TRDVAL: int
    MKTCAP: int
    LIST_SHRS: int
    MKT_ID: str
    
class stockPrices(BaseModel):
    dataset: List[stockPrice]