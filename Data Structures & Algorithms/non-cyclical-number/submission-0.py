class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        j = n
        while True:
            sumo = sum(int(digit) ** 2 for digit in str(j))
            if sumo == 1:
                return True
            if sumo in seen:
                return False
            else:
                seen.add(sumo)
            j = sumo