class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        line = []
        cnt = 0
        for i, ticket in enumerate(tickets):
            line.append([ticket, i])

        ticket_ = line[k][0]

        while ticket_:
            cnt += 1

            currTicket, i = line.pop(0)

            currTicket -= 1
            if i == k:
                ticket_ -= 1 
            if currTicket != 0:
                line.append([currTicket, i])
            if i == k and currTicket == 0:
                return cnt 
    
        return cnt 