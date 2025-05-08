import argparse
from decimal import getcontext

from prompt_toolkit import PromptSession

from input_decoder import process_and_calc

ctrl_c_counter = 0

if __name__ == '__main__':
    session = PromptSession('$ > ')
    parser = argparse.ArgumentParser(description="input parameters")
    parser.add_argument('-p', '--precision', type=int, default=30, help='The precision of Decimal')
    args = parser.parse_args()
    getcontext().prec = int(args.precision)
    print("An high-precision command-line calculator. Please enter a mathematical expression. Press ctrl+c twice to exit.")
    while True:
        try:
            user_input = session.prompt()
            if user_input.lower() == 'exit':
                break
            resu = process_and_calc(user_input)
            print(resu)
        except KeyboardInterrupt:
            if ctrl_c_counter < 1:
                ctrl_c_counter += 1
                continue
            break
        except Exception as e:
            print("Error!", e)

    print("exit")
