#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = a/b
    except:
        ans = None
    finally:
        print("Inside result: {}".format(ans))
        return ans
