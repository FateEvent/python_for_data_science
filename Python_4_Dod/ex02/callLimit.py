def callLimit(limit: int):
    """The callLimit() function takes as argument a call \
limit of another function and blocks its execution above \
the limit"""

    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):

            nonlocal count

            count += 1
            if count <= limit:
                function()
            else:
                print(f'Error: <function { function.__name__ } \
at { hex(id(function)) }> \
called too many times')

        return limit_function

    return callLimiter
