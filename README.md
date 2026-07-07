# ✈️ Jet Lag Mathematical Modeling & Simulation

대수(Algebra) 교과 과정에서 학습한 **삼각함수의 평행이동·주기 성질**과 **수열의 귀납적 정의(등차수열 점화식)**를 융합하여, 해외 이동 시 발생하는 일주기 생체 리듬(Circadian Rhythm)의 파형 충돌 및 시차 적응 과정을 수리적으로 모델링하고 시뮬레이션한 프로젝트입니다.

## 🧮 Mathematical Background

1. **Local Standard Circadian Function**
   $$f(t) = 5 \sin\left(\frac{\pi}{12}(t - 10)\right) + 5$$
2. **Jet Lagged Body Function (Day $n$)**
   $$g(t) = 5 \sin\left(\frac{\pi}{12}(t - a_n)\right) + 5$$
   - 초기 조건: $a_1 = 21$ (뉴욕 현지 기준 오전 3시 신체 리듬 정점 충돌)
   - 귀납적 점화식: $a_{n+1} = a_n - 1.0$ (공차가 $-1$인 등차수열 모델)
3. **Jet Lag Pain Index (JPI)**
   $$\text{JPI} = |f(t) - g(t)|$$

## 📊 Simulation Result
코드 실행 시 날짜별 신체 파형이 뉴욕 현지 표준 시간축선으로 매일 1시간씩 평행이동하며, 정확히 **12일 차**에 수렴(완벽 적응)하는 동적 진동 그래프(`jet_lag_simulation.png`)가 생성됩니다.
