document.addEventListener('DOMContentLoaded', () => {
    const display = document.getElementById('display');
    const buttons = document.querySelectorAll('.buttons button');

    let currentInput = '0';
    let previousInput = '';
    let operator = null;
    let waitingForSecondOperand = false;
    let justCalculated = false; // Flag to know if the last action was '='

    function updateDisplay() {
        display.value = currentInput;
    }

    function clearAll() {
        currentInput = '0';
        previousInput = '';
        operator = null;
        waitingForSecondOperand = false;
        justCalculated = false;
        updateDisplay();
    }

    function clearEntry() {
        if (waitingForSecondOperand) { // If CE is hit after an operator
            currentInput = '0'; // Clear the new operand entry
            // previousInput and operator remain
        } else { // CE is hit while entering the first operand or after '='
            currentInput = '0';
            previousInput = '';
            operator = null;
        }
        justCalculated = false;
        updateDisplay();
    }

    function deleteLast() {
        if (justCalculated || currentInput === 'Error') return; // Don't delete if result or error is shown
        if (currentInput.length > 1) {
            currentInput = currentInput.slice(0, -1);
        } else {
            currentInput = '0';
        }
        updateDisplay();
    }

    function appendNumber(number) {
        if (justCalculated) {
            currentInput = number;
            justCalculated = false;
        } else if (currentInput === '0' && number !== '.') {
            currentInput = number;
        } else if (number === '.' && currentInput.includes('.')) {
            return; // Avoid multiple decimal points
        } else {
            currentInput += number;
        }
        waitingForSecondOperand = false; // Allow operator input after number
        updateDisplay();
    }

    function chooseOperator(nextOperator) {
        if (operator && !waitingForSecondOperand && !justCalculated) {
            calculate(); // Calculate existing operation before starting new one
        }
        previousInput = currentInput;
        operator = nextOperator;
        waitingForSecondOperand = true;
        justCalculated = false;
        currentInput = '0'; // Ready for the next input, or show previousInput
        // Display might show previousInput until next number is typed
        // For simplicity, we can just clear currentInput for the next number
        // or show previousInput in the display. Let's show previousInput.
        display.value = previousInput;
    }

    function calculate() {
        if (operator === null || waitingForSecondOperand) {
            // If '=' is pressed without an operator or second operand not ready
            // (e.g. 5 * =) then use currentInput as second operand if operator exists
            if (operator && previousInput && currentInput) {
                 //Allow 5 * = (implies 5*5)
            } else {
                return;
            }
        }

        let result;
        const prev = parseFloat(previousInput);
        const current = parseFloat(currentInput);

        if (isNaN(prev) || isNaN(current)) {
            currentInput = 'Error: Invalid Input';
            operator = null;
            updateDisplay();
            return;
        }

        switch (operator) {
            case 'add': result = prev + current; break;
            case 'subtract': result = prev - current; break;
            case 'multiply': result = prev * current; break;
            case 'divide':
                if (current === 0) {
                    currentInput = 'Error: Div by Zero';
                    operator = null;
                    updateDisplay();
                    return;
                }
                result = prev / current;
                break;
            case 'power': result = Math.pow(prev, current); break;
            default: return; // Should not happen
        }
        currentInput = String(result);
        operator = null;
        waitingForSecondOperand = false;
        justCalculated = true;
        updateDisplay();
    }

    function handleScientific(operation) {
        const val = parseFloat(currentInput);
        if (isNaN(val) && operation !== 'pi') { // PI can be inserted into non-numeric
            currentInput = 'Error: Invalid Input';
            updateDisplay();
            return;
        }
        let result;
        try {
            switch (operation) {
                case 'sqrt':
                    if (val < 0) throw new Error("Sqrt of negative");
                    result = Math.sqrt(val);
                    break;
                case 'log': // Base 10
                    if (val <= 0) throw new Error("Log of non-positive");
                    result = Math.log10(val);
                    break;
                case 'ln':
                    if (val <= 0) throw new Error("Ln of non-positive");
                    result = Math.log(val);
                    break;
                case 'sin': result = Math.sin(val * Math.PI / 180); break; // Degrees to Radians
                case 'cos': result = Math.cos(val * Math.PI / 180); break; // Degrees to Radians
                case 'tan':
                    if (Math.abs(val % 180) === 90) { // e.g. 90, 270
                         // Represent "infinity" with a very large number or specific error
                        const cosVal = Math.cos(val * Math.PI / 180);
                        if (Math.abs(cosVal) < 1e-12) { // Check if cos is effectively zero
                             currentInput = 'Error: Tan undefined';
                             updateDisplay();
                             return;
                        }
                    }
                    result = Math.tan(val * Math.PI / 180);
                    break;
                case 'pi':
                    currentInput = String(Math.PI);
                    break;
                default: return;
            }
            if (result !== undefined) currentInput = String(result);
        } catch (e) {
            currentInput = e.message.startsWith("Error:") ? e.message : `Error: ${e.message}`;
        }
        justCalculated = true; // Treat scientific op as a calculation
        updateDisplay();
    }

    function toggleSign() {
        if (currentInput === 'Error' || justCalculated) return;
        if (currentInput !== '0') {
            currentInput = String(parseFloat(currentInput) * -1);
        }
        updateDisplay();
    }


    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const action = button.dataset.action;
            const num = button.dataset.num;
            const op = button.dataset.op;

            if (num) {
                appendNumber(num);
            } else if (op) {
                if (op === 'sqrt' || op === 'log' || op === 'ln' || op === 'sin' || op === 'cos' || op === 'tan' || op === 'pi') {
                    // If it's a unary scientific operation that should apply immediately
                    // or if an operator is pending for a binary operation like power
                    if (operator && op === 'power' && previousInput !== '') {
                         // This is a binary operator, not unary. ChooseOperator handles it.
                         chooseOperator(op);
                    } else if (op === 'power' && !operator) { // Starting with power, e.g. 2 ^
                        chooseOperator(op);
                    }
                    else {
                         handleScientific(op);
                    }
                } else { // Binary operators: +, -, *, /, power
                    chooseOperator(op);
                }
            } else if (action) {
                switch (action) {
                    case 'equals': calculate(); break;
                    case 'clear': clearAll(); break;
                    case 'clear-entry': clearEntry(); break;
                    case 'backspace': deleteLast(); break;
                    case 'negate': toggleSign(); break;
                }
            }
        });
    });

    clearAll(); // Initialize display
});
