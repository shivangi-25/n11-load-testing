# n11 Search Load Test

This project contains a basic load test for the search module of https://www.n11.com
using Locust.

## Scenario Covered
- Search for a product keyword from the header (e.g. iphone)
- Validate search results page response

## Prerequisites
- Python 3.8+
- pip

## Setup
```bash
pip install -r requirements.txt
```

## Run Load Test
```bash
locust
```
#### Open browser & go to http://localhost:8089

## Additional Test Scenarios (Designed)

### Scenario 3: Empty Search
- Submit search request with empty query
- Expected: No server error (4xx/5xx), graceful handling

### Scenario 4: Special Characters Search
- Keywords: @#$%, !!!, <>
- Expected: Application handles input safely without errors

### Scenario 5: Load Test (Baseline)
- Users: 1
- Repeated searches with think time
- Metrics observed:
  - Average response time
  - Maximum response time
  - Error rate
