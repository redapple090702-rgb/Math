"""
Project: Mathematical Modeling of Circadian Rhythm and Jet Lag Adaptation
Author: Jeonghyun An (Student ID: 20417)
Description: 
    This script simulates human circadian rhythm shifts during jet lag recovery 
    using trigonometric phase shifts and arithmetic sequence difference equations.
"""

import numpy as np
import matplotlib.pyplot as plt

def local_standard_rhythm(t):
    """
    현지(뉴욕) 표준 생체 각성도 함수 f(t)
    오후 4시(16시)에 최댓값 10, 새벽 4시(4시)에 최솟값 0을 가짐.
    """
    return 5 * np.sin(np.pi / 12 * (t - 10)) + 5

def body_rhythm(t, day):
    """
    일차별(day) 내 신체 생체 리듬 함수 g(t)
    귀납적 점화식 (a_1 = 21, a_n+1 = a_n - 1)에 따른 등차수열 위상 변화 모델링.
    목표 위상값인 10 이하로 떨어지지 않도록 하한선(Bound) 처리.
    """
    phase_shift = 22 - day
    phase_shift = max(phase_shift, 10)  # 뉴욕 표준 위상(10)에 도달하면 고정
    return 5 * np.sin(np.pi / 12 * (t - phase_shift)) + 5

def calculate_jpi(y_local, y_body):
    """
    차함수를 이용한 '시차 고통 지수(JPI, Jet Lag Pain Index)' 정량적 연산
    """
    return np.mean(np.abs(y_local - y_body))

def main():
    # 1. 시간 축 설정 (0시부터 24시까지 1,000개의 구간 분할)
    t = np.linspace(0, 24, 1000)
    
    # 2. 시각화 그래프 환경 설정
    plt.figure(figsize=(11, 6.5))
    
    # 현지 표준 리듬 (목표 점선 그래프)
    y_local = local_standard_rhythm(t)
    plt.plot(t, y_local, label='New York Local Standard', color='#0f172a', linestyle='--', linewidth=2.5)
    
    # 3. 시뮬레이션 플롯팅 (주요 관측 일자: Day 1, Day 5, Day 9, Day 12)
    days_to_plot = [1, 5, 9, 12]
    colors = ['#ef4444', '#f97316', '#3b82f6', '#10b981']  # Red, Orange, Blue, Green
    
    print("=" * 50)
    print(" [수리생물학 모델 기반 일차별 시차 고통 지수(JPI) 연산 결과] ")
    print("=" * 50)
    
    for day, color in zip(days_to_plot, colors):
        y_body = body_rhythm(t, day)
        jpi_value = calculate_jpi(y_local, y_body)
        
        # 터미널에 수학적 연산 결과 출력
        print(f"▶ Day {day:02d} | 신체 위상 평행이동 값: {22-day if day<=12 else 10:>2}시 | 평균 시차 고통 지수(JPI): {jpi_value:.4f}")
        
        # 그래프 선 추가
        plt.plot(t, y_body, label=f'Body Rhythm (Day {day})', color=color, linewidth=2)
    
    print("=" * 50)
    
    # 4. 그래프 디자인 및 레이아웃 디테일 설정
    plt.title('Jet Lag Adaptation Simulation via Mathematical Modeling', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Local Time in New York (Hours)', fontsize=12)
    plt.ylabel('Circadian Alertness Level (0 - 10)', fontsize=12)
    
    plt.xlim(0, 24)
    plt.ylim(-0.5, 11)
    plt.xticks(np.arange(0, 25, 2))
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right', frameon=True, shadow=True, facecolor='#f8fafc')
    
    # 5. 고해상도 이미지 저장 및 시각화 출력
    plt.tight_layout()
    plt.savefig('jet_lag_simulation.png', dpi=300)
    print("✔ 시뮬레이션 결과 그래프가 'jet_lag_simulation.png'로 저장되었습니다.")
    plt.show()

if __name__ == '__main__':
    main()
