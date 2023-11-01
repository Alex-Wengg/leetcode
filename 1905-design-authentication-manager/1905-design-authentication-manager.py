class AuthenticationManager:

    def __init__(self, timeToLive: int):
        
        self.hash_ = {} # tokenId to index
        self.curr_time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hash_[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime-self.curr_time        # calculate limit time to filter unexpired tokens
        if tokenId in self.hash_ and self.hash_[tokenId]>limit:    # filter tokens and renew its time
            self.hash_[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime-self.curr_time       # calculate limit time to filter unexpired tokens
        c = 0
        for i in self.hash_:
            if self.hash_[i]>limit:         # count unexpired tokens
                c+=1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)