from flask import Flask, render_template, request, jsonify
import numpy as np
from matrix_operations import matrix_multiply, matrix_multiply_multithreaded_row, matrix_multiply_multithreaded_cell, compare_performance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()  # Retrieve JSON data from the request
    matrix_A = data['matrix_A']
    matrix_B = data['matrix_B']
    operation = data['operation']

    # Convert lists to numpy arrays
    try:
        A = np.array(matrix_A)
        B = np.array(matrix_B)
    except ValueError as e:
        return jsonify({"error": "Invalid matrix format."}), 400

    if A.shape[1] != B.shape[0]:
        return jsonify({"error": "Matrices cannot be multiplied. Check dimensions."}), 400

    # Choose operation based on user input
    if operation == 'standard':
        result = matrix_multiply(A, B)
    elif operation == 'row_thread':
        result = matrix_multiply_multithreaded_row(A, B)
    elif operation == 'cell_thread':
        result = matrix_multiply_multithreaded_cell(A, B)

    return jsonify(result=result.tolist())

@app.route('/compare', methods=['POST'])
def compare():
    matrix_A = request.json['matrix_A']
    matrix_B = request.json['matrix_B']

    A = np.array(matrix_A)
    B = np.array(matrix_B)

    performance = compare_performance(A, B)
    return jsonify(performance=performance)

if __name__ == '__main__':
    app.run(debug=True)
