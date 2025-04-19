import numpy as np

def calculate_entropy_change(u_min_mv, u_max_mv):
    entropy_mv = np.log2(u_max_mv - u_min_mv)
    entropy_uv = np.log2((u_max_mv - u_min_mv) * 1000)
    return entropy_mv, entropy_uv

def calculate_average_information_speed(samples_count, message_duration, differential_entropy, conditional_entropy):
    return (differential_entropy - conditional_entropy) * (samples_count / message_duration)
