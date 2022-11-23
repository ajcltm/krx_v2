- General
~~~
Request URL: http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd
Request Method: POST
Status Code: 200 OK
Remote Address: 23.43.165.169:80
Referrer Policy: strict-origin-when-cross-origin
~~~

- Request Headers
~~~
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
Connection: keep-alive
Content-Length: 111
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: __utmz=139639017.1652282025.4.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=139639017.1852499237.1632745018.1666713177.1668953735.9; __utmc=139639017; __utmb=139639017.1.10.1668953735; __smVisitorID=Vt473Y6vPMv; JSESSIONID=187Taz3fnAJyOs2gBCvrspEy3i54Cph2f4b27Lo379xVUtGpbL5YWIelBxyUaYu1.bWRjX2RvbWFpbi9tZGNvd2FwMS1tZGNhcHAwMQ==
Host: data.krx.co.kr
Origin: http://data.krx.co.kr
Referer: http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010101
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
X-Requested-With: XMLHttpRequest
~~~

- Form Data
~~~
bld: dbms/MDC/STAT/standard/MDCSTAT01501
locale: ko_KR
mktId: ALL
trdDd: 19950614
share: 1
money: 1
csvxls_isNo: false
~~~

~~~json
{
  "OutBlock_1": [
    {
      "ISU_SRT_CD": "009840",
      "ISU_CD": "KR7009840000",
      "ISU_ABBRV": "갑을",
      "MKT_NM": "KOSPI",
      "SECT_TP_NM": "",
      "TDD_CLSPRC": "11,400",
      "FLUC_TP_CD": "2",
      "CMPPREVDD_PRC": "-200",
      "FLUC_RT": "-1.72",
      "TDD_OPNPRC": "11,700",
      "TDD_HGPRC": "11,800",
      "TDD_LWPRC": "11,400",
      "ACC_TRDVOL": "7,230",
      "ACC_TRDVAL": "83,553,000",
      "MKTCAP": "47,310,000,000",
      "LIST_SHRS": "4,150,000",
      "MKT_ID": "STK"
    },
    {
      "ISU_SRT_CD": "011290",
      "ISU_CD": "KR7011290004",
      "ISU_ABBRV": "갑을방적",
      "MKT_NM": "KOSPI",
      "SECT_TP_NM": "",
      "TDD_CLSPRC": "12,600",
      "FLUC_TP_CD": "1",
      "CMPPREVDD_PRC": "100",
      "FLUC_RT": "0.80",
      "TDD_OPNPRC": "12,700",
      "TDD_HGPRC": "12,800",
      "TDD_LWPRC": "12,500",
      "ACC_TRDVOL": "25,330",
      "ACC_TRDVAL": "321,797,000",
      "MKTCAP": "38,472,588,000",
      "LIST_SHRS": "3,053,380",
      "MKT_ID": "STK"
    },
    {
      "ISU_SRT_CD": "000900",
      "ISU_CD": "KR7000900001",
      "ISU_ABBRV": "강원산업",
      "MKT_NM": "KOSPI",
      "SECT_TP_NM": "",
      "TDD_CLSPRC": "14,700",
      "FLUC_TP_CD": "1",
      "CMPPREVDD_PRC": "200",
      "FLUC_RT": "1.38",
      "TDD_OPNPRC": "14,800",
      "TDD_HGPRC": "14,800",
      "TDD_LWPRC": "14,400",
      "ACC_TRDVOL": "39,290",
      "ACC_TRDVAL": "573,781,000",
      "MKTCAP": "129,653,676,600",
      "LIST_SHRS": "8,819,978",
      "MKT_ID": "STK"
    },
    ...(생략)
    ],
  "CURRENT_DATETIME": "2022.11.20 PM 11:36:01"
~~~