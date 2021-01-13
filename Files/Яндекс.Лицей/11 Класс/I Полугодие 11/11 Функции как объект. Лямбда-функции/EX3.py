def simple_map(transformation, values):
    x = []
    for i in values:
        x.append(transformation(i))
    return x
