def MaxAverage(matrix):
    """
    Return [col_index, max_avg] where max_avg is the largest column
    average in `matrix`, rounded to 1 decimal place.
    """
    if not matrix or not matrix[0]:              # handle empty input
        return [None, None]

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Start with column 0 as the tentative maximum
    col_sum   = sum(row[0] for row in matrix)
    max_avg   = round(col_sum / num_rows, 1)
    max_index = 0

    # Check the rest of the columns
    for j in range(1, num_cols):
        col_sum = sum(row[j] for row in matrix)
        avg     = round(col_sum / num_rows, 1)

        if avg >= max_avg:       
            max_avg   = avg
            max_index = j

    return [max_index, max_avg]


# ---- quick demo with the task’s examples ----
if __name__ == "__main__":
    ex1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ex2 = [[10, 5.5], [3.1, -2.7], [2.8, 6.4]]

    print(MaxAverage(ex1))   # ➜ [2, 6.0]
    print(MaxAverage(ex2))   # ➜ [0, 5.3