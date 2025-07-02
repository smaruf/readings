def process_until_no_A(arr, counterStep):
    iteration = 0
    while 'A' in arr:
        iteration += 1
        print(f"\nIteration {iteration} - Start: {arr}")

        # Step 1: Remove up to counterStep 'P's from the end
        p_removed = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 'P':
                arr.pop(i)
                p_removed += 1
                if p_removed == counterStep:
                    break

        # Step 2: Remove up to counterStep 'A's from the end
        a_removed = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 'A':
                arr.pop(i)
                a_removed += 1
                if a_removed == counterStep:
                    break

        # Step 3: Add 'A's at the beginning equal to number of P's removed
        arr = ['A'] * p_removed + arr

        print(f"Removed {p_removed} 'P'(s), {a_removed} 'A'(s), Added {p_removed} 'A'(s) at start.")
        print(f"Iteration {iteration} - End: {arr}")

        # Safety check to avoid infinite loop if it's regenerating forever
        if p_removed == 0 and a_removed == 0:
            print("No changes in this iteration. Breaking to prevent infinite loop.")
            break

    print(f"\nFinal array after {iteration} iterations: {arr}")
    return arr, iteration


# Example usage
initial_array = ["A", "A", "A", "P", "P", "P"]
counter_step = 2
final_array, total_iterations = process_until_no_A(initial_array, counter_step)
