---
marp: true
theme: gaia
class: invert
paginate: true
backgroundColor: #F7F2E8
color: #1A1A1A
style: |
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background-color: #F7F2E8; /* Aged Paper Background */
    color: #1A1A1A;
    padding: 50px;
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAAElBMVEUAAAD8/Pz09PT4+Pj29vb////87PqcAAAABnRSTlMAAAAAAN1Ky98AAAAuSURBVDjLY2DDAEZGMAByGDAwMDBghANGRkY4YGRkhANGREZAjpGRkREOGBkZ4QAAt7ID0RkYfQAAAABJRU5ErkJggg=='); /* Subtle Grain Texture */
  }
  h1 {
    font-family: 'Arial Black', sans-serif;
    font-size: 44pt;
    text-transform: uppercase;
    color: #E8344A; /* Riso Red */
    letter-spacing: 4pt;
    position: relative;
    display: inline-block;
  }
  h1::after {
    content: attr(data-content);
    position: absolute;
    left: 3px;
    top: 3px;
    color: rgba(232, 52, 74, 0.25); /* Ghost Title Effect */
    z-index: -1;
  }
  h2 {
    font-family: 'Arial Black', sans-serif;
    color: #0D5C9E; /* Riso Blue */
    margin-bottom: 20px;
  }
  blockquote {
    background: transparent;
    border-left: 10px solid #F5D020; /* Riso Yellow */
    padding: 20px;
    font-style: italic;
    color: #444;
  }
  img {
    border: none;
    mix-blend-mode: multiply; /* Authentic Riso Overlap */
    opacity: 0.9;
    filter: sepia(0.2) contrast(1.1);
  }
  ul li {
    font-family: 'Courier New', monospace;
    font-weight: bold;
    color: #333;
    margin-bottom: 12px;
  }
  .circle-container {
    position: absolute;
    bottom: 50px;
    right: 50px;
    width: 200px;
    height: 200px;
  }
  .riso-circle {
    position: absolute;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    mix-blend-mode: multiply;
  }
  .red { background-color: #E8344A; left: 0; top: 0; }
  .blue { background-color: #0D5C9E; left: 50px; top: 0; }
  .yellow { background-color: #F5D020; left: 25px; top: 40px; }
---

<!-- 
STYLE: Risograph Print
BG: #F7F2E8 (Aged Paper)
Colors: Riso Red (#E8344A), Riso Blue (#0D5C9E), Riso Yellow (#F5D020)
Effect: Multiply Blend, Ghost Text, Grain Texture
-->

# <span data-content="NEMO EDA ANALYSIS">NEMO EDA ANALYSIS</span>

**GANGNAM COMMERCIAL REAL ESTATE**

작성일: 2026-04-28
분석가: Antigravity

<div class="circle-container">
  <div class="riso-circle red"></div>
  <div class="riso-circle blue"></div>
  <div class="riso-circle yellow"></div>
</div>

<!--
(발표 시작) 이번에는 리소그래프 프린트 스타일로 리포트를 재구성했습니다. 아날로그 인쇄 특유의 따뜻한 질감과 CMYK 색상의 자연스러운 겹침을 통해, 차가운 데이터를 인간적인 온기가 느껴지는 통찰로 변환했습니다.
-->

---

## 0. DATA OVERVIEW

- **TOTAL**: 673 ITEMS
- **VARS**: 40 COLUMNS
- **TARGET**: GANGNAM AREA
- **STATUS**: 100% CLEANED

> "WE DECODE THE ANALOG SOUL OF DIGITAL DATA."

<!--
(데이터 개요) 리소그래프 특유의 '오프셋' 효과처럼, 우리는 데이터의 행간에 숨겨진 의미를 읽어냅니다.
-->

---

## 1. MARKET POLARIZATION

- **DEPOSIT**: AVG 69M (STD 99M)
- **RENT**: AVG 5.3M (MAX 90M)
- **PREMIUM**: MEDIAN 0 / MAX 900M

<!--
(수치 진단) 강남 시장의 양극화는 마치 리소그래프의 강렬한 잉크 대비와 같습니다. 상위 25%의 색채가 전체 인상을 결정합니다.
-->

---

## 2. SUPPLY STRUCTURE

- **F&B / SERVICE**: > 60%
- **TYPE**: 99% RENTAL
- **FLOOR**: 1F DOMINANT

<!--
(공급 구조) 음식점과 서비스업이 잉크처럼 진하게 도포된 시장입니다. 1층이라는 프레임이 여전히 강력합니다.
-->

---

## MONTHLY RENT DIST

![bg right:60% contain](./images/monthly_rent_dist.png)

- **ZONE**: 3M ~ 5M KRW
- **INSIGHT**: STANDARD COST
- **ACTION**: VERIFY HIGH-END

<!--
(시각화 1) 월세 분포. 가장 진하게 인쇄된 300~500만원 구간이 강남의 표준입니다.
-->

---

## DEPOSIT VS RENT

![bg right:60% contain](./images/deposit_rent_scatter.png)

- **CORR**: **0.95**
- **INSIGHT**: LOGICAL SYSTEM
- **ACTION**: FIND OUTLIERS

<!--
(시각화 2) 보증금과 월세의 상관관계. 인쇄 핀이 정확히 맞물리듯 논리적인 체계를 보입니다.
-->

---

## BUSINESS SECTORS

![bg right:60% contain](./images/business_large_count.png)

- **MAIN**: F&B, SERVICE
- **INSIGHT**: CONSUMPTION HUB
- **ACTION**: UNIQUE CONCEPT

<!--
(시각화 3) 업종별 현황. 겹쳐진 색상들 사이에서 나만의 고유한 컬러를 찾는 것이 중요합니다.
-->

---

## FLOOR RENT AVG

![bg right:60% contain](./images/floor_rent_avg.png)

- **TOP**: 11F, 12F, 1F
- **REASON**: SKY LOUNGE VALUE
- **ACTION**: OPTIMIZE FLOOR

<!--
(시각화 4) 층별 평균 월세. 예상치 못한 지점에서 발견되는 진한 색상(가치)에 주목하십시오.
-->

---

## SIZE VS RENT

![bg right:60% contain](./images/size_rent_scatter.png)

- **CORR**: **0.62**
- **INSIGHT**: LOCATION > SIZE
- **ACTION**: FIND SWEET SPOT

<!--
(시각화 5) 면적 대비 임대료. 입지의 프리미엄이 면적이라는 종이의 크기보다 중요합니다.
-->

---

## PRICE TYPE RATIO

![bg right:60% contain](./images/price_type_pie.png)

- **RENTAL**: 99.6%
- **INSIGHT**: CASH FLOW FOCUS
- **ACTION**: ASSET STABILITY

<!--
(시각화 6) 가격 유형. 거의 단일 색상(임대)으로 칠해진 시장의 단면입니다.
-->

---

## VIEW COUNT BY STATE

![bg right:60% contain](./images/state_view_avg.png)

- **INSIGHT**: FAST RESPONSE
- **ACTION**: REAL-TIME MONITOR

<!--
(시각화 7) 상태별 조회수. 실시간으로 인쇄되는 뉴스처럼 시장의 반응은 매우 즉각적입니다.
-->

---

## SIZE DISTRIBUTION

![bg right:60% contain](./images/size_dist.png)

- **MAIN**: < 100SQM
- **INSIGHT**: SMALL BI-EFFICIENCY
- **ACTION**: SPLIT STRATEGY

<!--
(시각화 8) 면적 분포. 중소형 상가라는 작은 판형이 시장의 대세임을 보여줍니다.
-->

---

## FAVORITE COUNT

![bg right:60% contain](./images/favorite_count_line.png)

- **INSIGHT**: STAR ITEMS
- **ACTION**: IMMEDIATE ACTION

<!--
(시각화 9) 관심등록수. 희소성 있는 '리미티드 에디션' 매물에 관심이 집중됩니다.
-->

---

## MFEE VS RENT

![bg right:60% contain](./images/mfee_rent_scatter.png)

- **CORR**: **0.48**
- **INSIGHT**: OCCUPANCY COST
- **ACTION**: TOTAL BUDGETING

<!--
(시각화 10) 관리비 vs 월세. 두 가지 색상이 겹쳐져 만드는 최종 비용(컬러)을 확인하십시오.
-->

---

## KEYWORD ANALYSIS

![bg right:60% contain](./images/title_tfidf.png)

- **TOP**: #GANGNAM #NO_PREMIUM
- **INSIGHT**: COST SAVING
- **ACTION**: SEO STRATEGY

<!--
(시각화 11) 키워드 분석. '무권리'라는 강력한 스탬프가 시장을 주도하고 있습니다.
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
(전략 제언) 아날로그의 가치를 디지털 성과로 연결하는 하이브리드 전략을 제언합니다.
-->

---

# <span data-content="ANY QUESTIONS?">ANY QUESTIONS?</span>

**DECODING GANGNAM FUTURE**

[ISSUE REPORT #2](https://github.com/leehyeji020108/wiset-inflearn-nemo/issues/2)

<!--
(마무리) 리소그래프 스타일로 살펴본 강남 상권 분석이었습니다. 따뜻한 통찰이 여러분의 성공적인 비즈니스 인쇄물이 되길 바랍니다.
-->
