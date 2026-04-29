---
marp: true
theme: gaia
class: invert
paginate: true
backgroundColor: #F7F2E8
color: #1A1A1A
style: |
  @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
  section {
    font-family: 'Pretendard', 'Helvetica Neue', Arial, sans-serif;
    background-color: #F7F2E8; /* 오래된 종이 배경 */
    color: #1A1A1A;
    padding: 50px;
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAAElBMVEUAAAD8/Pz09PT4+Pj29vb////87PqcAAAABnRSTlMAAAAAAN1Ky98AAAAuSURBVDjLY2DDAEZGMAByGDAwMDBghANGRkY4YGRkhANGREZAjpGRkREOGBkZ4QAAt7ID0RkYfQAAAABJRU5ErkJggg=='); /* 미세한 노이즈 텍스처 */
  }
  h1 {
    font-family: 'Pretendard', 'Arial Black', sans-serif;
    font-size: 44pt;
    font-weight: 900;
    text-transform: uppercase;
    color: #E8344A; /* 리소 레드 */
    letter-spacing: 2pt;
    position: relative;
    display: inline-block;
  }
  h1::after {
    content: attr(data-content);
    position: absolute;
    left: 2px;
    top: 2px;
    color: rgba(232, 52, 74, 0.25); /* 고스트 타이틀 효과 */
    z-index: -1;
  }
  h2 {
    font-family: 'Pretendard', 'Arial Black', sans-serif;
    font-weight: 800;
    color: #0D5C9E; /* 리소 블루 */
    margin-bottom: 20px;
    border-bottom: 2px solid #F5D020;
    display: inline-block;
  }
  blockquote {
    background: transparent;
    border-left: 10px solid #F5D020; /* 리소 옐로우 */
    padding: 20px;
    font-style: italic;
    color: #444;
    font-family: 'Pretendard', sans-serif;
  }
  img {
    border: none;
    mix-blend-mode: multiply; /* 아날로그 겹침 효과 */
    opacity: 0.9;
    filter: sepia(0.2) contrast(1.1);
  }
  ul li {
    font-family: 'Pretendard', sans-serif;
    font-weight: 600;
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
STYLE: Risograph Print (Korean Version)
BG: #F7F2E8 (Aged Paper)
Colors: Riso Red (#E8344A), Riso Blue (#0D5C9E), Riso Yellow (#F5D020)
Effect: Multiply Blend, Ghost Text, Grain Texture
-->

# <span data-content="NEMO EDA 분석 리포트">NEMO EDA 분석 리포트</span>

**강남권 상업용 부동산 시장 심층 분석**

작성일: 2026-04-28
분석가: Antigravity

<div class="circle-container">
  <div class="riso-circle red"></div>
  <div class="riso-circle blue"></div>
  <div class="riso-circle yellow"></div>
</div>

<!--
(발표 시작) 여러분 안녕하십니까. 오늘 저는 대한민국 상업용 부동산의 심장부인 '강남권 상가 시장'을 데이터로 분석한 결과를 발표하겠습니다. 이번 슬라이드는 리소그래프 프린트 스타일로 제작되어, 차가운 수치 속에 숨겨진 시장의 온기와 흐름을 아날로그적인 감성으로 재해석했습니다.
-->

---

## 0. 데이터 개요 및 정제

- **전체 규모**: 673개 매물 정보
- **변수 구성**: 40개 컬럼 (수치형, 범주형 등)
- **분석 대상**: 강남권 상가 임대/매매 데이터
- **정제 상태**: 중복 데이터 0건, 정제 완료

> "단순한 숫자를 넘어 상권의 생태계를 읽어냅니다."

<!--
(데이터 개요) 673개의 엄선된 데이터를 바탕으로 분석을 진행했습니다. 중복을 철저히 제거하여 강남 시장의 실제 모습을 가장 투명하게 반영하고자 노력했습니다.
-->

---

## 1. 수치 진단: 시장의 양극화

- **보증금**: 평균 6,900만 원 (표준편차 9,900만 원)
- **월세**: 평균 534만 원 (최고 9,000만 원)
- **권리금**: 중위수 0원 / 최고 9억 원

<!--
(수치 진단) 강남 시장은 극심한 양극화를 보입니다. 보증금과 월세 모두 '롱테일' 분포를 보이며, 상위 25%의 프리미엄 매물이 시장 지수를 주도하고 있습니다. 특히 권리금 중위수가 0원인 점은 최근의 상권 변화를 잘 보여줍니다.
-->

---

## 2. 공급 구조: 음식점과 1층 중심

- **업종 구성**: 음식점/서비스업/휴게음식점이 60% 이상
- **거래 유형**: 99.6%가 '임대' 매물
- **층수 전략**: 1층이 압도적 비중 (노출도 중시)

<!--
(공급 구조) 강남 상권은 먹고 즐기는 체험형 소비 중심으로 재편되었습니다. 대다수가 임대 매물인 점은 실운영자 중심의 활발한 시장임을 의미하며, 여전히 1층의 가시성이 최고의 가치로 평가받고 있습니다.
-->

---

## 시각화 1: 월세 분포 현황

![bg right:60% contain](./images/monthly_rent_dist.png)

- **집중 구간**: 300~500만 원대 밀집
- **인사이트**: 강남 진입의 표준 비용
- **제언**: 고가 매물은 철저한 매출 분석 필수

<!--
(시각화 1) 월세 분포입니다. 300~500만 원 구간에 가장 많은 매물이 몰려 있습니다. 이것이 강남 상권의 '표준 입장료'이며, 이 구간을 벗어난 고가 매물은 신중한 접근이 필요합니다.
-->

---

## 시각화 2: 보증금과 월세의 상관관계

![bg right:60% contain](./images/deposit_rent_scatter.png)

- **상관계수**: **0.95** (매우 강한 상관관계)
- **인사이트**: 논리적인 임대료 산정 체계
- **제언**: 추세선 이탈 매물은 특수 사정 확인 필요

<!--
(시각화 2) 보증금과 월세는 0.95라는 거의 완벽한 선형 관계를 보입니다. 시장이 매우 합리적으로 가격을 책정하고 있다는 증거이며, 이 관계에서 벗어난 매물은 특별한 기회이거나 혹은 위험 요소가 있을 수 있습니다.
-->

---

## 시각화 3: 업종별 공급 분포

![bg right:60% contain](./images/business_large_count.png)

- **주요 업종**: 일반음식점, 서비스업 압도적
- **인사이트**: '복합 소비 상권'의 특징
- **제언**: 레드오션 속 차별화된 컨셉 필수

<!--
(시각화 3) 강남은 전형적인 소비 상권입니다. 음식점 비중이 매우 높아 경쟁이 치열하므로, 단순한 창업보다는 독창적인 브랜딩이 생존의 열쇠가 됩니다.
-->

---

## 시각화 4: 층별 평균 월세 분석

![bg right:60% contain](./images/floor_rent_avg.png)

- **반전 결과**: 11-12층 고층부 월세가 최상위
- **이유**: 스카이라운지 및 대형 오피스 가치
- **제언**: 목적형 방문 업종은 고층부 효율 극대화

<!--
(시각화 4) 흥미롭게도 1층만큼이나 고층부의 임대료가 높게 나타납니다. 이는 뷰(View)가 중요한 프리미엄 매장이나 대형 법인 수요가 고층부에 몰려 있기 때문입니다.
-->

---

## 시각화 5: 면적과 월세의 상관관계

![bg right:60% contain](./images/size_rent_scatter.png)

- **상관계수**: **0.62** (상대적으로 낮음)
- **인사이트**: 면적보다 **'입지 프리미엄'**이 우선
- **제언**: 업종별 최적 효율 면적 도출 필요

<!--
(시각화 5) 면적이 넓다고 무조건 월세가 비례해서 오르지는 않습니다. 강남에서는 공간의 크기보다 '어디에 위치하느냐'라는 입지 가치가 임대료 결정의 핵심입니다.
-->

---

## 시각화 6: 가격 유형 비율

![bg right:60% contain](./images/price_type_pie.png)

- **현황**: 임대 99.6% vs 매매 0.4%
- **인사이트**: 자산주들의 장기 임대 수익 선호
- **제언**: 매매 기회 희소, 자산 가치 안정 신호

<!--
(시각화 6) 매매 물건이 극히 드뭅니다. 소유주들이 강남 자산의 가치를 확신하고 매각보다는 안정적인 임대 수익을 선택하고 있다는 뜻입니다.
-->

---

## 시각화 7: 상태별 평균 조회수

![bg right:60% contain](./images/state_view_avg.png)

- **인사이트**: 신규/변경 매물에 대한 빠른 시장 반응
- **제언**: 실시간 모니터링 및 빠른 의사결정 필수

<!--
(시각화 7) 시장 참여자들은 매우 민감합니다. 좋은 조건으로 변경되거나 새로 나온 매물은 즉시 높은 조회수를 기록하며 정보 전쟁이 일어납니다.
-->

---

## 시각화 8: 면적 분포 현황

![bg right:60% contain](./images/size_dist.png)

- **대세**: 100㎡(약 30평) 미만 중소형 상가
- **인사이트**: 소규모 프랜차이즈/1인 창업 최적화
- **제언**: 임대인은 분할 임대 전략이 수익성 유리

<!--
(시각화 8) 강남 상권은 30평 미만의 중소형 매장이 주도하고 있습니다. 이는 트렌드 변화에 유연하게 대처하려는 임차인들의 수요를 반영한 것입니다.
-->

---

## 시각화 9: 관심등록수 추이 분석

![bg right:60% contain](./images/favorite_count_line.png)

- **인사이트**: 소수 '스타 매물'에 대한 관심 집중
- **제언**: 관심도 급증 매물 발견 시 즉각 분석 필요

<!--
(시각화 9) 대다수의 매물은 낮은 관심을 받지만, 몇몇 스타 매물에 모든 이목이 쏠립니다. 이런 매물을 포착하는 데이터 안목이 선점의 핵심입니다.
-->

---

## 시각화 10: 관리비와 월세의 관계

![bg right:60% contain](./images/mfee_rent_scatter.png)

- **상관계수**: **0.48**
- **인사이트**: 프라임 빌딩의 높은 유지비용
- **제언**: 실질 유지비(월세+관리비) 기반 예산 수립

<!--
(시각화 10) 월세만 보시면 안 됩니다. 강남의 프라임 급 빌딩은 관리비 비중이 상당합니다. 반드시 합산된 '실질 유지비'를 계산하여 재무 계획을 세워야 합니다.
-->

---

## 시각화 11: 주요 키워드 분석 (TF-IDF)

![bg right:60% contain](./images/title_tfidf.png)

- **핵심 키워드**: #역세권 #강남역 #무권리 #인테리어완비
- **인사이트**: 비용 절감 및 접근성 강조
- **제언**: 마케팅 시 고가치 키워드 전략적 활용

<!--
(시각화 11) 제목에서 가장 많이 발견되는 키워드는 '무권리'와 '인테리어 완비'입니다. 초기 투자비를 줄이려는 임차인들의 간절한 욕구가 데이터에 그대로 나타나 있습니다.
-->

---

## 5. 전략적 제언: 승리하는 비즈니스

### 1. 거시 시장 진단
- 시장 투명성은 높으나 입지 계급화 고착화
- 무권리 매물 증가는 상권 생태 주기 단축을 의미

### 2. 임차인 생존 전략
- **경량 창업**: 인테리어 완비 매물로 초기 투자비 최소화
- **디지털 입지**: 물리적 위치만큼 SNS 마케팅 역량이 중요

### 3. 임대인 자산 관리
- **유연한 대응**: 공실 장기화 시 렌트프리 등 선제적 제안
- **공간 경험**: 고층부의 특화 설계로 자산 수익률 제고

<!--
(전략 제언) 요약하자면, 강남은 '초양극화' 시장입니다. 리스크를 줄이는 경량 창업과 공간의 가치를 높이는 임대 전략이 필수적입니다.
-->

---

# <span data-content="경청해주셔서 감사합니다">경청해주셔서 감사합니다</span>

**데이터로 그리는 강남 상권의 미래**

[이슈 리포트 확인하기](https://github.com/leehyeji020108/wiset-inflearn-nemo/issues/2)

<!--
(마무리) 지금까지 데이터로 읽어본 강남 상권이었습니다. 이 차가운 수치들 사이에서 여러분의 따뜻한 성공 기회를 발견하시길 바랍니다. 질문 있으시면 부탁드립니다. 감사합니다.
-->
