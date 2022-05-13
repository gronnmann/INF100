def add_together_safely(a, b, c, d):
    try:
        return a + b + c + d

    except Exception as e:
        print(f"Failed with error: {e}")
        return None
