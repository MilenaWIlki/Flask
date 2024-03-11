# Implementation of a web-based expense tracker using Flask
# Users can add expenses, categorize spending, and view summaries

from flask import Flask, request, jsonify

app = Flask(__name__)
expenses = {}

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    category = data['category']
    amount = data['amount']
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)
    return jsonify({"message": "Expense added successfully"})

@app.route('/view_summary', methods=['GET'])
def view_summary():
    summary = {}
    for category, amounts in expenses.items():
        summary[category] = sum(amounts)
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
