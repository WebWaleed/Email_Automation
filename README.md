# Email Automation Script

This project is a Python script that automates email interactions using Selenium WebDriver for Gmail, Yahoo, and Outlook. It reads a list of email addresses and passwords from a CSV file and offers the ability to compose, read, or manage spam emails across multiple email providers.

## Features

- Login automation for Gmail, Yahoo, and Outlook
- Options to:
  - Compose and send an email
  - Read the first email in the inbox
  - Mark the first email in the spam folder as "Not Spam" (for Yahoo and Outlook)
- Suppresses unwanted output in the terminal for a cleaner user experience

## Requirements

- Python 3.x
- [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) and Chrome WebDriver
- Chrome browser
- `pandas` library for reading CSV files

## Setup

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
