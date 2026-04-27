class Twitter:

    # Solution 1: LIFO stack for feed and dictionary for following
    def __init__(self):
        self.feed = []
        self.following = defaultdict(list)

    # Add post to feed stack
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append((userId, tweetId))

    # Get 10 most recent and valid (userId is following or posted) posts
    def getNewsFeed(self, userId: int) -> List[int]:
        if not self.feed:
            return []
        res = []
        index = len(self.feed) - 1
        # Max of 10 output to feed
        while len(res) < 10:
            # Get post info
            post = self.feed[index]
            # If following poster or are the poster, add to result
            if post[0] in self.following[userId] or post[0] == userId:
                res.append(post[1])
            # Move to next most recent post
            index -= 1
            # Return if no more posts
            if index < 0:
                return res
        return res

    # Add following if not already
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    # Remove follow if already following
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
