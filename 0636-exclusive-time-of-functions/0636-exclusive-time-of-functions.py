class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            parts = log.split(':') # log is 0:start:0
            id, type, time = int(parts[0]), parts[1], int(parts[2]) # id is 0, type is start, time is 0

            if type == 'start':
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(id)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result
                