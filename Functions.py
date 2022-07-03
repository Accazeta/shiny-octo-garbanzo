def weight_builder(length, m1, q1, m2, q2):
    half = length / 2
    result = [0] * length  # builds an empty list of zeros
    for i in range(0, length):
        if i <= half:
            result[i] = m1 * (i / length) + q1  # /length is used to normalize to 1
        else:
            result[i] = m2 * (i / length) + q2
    return result
