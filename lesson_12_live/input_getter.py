def input_getter(times: int, prompt='Input ? ', convert_to_int=False):
    inputs = []
    for time in range(times):
        if convert_to_int:
            inputs.append(int(input(prompt)))
        else:
            inputs.append(input(prompt))
    return inputs


gathered_inputs = input_getter(3, "Name: ")
print(gathered_inputs)
