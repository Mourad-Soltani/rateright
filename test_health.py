# Health tests for RateRight
# Signature: Mourad.Soltani

import pytest
from rateright import calculate_hourly_rate

def test_basic_calculation():
    result = calculate_hourly_rate(80000)
    assert result["hourly_rate_recommended"] > 80
    assert result["total_revenue_needed"] > 100000
    assert "signature" in result
    assert result["signature"] == "Mourad.Soltani"

def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculate_hourly_rate(-100)
    with pytest.raises(ValueError):
        calculate_hourly_rate(50000, billable_ratio=0)
    with pytest.raises(ValueError):
        calculate_hourly_rate(50000, billable_ratio=1.5)

def test_billable_impact():
    high_billable = calculate_hourly_rate(80000, billable_ratio=0.8)
    low_billable = calculate_hourly_rate(80000, billable_ratio=0.5)
    assert low_billable["hourly_rate_recommended"] > high_billable["hourly_rate_recommended"]

def test_health_check():
    # Minimal health: function runs and returns expected keys
    result = calculate_hourly_rate(50000)
    required_keys = [
        "desired_takehome", "total_revenue_needed", 
        "hourly_rate_recommended", "signature"
    ]
    for key in required_keys:
        assert key in result
    assert isinstance(result["hourly_rate_recommended"], int)
