import readline
import esolang.level0_arithmetic
import esolang.level1_statements
import esolang.level2_loops
import esolang.level3_functions


def run_repl(lang):
    parser = lang.parser
    interpreter = lang.Interpreter()
    while True:
        try:
            cmd = input('esolang> ')
            tree = parser.parse(cmd)
            result = interpreter.visit(tree)
            if result is not None:
                print(result)
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Run the esolang REPL.")
    parser.add_argument('--level', default=3, type=int, help='Choose esolang level (0-3)')
    args = parser.parse_args()

    level_modules = {
        0: esolang.level0_arithmetic,
        1: esolang.level1_statements,
        2: esolang.level2_loops,
        3: esolang.level3_functions
    }

    lang = level_modules.get(args.level)
    if lang is None:
        print(f"Error: Unsupported level {args.level}. Please choose a level between 0 and 3.")
    else:
        run_repl(lang)

