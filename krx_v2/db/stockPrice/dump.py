from Isql_v2 import sql
from pathlib import Path
import sqlite3
from pydantic import BaseModel 
from datetime import datetime
import pymysql


class stockPrice(BaseModel):
    date: datetime
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



class Create:

    def __init__(self, connect):
        self.con = connect

    def execute(self):
        sql_ = sql.CreateSql(model=stockPrice).get_create(
            date= 'date',
            ISU_SRT_CD= 'varchar(20)',
            ISU_CD= 'varchar(20)',
            ISU_ABBRV= 'varchar(20)',
            MKT_NM= 'varchar(20)',
            SECT_TP_NM= 'varchar(20)',
            TDD_CLSPRC= 'integer',
            FLUC_TP_CD= 'integer',
            CMPPREVDD_PRC= 'integer',
            FLUC_RT= 'integer',
            TDD_OPNPRC= 'integer',
            TDD_HGPRC= 'integer',
            TDD_LWPRC= 'integer',
            ACC_TRDVOL= 'integer',
            ACC_TRDVAL= 'bigint',
            MKTCAP= 'bigint',
            LIST_SHRS= 'bigint',
            MKT_ID= 'varchar(20)'
        )
        c = self.con.cursor()
        c.execute(sql_)
        self.con.commit()
    

class Dump:

    def __init__(self, connect):
        self.con = connect

    def execute(self, dataset):
        sql_ = sql.InsertSql(model=stockPrice).get_dump(dataset=dataset)
        c = self.con.cursor()
        c.execute(sql_)
        self.con.commit()