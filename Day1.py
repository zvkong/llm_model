## python source code
import sys
def main():
    print('hello world', sys.argv[1])

if __name__ == '__main__':
    main()

# # Defines a "repeat" function that takes 2 arguments
# def repeat(s, exclaim = True):
#     # result = s + s + s
#     result = s * 3 # this is faster since only do one time of calculation
#     if exclaim:
#         result = result + '!!!'
#     return result
dir(sys)