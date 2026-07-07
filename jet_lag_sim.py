"""
프로젝트: 수리생물학 기반 일차별 시차 적응 동적 시뮬레이션
작성자: 안정현 (학번: 20417)
설명: 코드를 실행하면 DAY 1부터 DAY 12까지 시간이 흐름에 따라 
      신체 위상(시간)과 시차 고통 지수(JPI) 숫자가 실시간으로 변하며 
      그래프가 스르륵 이동하는 애니메이션이 재생됩니다.
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def local_standard_rhythm(t):
    """뉴욕 현지 표준 생체 리듬 함수 f(t)"""
    return 5 * np.sin(np.pi / 12 * (t - 10)) + 5

def body_rhythm(t, phase):
    """일차별 내 신체 리듬 함수 g(t)"""
    return 5 * np.sin(np.pi / 12 * (t - phase)) + 5

def main():
    # 0시부터 24시까지 시간 축 설정
    t = np.linspace(0, 24, 500)
    y_local = local_standard_rhythm(t)
    
    # 대화형 모드 켜기 (실시간 애니메이션 재생을 위해 필수!)
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    
    print("=" * 65)
    print(" [실시간 생체 시계 동기화 및 JPI 수치 연산 대시보드] ")
    print("=" * 65)
    print("  날짜(Day)  |  현재 신체 최고점  |  목표 최고점  |  시차 고통 지수(JPI)")
    print("-" * 65)
    
    # DAY 1부터 DAY 14까지 루프 (12일 차에 완벽 적응 후 14일까지 유지 검증)
    for day in range(1, 15):
        # 등차수열 점화식 적용: 매일 1시간씩 지연 (목표치 10까지만)
        current_phase = 22 - day
        if current_phase < 10:
            current_phase = 10
            
        y_body = body_rhythm(t, current_phase)
        
        # 차함수의 절댓값 평균으로 시차 고통 지수(JPI) 실시간 계산
        jpi = np.mean(np.abs(y_local - y_body))
        
        # 1. 터미널에 실시간으로 변하는 숫자 출력
        print(f"   DAY {day:02d}    |     오전 {current_phase:02d}:00      |   오후 16:00   |       {jpi:.4f}")
        
        # 2. 그래프 창 실시간 업데이트 (지웠다 다시 그리기)
        ax.clear()
        
        # 뉴욕 표준 리듬 (목표선 - 고정)
        ax.plot(t, y_local, label='New York Local (Target)', color='#0f172a', linestyle='--', linewidth=2.5)
        
        # 내 신체 리듬 (매일 변하는 이동선)
        # 적응 완료 전에는 빨간색, 완료 후(DAY 12 이상)에는 초록색으로 변환하여 시각적 효과 극대화
        line_color = '#10b981' if current_phase == 10 else '#ef4444'
        ax.plot(t, y_body, label=f'My Body Rhythm (Day {day})', color=line_color, linewidth=3)
        
        # 현재 신체의 최고점 위치에 실시간 점 찍기
        peak_time = float(current_phase + 6) # 사인 함수 최고점은 평행이동+6시간 지점
        if peak_time >= 24: peak_time -= 24
        ax.scatter(peak_time, 10, color=line_color, s=150, zorder=5, edgecolor='black')
        ax.text(peak_time, 10.3, f"Peak: {int(peak_time)}h", ha='center', fontweight='bold', color=line_color)
        
        # 그래프 텍스트 및 서식 꾸미기
        ax.set_title(f'Circadian Rhythm Shift Simulation - DAY {day}', fontsize=14, fontweight='bold', pad=15)
        ax.set_xlabel('Local Time in New York (Hours)', fontsize=12)
        ax.set_ylabel('Alertness Level (0 - 10)', fontsize=12)
        ax.set_xlim(0, 24)
        ax.set_ylim(-1, 12)
        ax.set_xticks(np.arange(0, 25, 2))
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='upper right', frameon=True, shadow=True)
        
        # 현재 날짜의 JPI 수치를 그래프 내부에 실시간 주석으로 표시
        status_text = "ADAPTATION COMPLETE!" if current_phase == 10 else "ADAPTING..."
        ax.text(1, 0.5, f"Current JPI: {jpi:.4f}\nStatus: {status_text}", 
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='#cbd5e1', boxstyle='round,pad=0.5'),
                fontsize=11, fontweight='bold')
        
        # 화면 갱신 및 대기 시간 조절 (0.6초 간격으로 숫자가 바뀌며 스르륵 움직임)
        plt.draw()
        plt.pause(0.6)
        
    print("=" * 65)
    print("✔ 시뮬레이션이 성공적으로 완료되었습니다! (창을 닫으려면 그래프를 종료하세요)")
    
    # 대화형 모드 끄고 그래프 창 유지
    plt.ioff()
    plt.show()

if __name__ == '__main__':
    main()
