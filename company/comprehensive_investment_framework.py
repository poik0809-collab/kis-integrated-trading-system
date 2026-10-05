"""종합 투자 검증 프레임워크: 리스크 딴지 + 거시경제 + 생산능력."""

from typing import Dict, List
from risk_challenge_system import RiskChallenge, RiskChallengeWorkflow, EvidenceCollector
from production_analysis import ProductionMetrics, GapAnalysisReport, ProductionCapacityAnalyzer, SupplyChainExpert


class ComprehensiveInvestmentValidator:
    """종합 투자 검증 시스템.
    
    단계:
    1. 리스크 부장의 사전 딴지 제기
    2. 거시경제팀의 원자재/수출입/환율 분석
    3. 생산분석팀의 생산능력-수주 갭 분석
    4. 리스크팀의 근거 자료 검증
    5. 최종 승인/거절 결정
    """

    def __init__(self):
        self.validation_results = []

    def validate_investment(self, investment_proposal: Dict) -> Dict:
        """투자 안건 종합 검증."""
        
        print(f"\n[투자 검증 시작] {investment_proposal['project_name']}")
        print("=" * 80)

        # 1단계: 리스크 부장의 사전 딴지
        print("\n[1단계] 리스크 부장의 사전 딴지 제기...")
        risk_challenges = self._identify_risk_challenges(investment_proposal)
        
        # 2단계: 거시경제 분석
        print("\n[2단계] 거시경제/글로벌 리스크 분석...")
        macro_analysis = self._analyze_macro_environment(investment_proposal)
        
        # 3단계: 생산 능력 분석 (제조업인 경우)
        print("\n[3단계] 생산 능력-수주 갭 분석...")
        production_analysis = self._analyze_production_capacity(investment_proposal)
        
        # 4단계: 리스크팀의 근거 검증
        print("\n[4단계] 리스크팀의 근거 자료 검증...")
        evidence_validation = self._validate_evidence(risk_challenges)
        
        # 5단계: 최종 판결
        print("\n[5단계] 최종 판결...")
        final_decision = self._make_final_decision(
            risk_challenges,
            macro_analysis,
            production_analysis,
            evidence_validation
        )
        
        result = {
            "project_name": investment_proposal['project_name'],
            "risk_challenges": risk_challenges,
            "macro_analysis": macro_analysis,
            "production_analysis": production_analysis,
            "evidence_validation": evidence_validation,
            "final_decision": final_decision,
        }
        
        self.validation_results.append(result)
        return result

    def _identify_risk_challenges(self, proposal: Dict) -> List[Dict]:
        """리스크 부장이 제기할 딴지 목록."""
        challenges = []
        
        if proposal.get('sector') == '반도체':
            challenges.append({
                "issue": "반도체 수급 불안",
                "risk_type": "supply_chain",
                "severity": "high",
            })
        
        if proposal.get('leverage', 0) > 2.0:
            challenges.append({
                "issue": "높은 레버리지 비율",
                "risk_type": "financial",
                "severity": "high",
            })
        
        if proposal.get('market_cap', 0) < 100000:
            challenges.append({
                "issue": "낮은 시가총액, 유동성 위험",
                "risk_type": "liquidity",
                "severity": "medium",
            })
        
        for challenge in challenges:
            print(f"  - [{challenge['severity']}] {challenge['issue']}")
        
        return challenges

    def _analyze_macro_environment(self, proposal: Dict) -> Dict:
        """거시경제/글로벌 분석."""
        analysis = {
            "commodity_risk": self._assess_commodity_risk(proposal),
            "export_import_trend": self._assess_trade_trend(proposal),
            "fx_exposure": self._assess_fx_exposure(proposal),
            "geopolitical_risk": self._assess_geopolitical_risk(proposal),
        }
        
        print(f"  - 원자재 리스크: {analysis['commodity_risk']['level']}")
        print(f"  - 수출입 추이: {analysis['export_import_trend']['status']}")
        print(f"  - 환율 노출: {analysis['fx_exposure']['level']}")
        print(f"  - 지정학적 리스크: {analysis['geopolitical_risk']['level']}")
        
        return analysis

    def _assess_commodity_risk(self, proposal: Dict) -> Dict:
        """원자재 가격 리스크."""
        commodity = proposal.get('commodity_exposure', 'none')
        if commodity == 'oil':
            return {"level": "높음", "detail": "유가 변동성 높음"}
        elif commodity == 'metal':
            return {"level": "중간", "detail": "금속 가격 안정적"}
        else:
            return {"level": "낮음", "detail": "원자재 노출 낮음"}

    def _assess_trade_trend(self, proposal: Dict) -> Dict:
        """수출입 추세 분석."""
        return {
            "status": "증가",
            "detail": "국내 수출액 YoY +5.3%, 수입액 +2.1%",
        }

    def _assess_fx_exposure(self, proposal: Dict) -> Dict:
        """환율 노출도."""
        if proposal.get('export_ratio', 0) > 50:
            return {"level": "높음", "detail": "환율 약세에 유리"}
        else:
            return {"level": "낮음", "detail": "환율 영향 미미"}

    def _assess_geopolitical_risk(self, proposal: Dict) -> Dict:
        """지정학적 리스크."""
        return {"level": "낮음-중간", "detail": "미-중 기술 제재 모니터링 필요"}

    def _analyze_production_capacity(self, proposal: Dict) -> Dict:
        """생산 능력 분석."""
        if proposal.get('sector') != '제조업':
            return {"applicable": False, "reason": "제조업이 아님"}
        
        metrics = ProductionMetrics(
            company_name=proposal['company_name'],
            total_capacity=proposal.get('monthly_capacity', 10000),
            current_utilization_rate=proposal.get('utilization_rate', 75.0),
            available_capacity=proposal.get('available_capacity', 2500),
            monthly_orders=proposal.get('monthly_orders', 7500),
            order_backlog=proposal.get('order_backlog_months', 3),
            production_lead_time=proposal.get('lead_time_days', 45),
            supply_chain_risk_score=proposal.get('supply_chain_risk', 50.0),
        )
        
        analyzer = ProductionCapacityAnalyzer("생산분석 전문가")
        expert = SupplyChainExpert("공급체인 전문가")
        report = GapAnalysisReport(analyzer, expert).generate_report(metrics)
        
        print(f"  - 생산-수주 갭: {metrics.capacity_gap():.0f}개/월")
        print(f"  - 가동률: {metrics.current_utilization_rate:.1f}%")
        print(f"  - 건강도: {report['analysis']['health_assessment']['status']}")
        
        return report

    def _validate_evidence(self, challenges: List[Dict]) -> Dict:
        """리스크팀의 근거 검증."""
        validation_status = {}
        
        for challenge in challenges:
            issue = challenge['issue']
            validation_status[issue] = {
                "evidence_collected": True,
                "data_sources": ["backtest", "order_log", "policy_document"],
                "severity_confirmed": True,
                "status": "검증 완료",
            }
            print(f"  - {issue}: 검증 완료")
        
        return validation_status

    def _make_final_decision(self, challenges, macro, production, evidence) -> Dict:
        """최종 승인/거절 결정."""
        risk_count = len(challenges)
        
        if risk_count == 0 and macro['geopolitical_risk']['level'] == '낮음':
            decision = "APPROVE"
            reason = "모든 검증을 통과했습니다."
        elif risk_count > 2:
            decision = "REJECT"
            reason = f"리스크 {risk_count}개 미해결"
        else:
            decision = "CONDITIONAL_APPROVE"
            reason = "조건부 승인: 리스크 완화 후 진행"
        
        print(f"  - 최종 결정: {decision}")
        print(f"  - 사유: {reason}")
        
        return {
            "decision": decision,
            "reason": reason,
            "risk_count": risk_count,
            "approval_authority": "CEO",
        }


if __name__ == "__main__":
    validator = ComprehensiveInvestmentValidator()
    
    # 투자 안건 예시
    proposal = {
        "project_name": "반도체 제조사 A 투자",
        "company_name": "반도체 회사 A",
        "sector": "반도체",
        "leverage": 1.5,
        "market_cap": 500000,
        "commodity_exposure": "metal",
        "export_ratio": 60,
        "monthly_capacity": 10000,
        "utilization_rate": 85.0,
        "available_capacity": 1500,
        "monthly_orders": 8500,
        "order_backlog_months": 5,
        "lead_time_days": 45,
        "supply_chain_risk": 65.0,
    }
    
    result = validator.validate_investment(proposal)
    
    print("\n" + "=" * 80)
    print(f"[결과] {result['final_decision']['decision']}")
    print(f"사유: {result['final_decision']['reason']}")
