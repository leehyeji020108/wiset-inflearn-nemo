---
marp: true
theme: gaia
class: invert
paginate: true
backgroundColor: #F5F500
color: #000000
style: |
  section {
    font-family: 'Arial Black', sans-serif;
    background-color: #F5F500; /* Neo-Brutalism Primary Yellow */
    color: #000000;
    padding: 40px;
    border: 4px solid #000000;
  }
  h1 {
    font-family: 'Arial Black', sans-serif;
    font-size: 50pt;
    text-transform: uppercase;
    color: #000000;
    margin-bottom: 20px;
    border-bottom: 4px solid #000000;
    display: inline-block;
  }
  h2 {
    font-family: 'Arial Black', sans-serif;
    color: #000000;
    border: 3px solid #000000;
    background-color: #FFFFFF;
    padding: 10px 20px;
    display: inline-block;
    box-shadow: 8px 8px 0px #000000;
    margin-bottom: 30px;
  }
  section.lead {
    background-color: #CCFF00; /* Lime Accent */
  }
  section.lead h1 {
    background-color: #000000;
    color: #CCFF00;
    padding: 20px;
    box-shadow: 15px 15px 0px #FF3B30;
  }
  blockquote {
    background: #FFFFFF;
    border: 4px solid #000000;
    box-shadow: 10px 10px 0px #000000;
    padding: 20px;
    font-family: 'Courier New', monospace;
    font-weight: bold;
  }
  img {
    border: 4px solid #000000;
    box-shadow: 12px 12px 0px #000000;
    background-color: #FFFFFF;
  }
  ul li {
    font-family: 'Courier New', monospace;
    font-weight: 900;
    list-style-type: square;
    margin-bottom: 10px;
  }
  footer {
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #000000;
    bottom: 20px;
  }
---

<!-- 
STYLE: Neo-Brutalism
BG: #F5F500 (Yellow) / #CCFF00 (Lime)
Border: 4pt Solid Black
Shadow: Hard Offset Black (No blur)
Fonts: Arial Black (Title), Courier New (Body)
-->

# <!-- fit --> NEMO EDA ANALYSIS

**GANGNAM COMMERCIAL REAL ESTATE**

작성일: 2026-04-28
분석가: Antigravity

<!--
(발표 시작) Neo-Brutalism 스타일로 새롭게 디자인된 리포트를 소개합니다. 강렬한 대비와 파격적인 레이아웃을 통해 강남 시장의 역동성을 시각적으로 극대화했습니다.
-->

---

## 0. DATA OVERVIEW

- **TOTAL**: 673 ITEMS
- **VARS**: 40 COLUMNS
- **TARGET**: GANGNAM AREA
- **STATUS**: 100% CLEANED

> "WE DON'T JUST READ DATA. WE DECODE THE ECOSYSTEM."

<!--
(데이터 개요) 강남의 673개 매물 데이터를 파격적인 네오브루탈리즘 스타일 프레임워크로 분석합니다.
-->

---

## 1. MARKET POLARIZATION

- **DEPOSIT**: AVG 69M (STD 99M)
- **RENT**: AVG 5.3M (MAX 90M)
- **PREMIUM**: MEDIAN 0 / MAX 900M

<!--
(수치 진단) 시장의 극심한 양극화를 두꺼운 테두리와 하드 섀도우로 강조합니다. 평균의 함정을 경고합니다.
-->

---

## 2. SUPPLY STRUCTURE

- **F&B / SERVICE**: > 60%
- **TYPE**: 99% RENTAL
- **FLOOR**: 1F DOMINANT

<!--
(공급 구조) 임대 중심, 1층 중심의 견고한 공급 구조를 직관적인 블록 레이아웃으로 표현했습니다.
-->

---

## MONTHLY RENT DIST

![bg right:60% contain](./images/monthly_rent_dist.png)

- **ZONE**: 3M ~ 5M KRW
- **INSIGHT**: STANDARD COST
- **ACTION**: VERIFY HIGH-END

<!--
(시각화 1) 월세 분포. 300~500만원 사이의 표준 고정비용 구간을 강조합니다.
-->

---

## DEPOSIT VS RENT

![bg right:60% contain](./images/deposit_rent_scatter.png)

- **CORR**: **0.95**
- **INSIGHT**: LOGICAL SYSTEM
- **ACTION**: FIND OUTLIERS

<!--
(시각화 2) 보증금과 월세의 0.95 상관관계. 논리적인 가격 체계를 증명합니다.
-->

---

## BUSINESS SECTORS

![bg right:60% contain](./images/business_large_count.png)

- **MAIN**: F&B, SERVICE
- **INSIGHT**: CONSUMPTION HUB
- **ACTION**: UNIQUE CONCEPT

<!--
(시각화 3) 업종별 현황. 레드오션 속에서 차별화된 컨셉의 필요성을 역설합니다.
-->

---

## FLOOR RENT AVG

![bg right:60% contain](./images/floor_rent_avg.png)

- **TOP**: 11F, 12F, 1F
- **REASON**: SKY LOUNGE VALUE
- **ACTION**: OPTIMIZE FLOOR

<!--
(시각화 4) 층별 평균 월세. 고층부의 반전 가치를 시각적으로 강조합니다.
-->

---

## SIZE VS RENT

![bg right:60% contain](./images/size_rent_scatter.png)

- **CORR**: **0.62**
- **INSIGHT**: LOCATION > SIZE
- **ACTION**: FIND SWEET SPOT

<!--
(시각화 5) 면적 대비 임대료. 규모보다 입지 프리미엄이 우선임을 보여줍니다.
-->

---

## PRICE TYPE RATIO

![bg right:60% contain](./images/price_type_pie.png)

- **RENTAL**: 99.6%
- **INSIGHT**: CASH FLOW FOCUS
- **ACTION**: ASSET STABILITY

<!--
(시각화 6) 가격 유형. 임대 중심 시장의 압도적인 비율을 보여줍니다.
-->

---

## VIEW COUNT BY STATE

![bg right:60% contain](./images/state_view_avg.png)

- **INSIGHT**: FAST RESPONSE
- **ACTION**: REAL-TIME MONITOR

<!--
(시각화 7) 상태별 조회수. 시장의 빠른 반응 속도와 정보 경쟁을 강조합니다.
-->

---

## SIZE DISTRIBUTION

![bg right:60% contain](./images/size_dist.png)

- **MAIN**: < 100SQM
- **INSIGHT**: SMALL BI-EFFICIENCY
- **ACTION**: SPLIT STRATEGY

<!--
(시각화 8) 면적 분포. 소형화, 효율화 트렌드를 데이터로 증명합니다.
-->

---

## FAVORITE COUNT

![bg right:60% contain](./images/favorite_count_line.png)

- **INSIGHT**: STAR ITEMS
- **ACTION**: IMMEDIATE ACTION

<!--
(시각화 9) 관심등록수. 소수 스타 매물에 대한 집중 현상을 경고합니다.
-->

---

## MFEE VS RENT

![bg right:60% contain](./images/mfee_rent_scatter.png)

- **CORR**: **0.48**
- **INSIGHT**: OCCUPANCY COST
- **ACTION**: TOTAL BUDGETING

<!--
(시각화 10) 관리비 vs 월세. 실질 유지 비용 계산의 중요성을 강조합니다.
-->

---

## KEYWORD ANALYSIS

![bg right:60% contain](./images/title_tfidf.png)

- **TOP**: #GANGNAM #NO_PREMIUM
- **INSIGHT**: COST SAVING
- **ACTION**: SEO STRATEGY

<!--
(시각화 11) 키워드 분석. 무권리, 시설 완비 등 비용 절감 키워드의 위력을 보여줍니다.
-->

---

## STRATEGIC ACTION

### 1. MARKET
- EXTREME POLARIZATION
- FASTER ECOSYSTEM CYCLE

### 2. TENANT
- **LIGHT START**: USE NO-PREMIUM
- **DIGITAL LOC**: SNS MARKETING

### 3. LANDLORD
- **FLEXIBILITY**: RENT-FREE
- **EXPERIENCE**: SKY VALUE

<!--
(전략 제언) 네오브루탈리즘의 강렬한 어조로 승리하는 비즈니스 전략을 제언합니다.
-->

---

# <!-- fit --> ANY QUESTIONS?

**DECODING GANGNAM FUTURE**

[ISSUE REPORT #2](https://github.com/leehyeji020108/wiset-inflearn-nemo/issues/2)

<!--
(마무리) 데이터는 거짓말을 하지 않습니다. 네오브루탈리즘 스타일로 재해석한 이번 분석이 여러분의 혁신적인 의사결정에 도움이 되길 바랍니다.
-->
