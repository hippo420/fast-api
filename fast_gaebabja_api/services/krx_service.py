import pandas as pd

def load_allstock_KRX():
    krx_url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
    stk_data = pd.read_html(krx_url, header=0, encoding="euc-kr")[0]
    stk_data = stk_data[['회사명', '종목코드']]
    stk_data = stk_data.rename(columns={'회사명': 'isinCd', '종목코드': 'itmsNm'})
    stk_data['Code'] = stk_data['Code'].apply(lambda x: str(x).zfill(6))
    return stk_data.to_dict(orient='records')
