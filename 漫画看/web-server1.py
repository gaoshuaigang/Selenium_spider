import openpyxl
from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/excel-data')
def get_excel_data():
    wb = openpyxl.load_workbook('People/An_people.xlsx')
    sheet = wb['Sheet']
    data = []
    for i, row in enumerate(sheet.iter_rows(values_only=True), start=1):
        if i == 1:  # 跳过第一行
            continue
        data.append(list(row))
    return data

@app.route('/debug-excel')
def debug_excel_data():
    excel_path = 'People/A_people.xlsx'
    df = pd.read_excel(excel_path)
    return df.to_html()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
