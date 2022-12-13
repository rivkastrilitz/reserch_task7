import timeit

import cvxpy as cp
import numpy as np
import time
import matplotlib.pyplot as plt
import random


def generate_linear_equations(k):
    coefficients = [*range(-10, 0), *range(1, 11)]
    rng = np.random.default_rng()
    return rng.choice(coefficients, size=(k, k)), rng.integers(-10, 11, k)


# def solusion_cp(coeffs, variables):

def plot(k_range,run_time,title):
    plt.plot(k_range, run_time)
    # naming the x
    plt.xlabel('size of equation')
    # naming the y
    plt.ylabel('run time (ms)')

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    plt.show()

def print_np_solution(coeffs, variables,k):
    symbols = 'abcdefghijklmnop'[:k]
    solution = coeffs.dot(variables)
    for row, sol in zip(coefficients, solution):
        # lhe = left-hand side of equation
        lhs = ' '.join(f'{r:+}{s}' for r, s in zip(row, symbols)).lstrip('+')
        print(f'{lhs} = {sol}')
    print()
    for s, v in zip(symbols, variables):
        print(f'{s} = {v}')


#הבנתי שאני צריכה להכניס לאילוצים את המשוואות הלינאריות
# ושאם אכניס משתנה כפול מקדם ותוצאה זה יצור לי את המשוואות אבל לא הצלחתי לגרום לזה לעבוד וקצת התבחבשתי ולצערי נגמר הזמן - אבל סך הכל השאלה הייתה מעניינת

# def print_cvxpy_solution(k):
#     symbols = 'abcdefghijklmnop'[:k]
#     m = 20
#     n = 10
#     np.random.randn(m,n)
#     b = cp.Parameter(m)
#     coeffs = cp.Variable(n)
#     solution =[]
#     for i in range(6):
#         coeffs[i] = random.randint(1,8)
#
#
#     for i in range(5):
#         constrains.append((b[i]*coeffs[i]))
#
#     obj = cp.Maximize(0)
#     prob = cp.Problem(obj, constrains)
#     prob.solve()

if __name__ == '__main__':

    np_times=[]
    cvx_times=[]
    ## numpy solution
    for k in range(2,15):
        coefficients, variables = generate_linear_equations(k)
        start = timeit.default_timer()
        np_solu = print_np_solution(coefficients, variables,k)
        stop = timeit.default_timer()
        np_time = (stop - start)*10000
        print(np_time)
        np_times.append(np_time)
        # print ("np solutions")
        # print_solution(np_solu, variables)
    ## cvxpy solution
    # for k in range(1, 15):
    #     coefficients, variables = generate_linear_equations(k)
    #     start = timeit.default_timer()
    #     cvxpy_solu = print_cvxpy_solution(coefficients, variables)
    #     stop = timeit.default_timer()
    #     cvxpy_time = (stop - start) * 10000
    #     print(np_time)
    #     cvx_times.append(cvxpy_time)
    #     print("cvxpy solutions")




    # plot run time as an equation of k-(size of linear equation)
    plot(range(2,15),np_times,"numpy Graph")

    # plot(range(1, 15), cvx_times, "cvxpy Graph")






