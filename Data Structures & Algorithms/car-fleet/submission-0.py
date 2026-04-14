class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        max_time = 0
        fleet = 0

        for i in range(len(position)):
            stack.append([position[i], speed[i]])
        
        newStack = sorted(stack, reverse = True)

        for car in newStack:
            distance = target - car[0]
            time = distance/car[1]

            if time > max_time:
                fleet += 1
                max_time = time

        return fleet