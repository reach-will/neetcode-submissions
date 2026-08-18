class Twitter:

    def __init__(self):
        self.subscribed_to = defaultdict(set)
        self.post_order = 0
        self.user_posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((self.post_order, tweetId))
        self.post_order += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        priority_queue = []
        for followeeId in (self.subscribed_to[userId] | {userId}):
            for post in reversed(self.user_posts[followeeId]):
                if len(priority_queue) < 10:
                    heapq.heappush(priority_queue, post)
                else:
                    if priority_queue[0] >= post:
                        break
                    heapq.heappushpop(priority_queue, post)
        return [tweetId for _, tweetId in sorted(priority_queue, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscribed_to[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.subscribed_to[followerId]:
            self.subscribed_to[followerId].remove(followeeId)
