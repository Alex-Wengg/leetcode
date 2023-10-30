class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles = numBottles

        while numBottles > 1 and numBottles >= numExchange:
            bottles += numBottles // numExchange
            numBottles = numBottles // numExchange + numBottles % numExchange
        
        return bottles