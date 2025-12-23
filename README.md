# n11 Search Module – Load Testing

This project contains load test scenarios to evaluate the behavior and performance of the **search module** on the n11 website.

The focus is on validating search functionality and observing response behavior under simulated user activity using **Locust**.

---

## Tech Stack
- Python
- Locust (HTTP-based load testing tool)
- Requests (via Locust HTTP client)

---

## Scope of Testing

The load tests cover the following user interactions:

### Scenario 1: Homepage Access
- User opens the n11 homepage
- Verifies that the homepage responds successfully

### Scenario 2: Product Search
- User searches for popular keywords such as:
  - iphone
  - laptop
  - shoes
  - mobile
  - tv
- Validates that the search results page loads correctly

---

## Validations Performed

For each request, the following checks are applied:

- HTTP status code should be **200**
- Response time should be within an acceptable limit (baseline: **≤ 2 seconds**)
- Any failed request is explicitly marked as a failure in Locust statistics

---

## Load Configuration

- Virtual Users: **1**
- Spawn Rate: **1 user**
- Think Time: **2–5 seconds** between actions
- Task Distribution:
  - Homepage access: lower weight
  - Search action: higher weight (to simulate real user behavior)

---

## How to Run the Test

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### Start Locust
```bash
locust
```