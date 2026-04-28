import requests
import sqlite3
import json
import os
import time
from datetime import datetime

def scrape_nemo():
    # 1) 공통 설정 (업데이트된 정보 반영)
    base_url = "https://www.nemoapp.kr/api/store/search-list"
    params = {
        "Subway": "222",
        "Radius": "1000",
        "CompletedOnly": "false",
        "NELat": "37.513418496475516",
        "NELng": "127.03560698494442",
        "SWLat": "37.48333024902553",
        "SWLng": "127.00058793535545",
        "Zoom": "15",
        "SortBy": "29"
    }
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    # 2) 데이터 저장 경로 설정
    db_path = os.path.join("data", "nemo_stores.db")
    os.makedirs("data", exist_ok=True)

    # 3) SQLite DB 초기 설정
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"[{datetime.now()}] 신규 조건 데이터 수집 시작...")

    page_index = 0
    total_count = 0
    table_created = False
    columns = []

    try:
        while True:
            params["PageIndex"] = page_index
            print(f"[{datetime.now()}] Page {page_index} 수집 중...", end=" ")
            
            response = requests.get(base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            items = data.get("items", [])
            
            if not items:
                print("\n더 이상 수집할 데이터가 없습니다.")
                break

            print(f"({len(items)}개 발견)")

            # 테이블이 아직 생성되지 않았다면 첫 페이지 데이터를 기준으로 생성 (또는 기존 테이블 초기화)
            if not table_created:
                columns = list(items[0].keys())
                cursor.execute("DROP TABLE IF EXISTS stores")
                col_def = ", ".join([f'"{col}" TEXT' for col in columns])
                cursor.execute(f"CREATE TABLE stores ({col_def})")
                table_created = True

            # 데이터 삽입
            placeholders = ", ".join(["?" for _ in columns])
            insert_query = f"INSERT INTO stores ({', '.join([f'\"{c}\"' for c in columns])}) VALUES ({placeholders})"

            for item in items:
                values = []
                for col in columns:
                    val = item.get(col)
                    if isinstance(val, (list, dict)):
                        values.append(json.dumps(val, ensure_ascii=False))
                    else:
                        values.append(str(val) if val is not None else None)
                cursor.execute(insert_query, values)

            total_count += len(items)
            page_index += 1
            
            # 서버 부하 방지를 위한 짧은 휴식
            time.sleep(0.5)

        conn.commit()
        print(f"[{datetime.now()}] 전체 수집 완료! 총 {total_count}개의 데이터를 저장했습니다.")
        print(f"저장 위치: {db_path}")

    except Exception as e:
        print(f"\n에러 발생: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    scrape_nemo()
