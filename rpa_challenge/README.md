# RPA Challenge

## Table of Contents
- [Context](#context)
- [Requirements](#requirements)
  - [Technical Requirements](#technical-requirements)
  - [Functional Requirements](#functional-requirements)
  - [Non-Functional Requirements](#non-functional-requirements)
- [Input/Output](#inputoutput)
- [Expected Results](#expected-results)
- [Workflow](#workflow)
- [How to use](#how-to-use)
- [How to Obtain Chromedriver](#how-to-obtain-chromedriver)

## Context

**RPA Challenge** aims to automate the filling of an online form to save time in entering multiple pieces of information in a repetitive context. This project was developed to demonstrate the ability to read and insert information quickly and automatically.

#### Requirements:

To ensure the proper functioning of the project, the following requirements must be met:

## Technical Requirements
- **Programming Language**: `python3.6+`
- **Required Libraries**: `requirements.txt`
- **Operating System**: `Windows`
- **Other Requirements**: `Chrome` / `Chromedriver`

**Functional Requirements**
- Internet connection;
- Connection with the Chrome browser;
- Online form available;
- Input data for filling out the form;

**Non-Functional Requirements**
- Efficient performance;
- Ease of maintenance;

## Input/Output

```bash
project/
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── .env
    ├── .env.example
    ├── utils.py
    ├── main.py
    └── data/
        └── challenge.xlsx
    └── files/
        └── excel.py
    └── web/
        └── chrome.py
```

**Input**
- Excel file (`challenge.xlsx`) containing the data to be entered into the form.

**Output**
- Execution logs;
- Screenshots of the completed form;

**Expected Results**
- Form correctly filled with the provided data;
- Significant reduction in manual filling time;
- Detailed execution reports;

## Workflow
1. Read the data from the Excel file (`challenge.xlsx`).
2. Open the Chrome browser and access the online form.
3. Fill out the form with the read data.
4. Capture the ranking message of the completed form.
5. Save the logs.

## How to use
1. Clone the repository:
    ```bash
    git clone https://github.com/ThiagoLozano/MyPortfolio.git
    cd rpa_challenge
    ```
2. Install the dependencies listed in `requirements.txt`.
3. Configure the environment in the `env.py` file.
4. Run the main script `main.py`.

## How to Obtain Chromedriver

1. Go to the [Chromedriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).
2. Download the version that matches your Chrome browser version.
3. Extract the downloaded file.
4. Move the `chromedriver` executable to a directory included in your system's PATH, or specify the path to the executable in your script.
