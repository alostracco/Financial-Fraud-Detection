# Financial Fraud Detection Application
By: Aidan LoStracco, Adam Wilson, and Sean McCorquodale

## Overview

This project implements a financial fraud detection system using machine learning techniques with the help of PostgreSQL and Apache MADlib. The application analyzes transaction data that may indicate fraudulent activity.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Configuration](#database-configuration)
- [Usage](#usage)
  - [Run Logistic Regression](#run-logistic-regression)
  - [View Results](#view-results)
- [Key Considerations](#key-considerations)

## Features

- **Fraud Detection**: Uses logistic regression via MADlib to identify potentially fraudulent transactions.
- **Scalable Setup**: Designed to run on AWS with PostgreSQL and MADlib.
- **Python Integration**: Connects to PostgreSQL using SQLAlchemy and psycopg2.

## Dataset

The dataset used for this project is the [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle. This dataset contains transactions made by credit cards in September 2013 by European cardholders. It presents transactions that occurred in two days, where there are 492 frauds out of 284,807 transactions.

## Setup

### Prerequisites

- Python 3.6+
- PostgreSQL 11+
- Apache MADlib 2.1

### Installation

#### 1. Clone the repository

```bash
git clone https://github.com/alostracco/Financial-Fraud-Detection.git
cd Financial-Fraud-Detection
```

#### 2. Install python dependencies
```bash
pip install -r requirements.txt
```

#### 3. Install PostgreSQL and MADlib on AWS
Follow the AWS setup guide for PostgreSQL, and install MADlib as per [Apache MADlib documentation](https://cwiki.apache.org/confluence/display/MADLIB/Installation+Guide+for+MADlib+2.X).

### Database Configuration
Load your database credentials into environment variables in a .env file in the main directory.

Next, navigate to the src/backend/utils directory and run the data ingestion script to populate your database:

```bash
python data_ingestion.py
```

## Usage

### Run Logistic Regression

Navigate to the src/backend/fraud_detection directory and run the data ingestion script to populate your database:

```bash
python Logistic_regression.py
```

### View Results

A confusion matrix will be plotted to represent the results of your logistic regression on the data.

## Key Considerations

- **Security:** Use strong passwords and secure your PostgreSQL instance.
- **Environment Variables:** Store sensitive credentials in environment variables rather than hard-coding them.
- **Scalability:** Ensure your AWS setup can handle the scale of your dataset and processing needs.
