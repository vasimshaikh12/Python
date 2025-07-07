
"""
====================================================================
2) Task : Social Media Interaction Analysis

Analyze social media posts and interactions to find top influencers and engagement trends.


posts = [
    {"user": "alice", "likes": 120, "comments": 12, "shares": 8, "topic": "tech"},
    {"user": "bob", "likes": 200, "comments": 22, "shares": 14, "topic": "travel"},
    {"user": "alice", "likes": 90, "comments": 10, "shares": 5, "topic": "tech"},
    {"user": "diana", "likes": 300, "comments": 40, "shares": 25, "topic": "health"},
    {"user": "bob", "likes": 100, "comments": 12, "shares": 7, "topic": "travel"},
]

Calculate total engagement per user (likes + comments + shares).
Identify the top influencer (highest average engagement per post).
Calculate topic-wise engagement.
Find the most engaging topic.
"""

posts = [
    {"user": "alice", "likes": 120, "comments": 12, "shares": 8, "topic": "tech"},
    {"user": "bob", "likes": 200, "comments": 22, "shares": 14, "topic": "travel"},
    {"user": "alice", "likes": 90, "comments": 10, "shares": 5, "topic": "tech"},
    {"user": "diana", "likes": 300, "comments": 40, "shares": 25, "topic": "health"},
    {"user": "bob", "likes": 100, "comments": 12, "shares": 7, "topic": "travel"},
]

engagement_per_user ={}
for post in posts:
    user=post["user"]
    likes=post["likes"]
    comments=post["comments"]
    shares=post["shares"]
    topic=post["topic"]
    engagement=likes+comments+shares

    if user not in engagement_per_user:
        engagement_per_user[user] =0
        engagement_per_user[user] += engagement

print("total engagement per user:")
for user,engagement in engagement_per_user.items():
    print(f"{user}:{engagement}")

post_count_per_user={}
for post in posts:
    user=post["user"]
    if user not in post_count_per_user:
        post_count_per_user[user] =1
    else:
        post_count_per_user[user] += 1
print(post_count_per_user)
avg_engagement_per_user={}
for user in engagement_per_user:
    total = engagement_per_user[user]
    count = post_count_per_user[user]
    avg = total/count
    avg_engagement_per_user[user]=avg
print(avg_engagement_per_user)

engaging_topic={}
for topic in posts:
    topic=post["topic"]
    likes=post["likes"]
    comments=post["comments"]
    shares=post["shares"]
    engagement=likes+comments+shares

    if topic not in engaging_topic:
        engaging_topic[topic] = engagement
    else:
        engaging_topic[topic] += engagement
print(engaging_topic)

max_engagement=0
most_engaging_topic=""
for topic,engagement in engaging_topic.items():
    if engagement> max_engagement:
        max_engagement = engagement
        most_engaging_topic= topic

print(f"the most engaging topic is {most_engaging_topic} with total enagement of {max_engagement}")