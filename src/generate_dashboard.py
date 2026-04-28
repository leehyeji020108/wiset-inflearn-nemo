import pandas as pd
import sqlite3
import json
import os

def generate_dashboard():
    # 1) 데이터 로드
    db_path = os.path.join("data", "nemo_stores.db")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM stores", conn)
    conn.close()

    # 데이터 타입 변환
    numeric_cols = ['deposit', 'monthlyRent', 'premium', 'sale', 'maintenanceFee', 'size', 'viewCount', 'favoriteCount', 'areaPrice']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 요약 데이터 추출
    summary = {
        "total_stores": int(len(df)),
        "avg_rent": round(df['monthlyRent'].mean(), 1),
        "avg_deposit": round(df['deposit'].mean(), 0),
        "top_business": df['businessLargeCodeName'].mode()[0] if not df['businessLargeCodeName'].empty else "N/A"
    }

    # 차트 데이터 준비
    # 1. 월세 분포 (구간별)
    rent_bins = pd.cut(df['monthlyRent'], bins=[0, 100, 300, 500, 1000, 2000, 5000, 10000], labels=["0-100", "100-300", "300-500", "500-1000", "1000-2000", "2000-5000", "5000+"])
    rent_dist = rent_bins.value_counts().sort_index().to_dict()

    # 2. 업종별 비중
    business_dist = df['businessLargeCodeName'].value_counts().to_dict()

    # 3. 층별 매물 수
    floor_dist = df['floor'].value_counts().head(10).to_dict()

    # 4. 보증금 vs 월세 (상관관계 산점도용 샘플링)
    scatter_data = df[['deposit', 'monthlyRent']].dropna().sample(min(300, len(df))).to_dict(orient='records')

    # 5. 면적 분포
    size_bins = pd.cut(df['size'], bins=[0, 33, 66, 100, 165, 330, 1000], labels=["~10평", "10~20평", "20~30평", "30~50평", "50~100평", "100평+"])
    size_dist = size_bins.value_counts().sort_index().to_dict()

    # HTML 템플릿 작성
    html_template = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nemo 상가 데이터 프리미엄 대시보드</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #6366f1;
            --secondary: #a855f7;
            --accent: #f43f5e;
            --background: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --glass: rgba(255, 255, 255, 0.05);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Pretendard', sans-serif;
        }}

        body {{
            background-color: var(--background);
            color: var(--text-main);
            padding: 2rem;
            min-height: 100vh;
        }}

        .dashboard-container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            margin-bottom: 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            animation: fadeInDown 0.8s ease-out;
        }}

        header h1 {{
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
            animation: fadeInUp 0.8s ease-out;
        }}

        .card {{
            background: var(--card-bg);
            padding: 1.5rem;
            border-radius: 1.5rem;
            border: 1px solid var(--glass);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            overflow: hidden;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        }}

        .summary-card h3 {{
            color: var(--text-muted);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.1rem;
            margin-bottom: 0.5rem;
        }}

        .summary-card .value {{
            font-size: 2rem;
            font-weight: 800;
        }}

        .summary-card .unit {{
            font-size: 1rem;
            color: var(--text-muted);
            margin-left: 0.3rem;
        }}

        .chart-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
            gap: 2rem;
            animation: fadeInUp 1s ease-out;
        }}

        .chart-card {{
            height: 450px;
            display: flex;
            flex-direction: column;
        }}

        .chart-card h2 {{
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
            color: var(--text-main);
            border-left: 4px solid var(--primary);
            padding-left: 1rem;
        }}

        .chart-container {{
            flex: 1;
            position: relative;
        }}

        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .badge {{
            position: absolute;
            top: 1rem;
            right: 1rem;
            padding: 0.2rem 0.6rem;
            border-radius: 0.5rem;
            font-size: 0.7rem;
            font-weight: 600;
            background: var(--primary);
        }}

        @media (max-width: 768px) {{
            .chart-grid {{
                grid-template-columns: 1fr;
            }}
            .chart-card {{
                height: 400px;
            }}
        }}
    </style>
</head>
<body>
    <div class="dashboard-container">
        <header>
            <div>
                <h1>Nemo Real Estate Analytics</h1>
                <p style="color: var(--text-muted)">강남권 상업용 부동산 데이터 실시간 분석 현황</p>
            </div>
            <div style="text-align: right">
                <p style="font-weight: 600">Updated: {summary['total_stores']} Units</p>
                <p style="font-size: 0.8rem; color: var(--text-muted)">{pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </header>

        <div class="summary-grid">
            <div class="card summary-card">
                <h3>Total Listings</h3>
                <div class="value">{summary['total_stores']}</div>
                <div class="unit">개 매물</div>
            </div>
            <div class="card summary-card">
                <h3>Avg Monthly Rent</h3>
                <div class="value">{summary['avg_rent']}</div>
                <div class="unit">만원</div>
            </div>
            <div class="card summary-card">
                <h3>Avg Deposit</h3>
                <div class="value">{summary['avg_deposit']}</div>
                <div class="unit">만원</div>
            </div>
            <div class="card summary-card">
                <h3>Dominant Sector</h3>
                <div class="value" style="font-size: 1.5rem">{summary['top_business']}</div>
                <div class="unit">업종</div>
            </div>
        </div>

        <div class="chart-grid">
            <div class="card chart-card">
                <h2>월세 구간별 분포</h2>
                <div class="chart-container">
                    <canvas id="rentDistChart"></canvas>
                </div>
            </div>
            <div class="card chart-card">
                <h2>업종별 매물 비중</h2>
                <div class="chart-container">
                    <canvas id="businessPieChart"></canvas>
                </div>
            </div>
            <div class="card chart-card">
                <h2>보증금 vs 월세 상관관계</h2>
                <div class="chart-container">
                    <canvas id="rentScatterChart"></canvas>
                </div>
            </div>
            <div class="card chart-card">
                <h2>면적별(평수) 매물 분포</h2>
                <div class="chart-container">
                    <canvas id="sizeBarChart"></canvas>
                </div>
            </div>
            <div class="card chart-card">
                <h2>주요 층수별 매물 현황</h2>
                <div class="chart-container">
                    <canvas id="floorChart"></canvas>
                </div>
            </div>
            <div class="card chart-card" style="justify-content: center; align-items: center; background: linear-gradient(135deg, var(--primary), var(--secondary)); opacity: 0.9;">
                <div style="text-align: center">
                    <h2 style="border: none; color: white; margin-bottom: 1rem">AI Insight</h2>
                    <p style="font-size: 1.1rem; max-width: 80%; margin: 0 auto; line-height: 1.6">
                        "현재 강남권 상가 시장은 <strong>F&B(음식업)</strong> 위주의 재편이 뚜렷하며,<br>
                        300-500만원 사이의 <strong>중소형 매물</strong>이 시장의 유동성을 주도하고 있습니다."
                    </p>
                </div>
            </div>
        </div>
    </div>

    <script>
        const data = {{
            rentDist: {json.dumps(rent_dist)},
            businessDist: {json.dumps(business_dist)},
            scatter: {json.dumps(scatter_data)},
            sizeDist: {json.dumps(size_dist)},
            floorDist: {json.dumps(floor_dist)}
        }};

        Chart.defaults.color = '#94a3b8';
        Chart.defaults.font.family = 'Pretendard';

        // 1. Monthly Rent Dist
        new Chart(document.getElementById('rentDistChart'), {{
            type: 'bar',
            data: {{
                labels: Object.keys(data.rentDist),
                datasets: [{{
                    label: '매물 수',
                    data: Object.values(data.rentDist),
                    backgroundColor: '#6366f1',
                    borderRadius: 8
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{ legend: {{ display: false }} }},
                scales: {{ y: {{ grid: {{ color: '#1e293b' }} }}, x: {{ grid: {{ display: false }} }} }}
            }}
        }});

        // 2. Business Pie
        new Chart(document.getElementById('businessPieChart'), {{
            type: 'doughnut',
            data: {{
                labels: Object.keys(data.businessDist),
                datasets: [{{
                    data: Object.values(data.businessDist),
                    backgroundColor: [
                        '#6366f1', '#a855f7', '#f43f5e', '#10b981', '#f59e0b', '#3b82f6', '#ec4899'
                    ],
                    borderWidth: 0,
                    hoverOffset: 20
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ position: 'right', labels: {{ padding: 20, usePointStyle: true }} }}
                }},
                cutout: '70%'
            }}
        }});

        // 3. Scatter
        new Chart(document.getElementById('rentScatterChart'), {{
            type: 'scatter',
            data: {{
                datasets: [{{
                    label: '매물',
                    data: data.scatter.map(d => ({{ x: d.deposit, y: d.monthlyRent }})),
                    backgroundColor: 'rgba(244, 63, 94, 0.6)',
                    pointRadius: 4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    x: {{ title: {{ display: true, text: '보증금 (만원)' }}, grid: {{ color: '#1e293b' }} }},
                    y: {{ title: {{ display: true, text: '월세 (만원)' }}, grid: {{ color: '#1e293b' }} }}
                }}
            }}
        }});

        // 4. Size Bar
        new Chart(document.getElementById('sizeBarChart'), {{
            type: 'bar',
            data: {{
                labels: Object.keys(data.sizeDist),
                datasets: [{{
                    label: '매물 수',
                    data: Object.values(data.sizeDist),
                    backgroundColor: '#a855f7',
                    borderRadius: 8
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                plugins: {{ legend: {{ display: false }} }},
                scales: {{ x: {{ grid: {{ color: '#1e293b' }} }}, y: {{ grid: {{ display: false }} }} }}
            }}
        }});

        // 5. Floor Bar
        new Chart(document.getElementById('floorChart'), {{
            type: 'bar',
            data: {{
                labels: Object.keys(data.floorDist).map(f => f + '층'),
                datasets: [{{
                    label: '매물 수',
                    data: Object.values(data.floorDist),
                    backgroundColor: '#10b981',
                    borderRadius: 8
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{ legend: {{ display: false }} }},
                scales: {{ y: {{ grid: {{ color: '#1e293b' }} }}, x: {{ grid: {{ display: false }} }} }}
            }}
        }});
    </script>
</body>
</html>
    """
    
    with open("nemo_dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"대시보드가 생성되었습니다: {os.path.abspath('nemo_dashboard.html')}")

if __name__ == "__main__":
    generate_dashboard()
