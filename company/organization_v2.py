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


class InvestmentCompanyOrgV2:
    """AI 투자회사 조직 구조 v2: 원자재/수출입/생산능력 분석 추가."""

    def __init__(self):
        self.ceo = ExecutiveRole("사장님", "CEO", "최종 투자 승인")
        self.directors = {
            "investment": ExecutiveRole("투자부장", "Director of Investment", "전략/자산배분 승인"),
            "risk": ExecutiveRole("리스크부장(CRO)", "Chief Risk Officer", "사전 딴지/위험 승인거절"),
            "operations": ExecutiveRole("운영부장", "Director of Operations", "실행/주문 승인"),
            "macro_global": ExecutiveRole("거시경제부장", "Director of Macro & Global", "거시경제 정책 승인"),
        }

        self.team_leads = [
            TeamMember(
                "전략팀장",
                "Team Lead",
                "전략팀",
                ["국내 주식 시장 분석", "기업 펀더멘탈 분석", "섹터 분석"],
            ),
            TeamMember(
                "거시경제/글로벌팀장",
                "Team Lead",
                "거시경제팀",
                ["원자재 가격 분석", "수출입 통계 추적", "환율/글로벌 리스크"],
            ),
            TeamMember(
                "생산능력분석팀장",
                "Team Lead",
                "생산분석팀",
                ["기업 생산 능력 분석", "수주-생산 갭 계산", "공급 체인 리스크 평가"],
            ),
            TeamMember(
                "리스크팀장(CRO팀)",
                "Team Lead",
                "리스크팀",
                ["사전 딴지 검증", "근거 자료 수집", "위험도 계산"],
            ),
            TeamMember(
                "실행팀장",
                "Team Lead",
                "실행팀",
                ["주문 실행", "체결 추적", "실시간 모니터링"],
            ),
            TeamMember(
                "데이터/개발팀장",
                "Team Lead",
                "기술팀",
                ["데이터 수집/정제", "백테스트", "시스템 개발"],
            ),
        ]

        self.staff = [
            # 전략팀 (3명)
            TeamMember("전략분석 사원 1", "Analyst", "전략팀", ["기업 실적 분석", "펀더멘탈 리포트"]),
            TeamMember("전략분석 사원 2", "Analyst", "전략팀", ["기술적 분석", "차트 분석"]),
            TeamMember("전략분석 사원 3", "Analyst", "전략팀", ["섹터 동향 분석", "시장 뉴스 모니터링"]),
            # 거시경제팀 (3명)
            TeamMember(
                "원자재분석 사원 1",
                "Commodity Analyst",
                "거시경제팀",
                ["유가/금속 가격 추적", "원자재 차트 분석"],
            ),
            TeamMember(
                "수출입분석 사원 1",
                "Trade Analyst",
                "거시경제팀",
                ["수출입 통계 수집", "무역 불균형 분석"],
            ),
            TeamMember(
                "글로벌리스크 사원 1",
                "Global Risk Analyst",
                "거시경제팀",
                ["환율 변동 분석", "지정학적 리스크"],
            ),
            # 생산능력분석팀 (3명)
            TeamMember(
                "생산능력분석 사원 1",
                "Capacity Analyst",
                "생산분석팀",
                ["기업 생산 능력 조사", "설비 규모 분석"],
            ),
            TeamMember(
                "생산능력분석 사원 2",
                "Capacity Analyst",
                "생산분석팀",
                ["수주-생산 갭 계산", "가동률 예측"],
            ),
            TeamMember(
                "공급체인리스크 사원 1",
                "Supply Chain Analyst",
                "생산분석팀",
                ["공급 체인 리스크 평가", "납기 리스크 분석"],
            ),
            # 리스크팀 (2명)
            TeamMember("리스크검증 사원 1", "Risk Analyst", "리스크팀", ["딴지 근거 검증", "자료 수집"]),
            TeamMember("리스크검증 사원 2", "Risk Analyst", "리스크팀", ["데이터 검산", "근거 정리"]),
        ]

    def challenge_policy(self) -> Dict[str, List[str]]:
        return {
            "risk_director_rule": [
                "모든 신규 프로젝트는 사전 리스크 딴지 검증을 통과해야 한다.",
                "딴지는 단순 반대가 아니라 근거 기반의 검증이다.",
                "팀장과 사원은 자료, 로그, 문서, 백테스트 결과로 타당성을 검토한다.",
                "결론은 승인, 수정, 보류 중 하나로 명시한다.",
            ],
            "macro_global_analysis": [
                "모든 투자 결정에 원자재 가격 변동을 포함한다.",
                "수출입 금액 추이를 분기별로 추적한다.",
                "환율 변동이 포트폴리오에 미치는 영향을 분석한다.",
                "글로벌 리스크(무역 분쟁, 지정학)를 사전에 파악한다.",
            ],
            "production_capacity_analysis": [
                "모든 제조업 투자 대상의 생산-수주 갭을 계산한다.",
                "공급 체인 리스크를 정량화한다.",
                "기업의 실제 이익 창출 능력(생산성)을 평가한다.",
                "과잉 생산 능력 또는 부족 능력을 조기에 파악한다.",
            ],
        }

    def organizational_chart(self) -> Dict[str, List]:
        """조직도 반환."""
        return {
            "executives": [self.ceo, *self.directors.values()],
            "team_leads": self.team_leads,
            "staff": self.staff,
            "total_members": 1 + len(self.directors) + len(self.team_leads) + len(self.staff),
        }


if __name__ == "__main__":
    org = InvestmentCompanyOrgV2()
    chart = org.organizational_chart()
    print(f"조직 규모: {chart['total_members']}명")
    print(f"CEO: {org.ceo.name}")
    print(f"\n부장 {len(org.directors)}명:")
    for dept, director in org.directors.items():
        print(f"  - {director.name} ({director.title})")
    print(f"\n팀장 {len(org.team_leads)}명:")
    for lead in org.team_leads:
        print(f"  - {lead.name} ({lead.team})")
    print(f"\n사원 {len(org.staff)}명:")
    for staff in org.staff:
        print(f"  - {staff.name} ({staff.team})")
