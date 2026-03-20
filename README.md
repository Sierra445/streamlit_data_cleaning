# Streamlit Data Cleaning App

A simple web application built with **Streamlit** and **Pandas** that allows users to upload an Excel file and perform basic data cleaning operations such as removing duplicate rows and handling missing values.

## Features

* Upload Excel files (`.xlsx`)
* Preview dataset (first few rows)
* Detect duplicate rows
* Remove duplicate rows interactively
* Identify and drop missing values
* Simple and user-friendly interface

## Technologies Used

* Python
* Streamlit
* Pandas
* OpenPyXL (for reading Excel files)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/streamlit-data-cleaning-app.git
cd streamlit-data-cleaning-app
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install streamlit pandas openpyxl
```

## Usage

Run the application using:

```bash
streamlit run app.py
```

Then open the provided local URL in your browser (usually `http://localhost:8501`).

## How It Works

1. Upload an Excel file using the file uploader.
2. The app displays a preview of the dataset.
3. Duplicate rows are identified and displayed.
4. Use the buttons to:

   * Remove duplicate rows
   * Drop rows with missing values
5. The cleaned dataset is displayed after each operation.

## Project Structure

```
streamlit-data-cleaning-app/
│
├── app.py
├── README.md
└── requirements.txt
```

## requirements.txt

```
streamlit
pandas
openpyxl
```

## Future Improvements

* Add option to download cleaned data
* Include data visualization (charts and graphs)
* Support additional file formats (CSV, JSON)
* Add data filtering and sorting features
* Improve UI styling and layout

