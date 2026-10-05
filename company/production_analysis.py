from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class CompanyHealthStatus(str, Enum):
    """기업 생산성 건강도."""
    EXCELLENT = "우수"
    GOOD = "양호"
    WARNING = "주의"
    CRITICAL = "위험"


@dataclass
class ProductionMetrics:
    """생산 능력 지표."""
    company_name: str
    total_capacity: float  # 월 생산 능력 (단위: 개)
    current_utilization_rate: float  # 현재 가동률 (%)
    available_capacity: float  # 사용 가능한 여유 생산력
    monthly_orders: float  # 월 수주량
    order_backlog: float  # 수주 잔량 (몇 개월치)
    production_lead_time: int  # 생산 리드타임 (일)
    supply_chain_risk_score: float  # 공급 체인 리스크 점수 (0~100)

    def capacity_gap(self) -> float:
        """생산 능력 - 수주량 갭 계산."""
        return self.total_capacity - self.monthly_orders

    def utilization_forecast(self, months_ahead: int = 3) -> float:
        """향후 가동률 예측 (수주 잔량 기반)."""
        if self.total_capacity == 0:
            return 0.0
        forecast_load = (self.order_backlog + (self.monthly_orders * months_ahead)) / (self.total_capacity * months_ahead)
        return min(forecast_load * 100, 100.0)  # 최대 100%

    def surplus_capacity(self) -> float:
        """초과 생산 능력 (%)."""
        if self.total_capacity == 0:
            return 0.0
        return ((self.total_capacity - self.monthly_orders) / self.total_capacity) * 100

    def health_status(self) -> CompanyHealthStatus:
        """기업 생산성 건강도."""
        utilization = self.current_utilization_rate
        gap = self.capacity_gap()
        supply_risk = self.supply_chain_risk_score

        if utilization > 85 and gap < 0 and supply_risk < 30:
            return CompanyHealthStatus.EXCELLENT
        elif 70 <= utilization <= 85 and gap >= 0 and supply_risk < 50:
            return CompanyHealthStatus.GOOD
        elif 50 <= utilization < 70 or supply_risk >= 50:
            return CompanyHealthStatus.WARNING
        else:
            return CompanyHealthStatus.CRITICAL


@dataclass
class SupplyChainRisk:
    """공급 체인 리스크 분석."""
    risk_factor: str
    impact_level: str  # "높음", "중간", "낮음"
    probability: float  # 0~1
    mitigation_status: str  # "완화됨", "진행 중", "미대응"
    affected_products: List[str] = field(default_factory=list)


class ProductionCapacityAnalyzer:
    """기업 생산 능력 분석 전문가."""

    def __init__(self, name: str):
        self.name = name
        self.analysis_history: List[Dict] = []

    def analyze(self, metrics: ProductionMetrics, supply_risks: List[SupplyChainRisk]) -> Dict:
        """생산 능력과 수주량 갭 분석."""
        gap = metrics.capacity_gap()
        utilization_forecast = metrics.utilization_forecast()
        surplus = metrics.surplus_capacity()
        health = metrics.health_status()

        analysis = {
            "company": metrics.company_name,
            "analyst": self.name,
            "current_metrics": {
                "total_capacity": metrics.total_capacity,
                "current_utilization_rate": metrics.current_utilization_rate,
                "monthly_orders": metrics.monthly_orders,
                "order_backlog_months": metrics.order_backlog,
                "capacity_gap": gap,
                "surplus_capacity_percent": surplus,
            },
            "forecast": {
                "utilization_3months": utilization_forecast,
                "production_lead_time_days": metrics.production_lead_time,
            },
            "supply_chain_analysis": {
                "risk_score": metrics.supply_chain_risk_score,
                "risk_factors": [r.risk_factor for r in supply_risks],
                "critical_risks": [r for r in supply_risks if r.impact_level == "높음"],
            },
            "health_assessment": {
                "status": health.value,
                "recommendation": self._recommend(gap, surplus, utilization_forecast, health),
            },
        }

        self.analysis_history.append(analysis)
        return analysis

    def _recommend(self, gap: float, surplus: float, forecast: float, health: CompanyHealthStatus) -> str:
        """투자 권고사항."""
        if health == CompanyHealthStatus.EXCELLENT:
            return "매수: 생산 능력이 수주를 처리하기에 충분하고 공급 체인 리스크 낮음"
        elif health == CompanyHealthStatus.GOOD:
            return "매수: 양호한 생산성, 약간의 여유 있음"
        elif health == CompanyHealthStatus.WARNING:
            return "보류: 생산 능력 검토 필요, 공급 체인 리스크 주시"
        else:
            return "매도/회피: 생산 능력 부족 또는 공급 체인 심각한 리스크"

    def identify_bottleneck(self, metrics: ProductionMetrics) -> Dict:
        """병목 지점 파악."""
        if metrics.capacity_gap() < 0:
            return {
                "bottleneck": "생산 능력 부족",
                "severity": "높음",
                "shortage_amount": abs(metrics.capacity_gap()),
                "required_action": "추가 생산 설비 투자 또는 수주 조정 필요",
            }
        elif metrics.current_utilization_rate < 50:
            return {
                "bottleneck": "과잉 생산 능력",
                "severity": "중간",
                "idle_capacity": metrics.surplus_capacity(),
                "required_action": "고정 비용 부담 큼, 가동률 개선 또는 신규 사업 검토",
            }
        else:
            return {
                "bottleneck": "None",
                "severity": "낮음",
                "status": "정상 가동 중",
            }


class SupplyChainExpert:
    """공급 체인 리스크 전문가."""

    def __init__(self, name: str):
        self.name = name

    def assess_risks(self, metrics: ProductionMetrics) -> List[SupplyChainRisk]:
        """공급 체인 리스크 평가."""
        risks = []

        # 리드타임이 길면 공급 리스크 높음
        if metrics.production_lead_time > 60:
            risks.append(
                SupplyChainRisk(
                    risk_factor="장 리드타임",
                    impact_level="높음",
                    probability=0.7,
                    mitigation_status="미대응",
                    affected_products=[metrics.company_name],
                )
            )

        # 수주 잔량이 많으면 수급 조임
        if metrics.order_backlog > 6:
            risks.append(
                SupplyChainRisk(
                    risk_factor="납기 연장 위험",
                    impact_level="높음",
                    probability=0.6,
                    mitigation_status="진행 중",
                    affected_products=[metrics.company_name],
                )
            )

        # 공급 체인 위험도 높으면
        if metrics.supply_chain_risk_score > 70:
            risks.append(
                SupplyChainRisk(
                    risk_factor="원재료 가격 급등 또는 공급 중단",
                    impact_level="높음",
                    probability=0.5,
                    mitigation_status="완화됨",
                    affected_products=[metrics.company_name],
                )
            )

        return risks

    def forecast_supply_shortage(self, metrics: ProductionMetrics, months_ahead: int = 6) -> Dict:
        """공급 부족 예측."""
        forecast_production = metrics.total_capacity * months_ahead
        forecast_demand = (metrics.monthly_orders + metrics.order_backlog) * months_ahead
        shortage = forecast_demand - forecast_production

        return {
            "period_months": months_ahead,
            "forecasted_production": forecast_production,
            "forecasted_demand": forecast_demand,
            "shortage_risk": shortage > 0,
            "shortage_amount": max(shortage, 0),
            "confidence": "높음" if metrics.order_backlog > 3 else "낮음",
        }


class GapAnalysisReport:
    """생산 능력-수주량 갭 분석 리포트."""

    def __init__(self, analyzer: ProductionCapacityAnalyzer, expert: SupplyChainExpert):
        self.analyzer = analyzer
        self.expert = expert

    def generate_report(self, metrics: ProductionMetrics) -> Dict:
        """종합 리포트 생성."""
        supply_risks = self.expert.assess_risks(metrics)
        analysis = self.analyzer.analyze(metrics, supply_risks)
        bottleneck = self.analyzer.identify_bottleneck(metrics)
        shortage_forecast = self.expert.forecast_supply_shortage(metrics)

        return {
            "report_title": f"{metrics.company_name} 생산 능력 분석 리포트",
            "analyst": self.analyzer.name,
            "supply_chain_expert": self.expert.name,
            "analysis": analysis,
            "bottleneck": bottleneck,
            "supply_forecast": shortage_forecast,
            "investment_recommendation": analysis["health_assessment"]["recommendation"],
        }


if __name__ == "__main__":
    # 예시: 반도체 회사 A
    metrics = ProductionMetrics(
        company_name="반도체 회사 A",
        total_capacity=10000,  # 월 10,000개
        current_utilization_rate=85.0,  # 현재 85% 가동
        available_capacity=1500,
        monthly_orders=8500,  # 월 수주 8,500개
        order_backlog=5,  # 5개월치 수주 잔량
        production_lead_time=45,  # 생산 리드타임 45일
        supply_chain_risk_score=65.0,  # 중간 정도 리스크
    )

    analyzer = ProductionCapacityAnalyzer("생산성 분석가")
    expert = SupplyChainExpert("공급 체인 전문가")
    report_generator = GapAnalysisReport(analyzer, expert)

    report = report_generator.generate_report(metrics)
    print(f"회사: {report['report_title']}")
    print(f"분석가: {report['analyst']}, 공급 체인 전문가: {report['supply_chain_expert']}")
    print(f"\n생산 능력: {metrics.total_capacity}개/월")
    print(f"월 수주량: {metrics.monthly_orders}개")
    print(f"생산-수주 갭: {metrics.capacity_gap()}개/월")
    print(f"\n건강도: {report['analysis']['health_assessment']['status']}")
    print(f"투자 권고: {report['analysis']['health_assessment']['recommendation']}")
    print(f"\n병목 지점: {report['bottleneck']['bottleneck']} ({report['bottleneck']['severity']})")
    print(f"공급 부족 예측: {report['supply_forecast']['shortage_risk']}")
