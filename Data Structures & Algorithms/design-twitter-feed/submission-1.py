class Twitter:

    def __init__(self):
        self.feed = []
        self.following = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if not self.feed:
            return []
        res = []
        index = len(self.feed) - 1
        while len(res) < 10:
            post = self.feed[index]
            if post[0] in self.following[userId] or post[0] == userId:
                res.append(post[1])
            index -= 1
            if index < 0:
                return res
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
