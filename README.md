# Simple Calculator App

This is a simple calculator built using [Streamlit](https://streamlit.io/). The calculator supports basic arithmetic operations, including addition, subtraction, multiplication, and division. The app is already deploy in [cloud](https://simplecalculatorr.streamlit.app/)

## Features

- **Responsive Layout:** The calculator is designed to be user-friendly with large buttons and an easy-to-read display.
- **Basic Operations:** Perform basic arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Error Handling:** Prevents division by zero and returns `'INF'` if attempted.
- **Clear Display:** The `AC` button clears the current input and resets the calculator.

## How to Run

1. **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/your-username/simple-calculator.git
    cd simple-calculator
    ```

2. **Install the required dependencies**:
    ```bash
    pip install streamlit
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

4. **Access the app**:
    - Open your web browser and go to `http://localhost:8501` to use the calculator.

## Custom Styling

The calculator has custom CSS applied to style the buttons and layout:
- Buttons are large and bold, with a dark background and white text.
- The display input is styled for better readability and alignment.

## Code Explanation

The core functionality is handled by the `calculate()` function, which evaluates the arithmetic expression entered by the user. The `button_click()` function manages the interaction logic, updating the display and handling different button presses.

## Example Usage

1. **Basic Operations:**
   - Enter `7 + 3` and press `=` to get `10`.
   - Enter `10 / 2` and press `=` to get `5`.

2. **Handling Errors:**
   - Attempting to divide by zero (e.g., `10 / 0`) will return `'INF'`.


## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
