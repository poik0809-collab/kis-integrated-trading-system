from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ExecutiveRole:
    name: str
    title: str
    decision_right: str


@dataclass
class TeamMember:
    name: str
    title: str
    team: str
    responsibilities: List[str] = field(default_factory=list)


class InvestmentCompanyOrg:
    """투자회사형 AI 에이전트 조직 모델."""

    def __init__(self):
        self.ceo = ExecutiveRole("사장님", "CEO", "최종 투자 승인")
        self.directors = {
            "investment": ExecutiveRole("투자부장", "Director of Investment", "전략/자산배분 승인"),
            "risk": ExecutiveRole("리스크부장", "Director of Risk", "사전 딴지 제기 및 위험 승인 거부"),
            "operations": ExecutiveRole("운영부장", "Director of Operations", "실행/운영 관리"),
            "technology": ExecutiveRole("기술부장", "Director of Technology", "데이터/시스템/AI 관리"),
        }

        self.team_leads = [
            TeamMember("전략팀장", "Team Lead", "전략팀", ["시장분석", "전략 수립", "백테스트 검증"]),
            TeamMember("리스크팀장", "Team Lead", "리스크팀", ["사전 딴지 검증", "리스크 모델 검토", "근거 수집 관리"]),
            TeamMember("실행팀장", "Team Lead", "실행팀", ["주문 실행", "체결 검증", "모니터링"]),
            TeamMember("데이터팀장", "Team Lead", "데이터팀", ["데이터 수집", "데이터 정제", "AI 학습"]),
            TeamMember("개발팀장", "Team Lead", "개발팀", ["API 연동", "시스템 안정화", "배포 관리"]),
            TeamMember("고객운영팀장", "Team Lead", "고객운영팀", ["리포트", "고객 커뮤니케이션", "운영 개선"]),
        ]

        self.staff = [
            TeamMember("전략분석 사원 1", "Analyst", "전략팀", ["시장 데이터 분석", "전략 후보 검토"]),
            TeamMember("전략분석 사원 2", "Analyst", "전략팀", ["시그널 검증", "데이터 비교"]),
            TeamMember("전략분석 사원 3", "Analyst", "전략팀", ["시장 상황 점검", "리포트 작성"]),
            TeamMember("리스크검증 사원 1", "Risk Analyst", "리스크팀", ["자료 수집", "근거 정리", "리스크 계산"]),
            TeamMember("리스크검증 사원 2", "Risk Analyst", "리스크팀", ["백테스트 검토", "손실 한도 확인"]),
            TeamMember("주문모니터링 사원 1", "Operator", "실행팀", ["주문 추적", "정상 여부 점검"]),
            TeamMember("주문모니터링 사원 2", "Operator", "실행팀", ["체결 로그 확인", "오류 대응"]),
            TeamMember("주문모니터링 사원 3", "Operator", "실행팀", ["실시간 이슈 관리", "업무 분담"]),
            TeamMember("데이터분석 사원 1", "Data Analyst", "데이터팀", ["데이터 정제", "전처리"]),
            TeamMember("데이터분석 사원 2", "Data Analyst", "데이터팀", ["AI 데이터셋 구성", "지표 생성"]),
            TeamMember("고객리포트 사원 1", "Operations Staff", "고객운영팀", ["리포트 생성", "투자 성과 정리"]),
            TeamMember("고객리포트 사원 2", "Operations Staff", "고객운영팀", ["고객 대응", "운영 문서화"]),
        ]

    def challenge_policy(self) -> Dict[str, List[str]]:
        return {
            "risk_director_rule": [
                "모든 신규 프로젝트는 사전 리스크 딴지 검증을 통과해야 한다.",
                "딴지는 단순한 반대가 아니라 근거 기반의 검증이다.",
                "팀장과 사원은 자료와 과거 데이터를 기반으로 타당성을 검토한다.",
                "결론은 승인, 보완, 보류 중 하나로 명시한다.",
            ]
        }


if __name__ == "__main__":
    org = InvestmentCompanyOrg()
    print(org.ceo)
    print(org.directors["risk"])
    print(len(org.team_leads), len(org.staff))
    print(org.challenge_policy())
