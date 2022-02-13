from hwfunctions import fun_factor, fun_inc
from dask import delayed

def delayed_increment(c, start, end):
    # use fun_inc
    return sum([delayed(fun_inc)(i) for i in range(start, end)])


def delayed_factor(c, start, end):
    # use fun_factor
    return sum([delayed(fun_factor)(i) for i in range(start, end)])


def future_increment(c, start, end):
    # use fun_inc
    inc_result = []
    for i in range(start, end):
        future = c.submit(fun_inc, i)
        inc_result.append(future)
    return c.submit(sum, inc_result)


def future_factor(c, start, end):
    # use fun_factor
    fact_result = []
    for i in range(start, end):
        future = c.submit(fun_factor, i)
        fact_result.append(future)
    return c.submit(sum, fact_result)
