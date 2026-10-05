from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class RiskChallenge:
    """리스크 부장이 제기하는 사전 딴지."""
    project_name: str
    issue: str
    risk_type: str
    severity: str
    evidence_needed: List[str] = field(default_factory=list)
    status: str = "OPEN"


@dataclass
class Evidence:
    """딴지 검증에 필요한 자료."""
    source: str
    category: str
    summary: str
    details: Dict[str, object] = field(default_factory=dict)


class RiskDirector:
    """부장급 리스크 담당자. 모든 프로젝트에 사전 딴지를 건다."""

    def __init__(self, name: str):
        self.name = name

    def raise_challenge(self, project_name: str, issue: str, risk_type: str, severity: str) -> RiskChallenge:
        challenge = RiskChallenge(
            project_name=project_name,
            issue=issue,
            risk_type=risk_type,
            severity=severity,
            evidence_needed=[
                "과거 데이터 분석",
                "백테스트 결과",
                "로그 및 주문 이력",
                "규제/운영 정책 확인",
                "포지션 리스크 계산",
            ],
        )
        return challenge


class TeamLeadReviewer:
    """팀장은 딴지의 정확성을 해석하고 사원들이 자료를 찾도록 지시한다."""

    def __init__(self, name: str, team_name: str):
        self.name = name
        self.team_name = team_name

    def assign_review(self, challenge: RiskChallenge) -> Dict[str, object]:
        return {
            "reviewer_team": self.team_name,
            "challenge": challenge.issue,
            "instructions": [
                "딴지의 핵심 문장을 재정의한다",
                "필요한 자료를 분류한다",
                "근거가 수치/로그/문서에서 확인될 수 있는지 점검한다",
                "결론을 승인/수정/보류로 나눈다",
            ],
        }


class EvidenceCollector:
    """대리/사원급 인력. 자료를 찾고 근거를 정리한다."""

    def __init__(self, name: str):
        self.name = name

    def collect(self, challenge: RiskChallenge) -> List[Evidence]:
        evidence = [
            Evidence(
                source="backtest",
                category="performance",
                summary=f"{challenge.project_name}의 과거 성과와 손실 구간을 확인합니다.",
                details={"risk_type": challenge.risk_type, "severity": challenge.severity},
            ),
            Evidence(
                source="order_log",
                category="execution",
                summary="주문 체결 로그와 실패 로그를 점검해 실제 리스크를 확인합니다.",
                details={"issue": challenge.issue},
            ),
            Evidence(
                source="policy",
                category="regulation",
                summary="운영 정책/규제 문서와 현재 현행 기준을 비교합니다.",
                details={"status": challenge.status},
            ),
        ]
        return evidence


class ReviewDecision:
    """딴지 검증 결과를 기록하는 객체."""

    def __init__(self, challenge: RiskChallenge, evidence: List[Evidence]):
        self.challenge = challenge
        self.evidence = evidence

    def decide(self) -> Dict[str, object]:
        if not self.evidence:
            return {"decision": "HOLD", "reason": "근거가 부족합니다."}

        return {
            "decision": "APPROVE",
            "reason": "자료와 로그를 확인했으며, 리스크가 관리 가능 범위로 판단됩니다.",
            "evidence_count": len(self.evidence),
            "project": self.challenge.project_name,
        }


class RiskChallengeWorkflow:
    """리스크 딴지 검증 전체 흐름."""

    def __init__(self, risk_director: RiskDirector, team_lead: TeamLeadReviewer):
        self.risk_director = risk_director
        self.team_lead = team_lead

    def process(self, project_name: str, issue: str, risk_type: str, severity: str, collector: EvidenceCollector):
        challenge = self.risk_director.raise_challenge(project_name, issue, risk_type, severity)
        assignment = self.team_lead.assign_review(challenge)
        evidence = collector.collect(challenge)
        decision = ReviewDecision(challenge, evidence).decide()
        return {
            "challenge": challenge,
            "assignment": assignment,
            "evidence": evidence,
            "decision": decision,
        }


if __name__ == "__main__":
    workflow = RiskChallengeWorkflow(
        risk_director=RiskDirector("리스크부장"),
        team_lead=TeamLeadReviewer("리스크팀장", "리스크관리팀"),
    )
    result = workflow.process(
        project_name="KIS 자동매매 전략 v2",
        issue="급락 시 손실 확대 가능성이 높은 전략입니다.",
        risk_type="market_risk",
        severity="high",
        collector=EvidenceCollector("사원 A"),
    )
    print(result)
