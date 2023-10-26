class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.NUMBERS = {"1","2","3","4","5","6","7","8","9"}
        seen_in_row = [set() for _ in range(9)]
        seen_in_col = [set() for _ in range(9)]
        seen_in_section = [set() for _ in range(9)]
        for row_num, row in enumerate(board):
            for col_num, num in enumerate(row):
                if num in self.NUMBERS:
                    if num not in seen_in_row[row_num]:
                        seen_in_row[row_num].add(num)
                    else:
                        return False
                    
                    if num not in seen_in_col[col_num]:
                        seen_in_col[col_num].add(num)
                    else:
                        return False
                    
                    sec_num = self.calculate_sec_num(row_num, col_num)
                    if num not in seen_in_section[sec_num]:
                        seen_in_section[sec_num].add(num)
                    else:
                        return False
        return True