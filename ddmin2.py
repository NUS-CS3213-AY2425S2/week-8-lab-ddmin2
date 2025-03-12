def test(s):
    return "error" in s

def ddmin2(test_case, n=2):
    """
    Implementation of the ddmin2 algorithm as described by Andreas Zeller.
    
    Args:
        test_case (str): The string to minimize
        n (int): number of deltas
        
    
    Returns:
        str: A minimal test case that still causes test to fail
    """
    
    # TODO
    pass    


def compute_deltas(test_case, n):
    """
    Split the test case into n chunks of approximately equal size.
    
    Args:
        test_case (str): The test case to split
        n (int): Number of chunks to split the test case into
    
    Returns:
        list: List of substrings (deltas) from the test case
    """
    if n > len(test_case):
        n = len(test_case)
    
    # Calculate chunk size
    chunk_size = len(test_case) // n
    remainder = len(test_case) % n
    
    deltas = []
    pos = 0
    
    for i in range(n):
        # Distribute remainder across the first 'remainder' chunks
        size = chunk_size + (1 if i < remainder else 0)
        deltas.append(test_case[pos:pos + size])
        pos += size
    
    return deltas


def compute_complements(deltas):
    """
    Compute the complements
    
    Args:
        deltas (list): List of deltas (chunks) from the test case
    
    Returns:
        list: a list of complements, each with one delta removed
    """
    result = []
    for i in range(len(deltas)):
        result.append(''.join(deltas[:i] + deltas[i+1:]))
    return result


# Example usage:
if __name__ == "__main__":
    
    # Example test case
    original_case = "This string contains an error message that we want to minimize."
    
    # Find minimal failing test case
    minimal_case = ddmin2(original_case)
    
    print(f"Original test case ({len(original_case)} chars): {original_case}")
    print(f"Minimal test case ({len(minimal_case)} chars): {minimal_case}")
    
    # Example test case
    original_case = "This string is yet another message that we want to minimize for an error"
    
    # Find minimal failing test case
    minimal_case = ddmin2(original_case)
    
    print(f"Original test case ({len(original_case)} chars): {original_case}")
    print(f"Minimal test case ({len(minimal_case)} chars): {minimal_case}")
