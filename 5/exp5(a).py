def totalNQueens(n):
    result = 0
    columns = set()
    diag1 = set()
    diag2 = set()
    
    def backtrack(row):
        nonlocal result
        if row == n:
            result += 1
            return
        
        for col in range(n):
            if col in columns or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            columns.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1)
            
            columns.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    backtrack(0)
    return result


# Example Run
n = 4
print("Number of distinct solutions for", n, "Queens:", totalNQueens(n))