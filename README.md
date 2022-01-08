# Loan Qualifier App

This Loan Qualifier App is a command-line interface application allowing users to filter loans from various lenders based on their unique criteria and then save them to a new .csv file. The app works by taking in loan information provided by the user (in this example, the 'daily_rate_sheet.csv' file) and cross-referencing it against a number of questions that determine the user's eligibility (including credit quality, monthly debt, monthly income, requested loan size, and home value). It then returns a list of qualifying loans and saves them to a new .csv file upon the user's request.

---

## Technologies

This app runs on python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and responses.

---

## Installation Guide

Please install the following dependencies:

```python
  pip install fire
  pip install questionary
```

---

## Usage

To use the loan qualifier application, clone the repository and run **app.py** with:

```python
python app.py
```
Upon launching, you will be prompted to load the full loan data set and answer a few questions about your credit score, financial status, and desired loan per the screenshot below:

![Initial_Prompts](/images/initial_prompt_screenshot.png)

Once the summary information is returned, you will be asked if you'd like to save the list of qualifying loans. If so, please enter a file path for the newly created file:

![Save_Prompts](/images/save_prompt_screenshot.png)

---

## Contributors

This app was created by Nico Cortese with support from the lovely Fintech Coding Boot Camp Team at Boot Camp Spot / Columbia School of Engineering

Nico Cortese

XXX-XXX-XXXX

XXXX@gmail.com

---

## License

MIT

