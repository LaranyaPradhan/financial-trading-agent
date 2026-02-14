def api_cost_simulation(raw_calls, compressed_calls, cost_per_call=0.01):
    raw_cost = raw_calls * cost_per_call
    compressed_cost = compressed_calls * cost_per_call
    savings = raw_cost - compressed_cost

    return {
        "Raw Cost": raw_cost,
        "Compressed Cost": compressed_cost,
        "Savings": savings
    }
