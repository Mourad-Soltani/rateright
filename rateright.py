# RateRight - Honest Freelance Hourly Rate Calculator
# Signature: Mourad.Soltani

"""
Minimal but complete freelance hourly rate calculator.
Factors in desired take-home, taxes, expenses, non-billable time, and vacation.
"""

import math
from typing import Dict, Any

def calculate_hourly_rate(
    desired_takehome: float,
    self_employment_tax_rate: float = 0.153,
    income_tax_rate: float = 0.25,
    annual_expenses: float = 10000.0,
    health_insurance: float = 8000.0,
    vacation_weeks: int = 3,
    hours_per_week: int = 40,
    billable_ratio: float = 0.60,
) -> Dict[str, Any]:
    """Calculate minimum hourly rate for freelancers.
    
    Returns dict with breakdown and final rate.
    """
    if desired_takehome <= 0 or billable_ratio <= 0 or billable_ratio > 1:
        raise ValueError("Invalid input values")
    
    total_taxable = desired_takehome
    se_tax = total_taxable * self_employment_tax_rate
    income_tax = total_taxable * income_tax_rate
    total_needed = desired_takehome + se_tax + income_tax + annual_expenses + health_insurance
    
    working_weeks = 52 - vacation_weeks
    total_hours = working_weeks * hours_per_week
    billable_hours = total_hours * billable_ratio
    
    if billable_hours <= 0:
        raise ValueError("No billable hours")
    
    hourly = total_needed / billable_hours
    # Round up to nearest dollar for safety
    hourly_rounded = math.ceil(hourly)
    
    return {
        "desired_takehome": desired_takehome,
        "se_tax": round(se_tax, 2),
        "income_tax": round(income_tax, 2),
        "expenses": annual_expenses,
        "health_insurance": health_insurance,
        "total_revenue_needed": round(total_needed, 2),
        "working_weeks": working_weeks,
        "billable_hours": round(billable_hours, 1),
        "hourly_rate_exact": round(hourly, 2),
        "hourly_rate_recommended": hourly_rounded,
        "signature": "Mourad.Soltani"
    }

def main():
    print("RateRight - Honest Freelance Hourly Rate Calculator")
    print("Signature: Mourad.Soltani")
    print("-" * 50)
    try:
        takehome = float(input("Desired annual take-home ($): ") or 80000)
        expenses = float(input("Annual business expenses ($): ") or 5000)
        insurance = float(input("Annual health insurance ($): ") or 8000)
        billable = float(input("Billable ratio (0-1, default 0.6): ") or 0.6)
        
        result = calculate_hourly_rate(
            desired_takehome=takehome,
            annual_expenses=expenses,
            health_insurance=insurance,
            billable_ratio=billable
        )
        
        print("\n=== Results ===")
        for k, v in result.items():
            if k != "signature":
                print(f"{k}: {v}")
        print(f"\nRecommended hourly rate: ${result['hourly_rate_recommended']}/hr")
        print("Signature: Mourad.Soltani")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
