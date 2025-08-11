class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        
        # 헬퍼 함수를 exist 함수 안에 정의합니다.
        def dfs(r, c, index):
            # 1. 성공 조건: 단어를 모두 찾았을 때
            if index == len(word):
                return True

            # 2. 실패 조건 (가지치기):
            # 그리드 범위를 벗어나거나
            # 현재 칸의 문자가 word의 해당 문자와 다르거나
            # 이미 방문한 칸일 때 (방문 표시는 '#'로 함)
            if not (0 <= r < rows and 0 <= c < cols) or \
               board[r][c] != word[index]:
                return False

            # 3. 방문 표시: 현재 칸을 임시로 다른 문자로 바꿔 방문했음을 표시합니다.
            temp = board[r][c]
            board[r][c] = '#'

            # 4. 재귀 호출: 상하좌우 4방향으로 탐색을 시도합니다.
            # 하나라도 True를 반환하면 바로 True를 반환합니다.
            res = dfs(r + 1, c, index + 1) or \
                  dfs(r - 1, c, index + 1) or \
                  dfs(r, c + 1, index + 1) or \
                  dfs(r, c - 1, index + 1)

            # 5. 백트래킹: 다음 경로 탐색을 위해 원래의 문자로 되돌립니다.
            board[r][c] = temp

            return res

        # 모든 칸을 시작점으로 시도합니다.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False