# DB에 저장된 수집 데이터를 가져와서 Excel로 저장
#  - List, Dict type → Pandas의 DataFrame(표)으로 생성 가능 → Excel, csv 저장

import pandas as pd
from datetime import datetime
from db.moive_dao import get_reviews

review = get_reviews()
print(reviews)
# DB에서 가져온 데이터 확인
for items in reviews:
    print(item)

# dict Type의 데이터를 Table 생성
print("="*100)
df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d")
df_save.to_excel(f"./review_save_{now}.xlsx", index=False)