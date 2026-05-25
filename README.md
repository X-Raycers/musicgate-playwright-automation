# MusicGate Playwright Automation

UI automation testing framework for the MusicGate e-commerce website using Playwright, Pytest, Page Object Model (POM), and Allure Reports.

---

# About The Project

MusicGate is an Israeli e-commerce website and physical music store focused on musical instruments, amplifiers, keyboards, percussion instruments, audio equipment, and accessories.

This project was created in order to practice and improve real-world UI automation testing skills on a live WooCommerce-based website with dynamic user interactions and complex navigation behavior.

The framework includes automated coverage for:
- Homepage
- Product Search
- Login Functionality
- Shopping Cart
- Product Categories
- Footer Navigation

A total of 46 automated UI tests were created during the project.

---

# Technologies Used

- Python
- Playwright
- Pytest
- Allure Reports
- Page Object Model (POM)
- GitHub

---

# Framework Architecture

The project follows the Page Object Model (POM) design pattern in order to improve:
- Readability
- Maintainability
- Reusability
- Scalability

The framework structure includes:
- Tests
- Page Objects
- Base Pages
- Allure Reporting

---

# Challenges During Automation

This project was built on a real WooCommerce-based e-commerce website, which introduced several automation challenges during development and execution.

The purpose of these tests was not only to validate functionality, but also to understand how unstable UI behavior, timing issues, and dynamic rendering affect automation reliability in real-world environments.

## Homepage Stability

The homepage became one of the most important parts of the framework because many tests depended on it as the main entry point.

Several failures were caused by:
- Incomplete page loading
- Dynamic content rendering
- Navigation timing issues
- Menus loading before the page fully stabilized

To improve execution stability, additional synchronization and improved page loading strategies were introduced through the BasePage architecture.

---

## Mega Menu and Categories

The categories section was one of the most unstable areas of the website during automation.

Challenges included:
- Dynamic mega menus
- Hover-sensitive navigation
- Menus collapsing during execution
- Click interception issues
- Timeout failures on category navigation

These behaviors became more noticeable during faster execution speeds.

---

## Search Functionality

The search system generally behaved well, but some issues appeared during repeated executions.

Observed issues included:
- Slow search result rendering
- Delayed page updates
- Dynamic sorting behavior
- Timing inconsistencies after navigation

Different SlowMo values were tested in order to improve reliability and reduce flaky behavior.

---

## Shopping Cart Behavior

The shopping cart included several AJAX-based UI updates which introduced synchronization challenges.

Observed behaviors:
- Delayed quantity updates
- Dynamic cart refreshes
- Temporary UI inconsistencies
- Delayed cart counter rendering

Although most cart tests became stable, the WooCommerce rendering behavior still caused occasional inconsistencies.

---

## Checkout Flow

The checkout flow was intentionally excluded from the final automation scope due to instability and excessive complexity for the current framework stage.

Main challenges:
- Multiple redirects
- Returning to previous pages
- Dynamic checkout rendering
- Session-related inconsistencies
- Unstable automation flow behavior
- Highly dynamic WooCommerce updates

The checkout flow required significantly more advanced synchronization and state handling than other tested areas.

---

## Registration Flow

The registration flow also introduced several automation difficulties.

Observed issues:
- Dynamic form behavior
- Inconsistent page refreshes
- Validation timing issues
- Unexpected redirects
- State instability between executions

Because of this, registration automation was not fully included in the final stable framework scope.

---

## Social Media Redirects

Footer social media tests occasionally failed due to:
- External redirects
- Popup behavior
- Browser security handling
- Timing inconsistencies after redirection

These failures were environmental and UI-related rather than framework-related.

---

# Stability Benchmark Testing

Several SlowMo configurations were tested in order to evaluate framework stability under different execution speeds.

Tested values:
- 1000ms
- 2000ms
- 3000ms
- 4000ms
- 5000ms

Observed results:
- Lower SlowMo values produced more failures
- Faster execution exposed additional timing issues
- 4000ms produced the most stable overall execution results

Final benchmark result:
- 46 automated tests
- 82.6% pass rate

---

# Future Improvements

Possible future improvements for the framework may include:
- Better synchronization strategies
- Improved locator stability
- Retry mechanisms
- Advanced waiting logic
- More resilient navigation handling
- Improved support for highly dynamic WooCommerce behavior

---

# Personal Interest

I have a personal interest in musical instruments and personally purchased musical equipment from the physical MusicGate store, including:
- A classical guitar
- Guitar accessories
- An electric guitar amplifier

I also own:
- Two classical guitars
- One acoustic guitar
- One electric guitar

This project combined my interest in music with my passion for software QA and automation testing.

---

# Running The Tests

## Supported Platforms

This framework supports:
- Windows
- macOS
- Linux distributions (including Ubuntu)

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Run All Tests

```bash
pytest
```

---

## Run Tests With SlowMo

```bash
pytest --headed --slowmo 4000
```

---

# Allure Reports

Generate Allure report:

```bash
allure generate allure-results -o allure-report --clean
```

Open Allure report:

```bash
allure open allure-report
```
