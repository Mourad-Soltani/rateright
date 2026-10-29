# RateRight

Honest Freelance Hourly Rate Calculator for Solo Founders and Freelancers.

**Signature: Mourad.Soltani**

## Idea

A small, shippable micro-tool that helps freelancers and solo product engineers calculate a realistic hourly rate. It accounts for taxes, expenses, health insurance, vacation, and non-billable time — the things most people forget, leading to undercharging.

Trending in 2026 among indie hackers and remote freelancers who need better pricing without complex SaaS.

No similar exact open-source implementation focused on this transparent breakdown with recommended ceiling was found in public GitHub searches for the specific formula combination used here (checked against common freelance rate repos).

## Features

- Simple CLI calculator
- Full breakdown of revenue needed
- Recommended rounded-up rate
- Local, no accounts, no tracking
- Health tests included

## Quick Start

```bash
cd rateright
python rateright.py
```

Or import the function:

```python
from rateright import calculate_hourly_rate
print(calculate_hourly_rate(80000))
```

## Tests

```bash
pip install pytest
pytest test_health.py -v
```

All health tests must pass before shipping.

## Tech

Pure Python 3, no dependencies for core.

## License

MIT - see LICENSE

Signature: Mourad.Soltani
