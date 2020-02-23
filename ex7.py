import tweepy

def count_words_tweets(username):
    consumer_key = "QQ1iQEa4AMa4iR9U5yQLvoanG"
    consumer_secret = "AEP9u0aEhHLvrLpGgJGpS9yzJkhykKc8JU7VQgqTA6ZJeb9Pca"
    access_token = "803644562317148160-Z9656M40OVVx282YcQv5IvFW8alCa3T"
    access_secret = "7MZjCSdiz0ZcxIh7ztcDYSP3EAA7G2YcnbuisRtldd5Rp"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    number_of_words = 0
    try:
        for tweet in api.user_timeline(username, count=50):
            number_of_words = number_of_words + len(tweet.text.split())

    except exception as sth:
        print("fail",str(sth))
        return 0

    return number_of_words

while 1:
    user1 = input("please type a tweeter user: ")
    number_of_words1 = count_words_tweets(user1)
    if number_of_words1 != 0:
        user2 = input("please insert another user: ")
        number_of_words2 = count_words_tweets(username)
        if number_of_words2 != 0:
            if number_of_words1 > number_of_words2:
                print(user1,"has more words in his tweets than",user2)
            elif number_of_words2 > number_of_words1:
                print(user2,"has more words in his tweets than",user1)
            else:
                print(" they have the same number of words on their tweets")
        else:
            print("please insert a  correct username: ")
    else:
        print("please try with another username: ")
        



