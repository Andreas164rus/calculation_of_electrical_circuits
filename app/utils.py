PREFIXES_MORE_1 = {
    1e+6: 'Meg',
    1e+3: 'k',
}

PREFIXES_LESS_1 = {
    1e-3: 'm',
    1e-6: "u",
}


def prefix_converter(value):
    for prefix in PREFIXES_MORE_1:
        if value/prefix >= 1:
            return f"{value/prefix:.3f}{PREFIXES_MORE_1[prefix]}"
    for prefix in PREFIXES_LESS_1:
        if value/prefix >= 1 and value < 1:
            return f"{value/prefix:.3f}{PREFIXES_LESS_1[prefix]}"
    return f"{value:.3f}"
