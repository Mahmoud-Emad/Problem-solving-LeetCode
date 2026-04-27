class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid_row = False
        is_valid_column = False
        is_valid_boxes = False
        is_valid_board = False

        