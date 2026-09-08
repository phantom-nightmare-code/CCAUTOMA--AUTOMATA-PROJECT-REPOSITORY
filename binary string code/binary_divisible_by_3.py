# Binary Number Recognizer - Divisible by 3
# Minimized DFA: states q0, q1, q2; start q0; accept q0

def run_simulator():
    # Transition table: current_state -> (input: next_state)
    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q0'},
        'q2': {'0': 'q1', '1': 'q2'}
    }
    
    print("Binary Number Recognizer (Divisible by 3)")
    print("Enter binary strings to check. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("Enter a binary string: ").strip()
        if user_input.lower() == 'exit':
            break
        
        # Validate alphabet
        if not all(c in '01' for c in user_input):
            print("REJECTED - Invalid character (only 0 and 1 allowed)\n")
            continue
        
        current_state = 'q0'
        print(f"Processing: {user_input}")
        print("Step   Symbol   New State")
        for idx, symbol in enumerate(user_input, start=1):
            current_state = transitions[current_state][symbol]
            print(f"{idx:>4}   {symbol}       {current_state}")
        
        if current_state == 'q0':
            print("Result: ACCEPTED (divisible by 3)\n")
        else:
            print("Result: REJECTED (not divisible by 3)\n")

if __name__ == "__main__":
    run_simulator()