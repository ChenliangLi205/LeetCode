class tweet(object):
    def __init__(self, tid, uid, time):
        self.tweetId = tid
        self.userId = uid
        self.time = time


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = dict()  # user: list[tweet]
        self.recentTweets = dict()  # user: tweetList: list[tweet]
        self.followedBy = dict()  # user: set{userId}
        self.timeCnt = 0
        self.userSet = set()

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.userSet:
            self.userSet.add(userId)
        if userId not in self.recentTweets:
            self.recentTweets[userId] = []
        if userId not in self.followedBy:
            self.followedBy[userId] = set()
            self.followedBy[userId].add(userId)

        thisTweet = tweet(tweetId, userId, self.timeCnt)

        if userId not in self.tweets:
            self.tweets[userId] = [thisTweet]
        else:
            self.tweets[userId].insert(0, thisTweet)

        for follower in self.followedBy[userId]:
            if follower not in self.recentTweets:
                self.recentTweets[follower] = []
            self.recentTweets[follower].insert(0, thisTweet)

        self.timeCnt += 1
        return

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.userSet:
            return []
        if userId not in self.recentTweets:
            return []
        else:
            if len(self.recentTweets[userId]) >= 10:
                return [t.tweetId for t in self.recentTweets[userId][:10]]
            else:
                return [t.tweetId for t in self.recentTweets[userId]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId not in self.userSet:
            self.userSet.add(followerId)
        if followeeId not in self.userSet:
            self.userSet.add(followeeId)
        if followeeId not in self.followedBy:
            self.followedBy[followeeId] = {followeeId}
        if followerId in self.followedBy[followeeId]:
            return
        self.followedBy[followeeId].add(followerId)

        if followerId not in self.tweets:
            self.tweets[followerId] = []
        if followeeId not in self.tweets:
            self.tweets[followeeId] = []

        if followerId not in self.recentTweets:
            self.recentTweets[followerId] = []
            for tweet in self.tweets[followerId]:
                self.recentTweets[followerId].insert(0, tweet)

        i, idx = 0, 0
        while i < len(self.tweets[followeeId]):
            t = self.tweets[followeeId][i]
            if idx >= len(self.recentTweets[followerId]):
                self.recentTweets[followerId].append(t)
                i += 1
            elif self.recentTweets[followerId][idx].time < t.time:
                self.recentTweets[followerId].insert(idx, t)
                i += 1
            idx += 1
        return

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId not in self.userSet or followerId not in self.userSet:
            return
        if followeeId not in self.followedBy:
            return
        if followerId not in self.followedBy[followeeId]:
            return

        self.followedBy[followeeId].remove(followerId)

        if followerId not in self.recentTweets:
            return
        i = 0
        while i < len(self.recentTweets[followerId]):
            if self.recentTweets[followerId][i].userId == followeeId:
                self.recentTweets[followerId].pop(i)
            else:
                i += 1
        return

        # Your Twitter object will be instantiated and called as such:
        # obj = Twitter()
        # obj.postTweet(userId,tweetId)
        # param_2 = obj.getNewsFeed(userId)
        # obj.follow(followerId,followeeId)
        # obj.unfollow(followerId,followeeId)