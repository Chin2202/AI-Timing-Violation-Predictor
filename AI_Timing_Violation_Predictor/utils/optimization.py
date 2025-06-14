def suggest_optimal_frequency(max_path_delay, target_slack=0.0):
    required_time_ns = max_path_delay + abs(target_slack)
    optimal_frequency = 1 / (required_time_ns * 1e-9) * 1e-6  # MHz
    return round(optimal_frequency, 2)
