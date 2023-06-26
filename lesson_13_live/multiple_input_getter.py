DEFAULT_INPUTS = (
    'NAME',
    'AGE', 'OCCUPATION'
)

DEFAULT_TIMES = 5


def multiple_input_getter(prompts: list, times: int):
    result_list = []
    for i in range(times):
        result = dict()
        for prompt in prompts:
            result[prompt] = input(prompt)
        result_list.append(result)
    return result_list
