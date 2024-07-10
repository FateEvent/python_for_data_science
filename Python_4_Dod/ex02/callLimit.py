def callLimit(limit: int):
    """The callLimit() function takes as argument a call \
limit of another function and blocks its execution above \
the limit."""

    count = 0

    def callLimiter(function):
        """The callLimiter() function takes as argument a \
function and calls limit_function() that returns it."""

        def limit_function(*args: any, **kwds: any):
            """The limit_function() calls the function \
passed as argument to callLimiter() if and only if the \
call limit has not been exceeded."""

            nonlocal count

            count += 1
            if count <= limit:
                try:
                    function()
                except Exception as error:
                    print(f'{type(error).__name__}: {error}')
                    return

            else:
                print(f'Error: <function { function.__name__ } \
at { hex(id(function)) }> \
called too many times')

        return limit_function

    return callLimiter
