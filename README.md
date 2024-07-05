# 💻 Test Automation Framework |

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions) 
![Pytest](https://img.shields.io/badge/Pytest-2088FF?style=for-the-badge&logo=PyTest&logoColor=white)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-3.141.59-brightgreen)

## Overview

This project demonstrates the use of Selenium WebDriver with Python to automate browser interactions for testing web applications. It includes examples of various Selenium functionalities such as navigating web pages, interacting with web elements, handling multiple windows, and generating test reports.



## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.11
- pip (Python package installer)
- Google Chrome or Mozilla Firefox browser
- ChromeDriver or GeckoDriver (compatible with your browser version)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/piyush466/make_my_trip.git
    cd make_my_trip
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running Tests

To execute the test cases, use the following command:

```bash
pytest --alluredir=./reports

Folder Structure

seleniumJenkins/
├── tests/
│   ├── test_example.py
│   └── ...
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── ...
├── utils/
│   ├── readProperties.py
│   ├── helpers.py
│   └── ...
├── reports/
│   └── reports.html
├── requirements.txt
├── README.md
└── ...




