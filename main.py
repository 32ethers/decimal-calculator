import argparse
from decimal import getcontext

from prompt_toolkit import PromptSession

from input_decoder import process_and_calc

if __name__ == '__main__':
    session = PromptSession('$ > ')
    parser = argparse.ArgumentParser(description="imput parameters")
    parser.add_argument('-p', '--precision', type=int, default=100, help='The precision of Decimal')
    args = parser.parse_args()
    getcontext().prec = int(args.precision)
    print("An high-precision command-line calculator. Please enter a mathematical expression.")
    while True:
        try:
            user_input = session.prompt()
            if user_input.lower() == 'exit':
                break
            resu = process_and_calc(user_input)
            print(resu)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("Error!", e)

    print("exit")
