def fibonacci(n):
    """Generate a Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    n_terms = 10
    print(f"Fibonacci sequence (first {n_terms} terms):")
    print(fibonacci(n_terms))
