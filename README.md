# AI/Deep Learning Study Repository

이 레포지토리는 백엔드 개발자로서 AI 및 딥러닝 지식을 습득하고 궁극적으로 **입찰 도메인 패턴 분석** 프로젝트를 성공적으로 수행하기 위한 모든 학습 과정과 코드를 기록합니다.

* **최종 목표:** TabNet과 같은 고급 모델을 활용하여 비즈니스 문제(경쟁사 입찰 전략 예측)를 해결하는 **실무 역량** 확보.
* **주요 학습 기술:** Python, PyTorch, NumPy/Pandas, CNN/RNN/Attention Mechanism, MLOps 기본.

---

## 🗺️ 학습 로드맵 및 진도 현황 (Learning Roadmap & Progress)

| 단계 | 학습 자료 / 프로젝트 | 상태 | 주요 내용 |
| :--- | :--- | :--- | :--- |
| **Stage 1 (기초)** | **[DL_From_Scratch]** | ⏳ 진행 중 | 신경망의 동작 원리 이해 (NumPy 기반 구현) |
| **Stage 2 (프레임워크)**| **[PyTorch_Core_Deep_Dive] (인프런 강의)** | 💡 예정 | PyTorch 실무 핵심 이론 심화 (Loss, GD, Normalization, CNN/RNN) |
| **Stage 3 (심화/적용)**| **[TabNet_Specialization]** | 💡 예정 | 정형 데이터 딥러닝 모델 구조 및 Interpretabilty 분석 |
| **Final Project**| **[Bidding_Pattern_Analysis]**| 💡 예정 | 실제 입찰 패턴 데이터에 TabNet 모델 적용 및 API 배포 |
---

## 📂 주요 폴더 구조 설명

| 폴더명 | 목적 및 내용 |
| :--- | :--- |
| **`courses/`** | 개별 책이나 강의별 실습 코드와 정리 자료. |
| **`utils/`** | 프로젝트 전반에 걸쳐 사용되는 환경 설정 및 공통 유틸리티 함수 모듈. |
| **`docs/`** | 회고 및 핵심 개념 정리. |
---

## 🛠️ 환경 설정 (Setup)

### 1. Python 환경 준비

```bash
# 1. uv 설치
pip install uv

# 2. 프로젝트 디렉토리로 이동
cd deeplearning_study

# 3. 의존성 설치
uv sync

# 4. 실행
uv run main.py
```