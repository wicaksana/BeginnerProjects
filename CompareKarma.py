import requests
import json

__author__ = 'arif'

# https://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/


def compare_karma(user1, user2):
    if user_karma[user1]['karma'] > user_karma[user2]['karma']:
        print('\n{} has more karma than {}. The difference is {}'
              .format(user1, user2, user_karma[user1]['karma'] - user_karma[user2]['karma']))
    else:
        print('\n{} has more karma than {}. The difference is {}'
              .format(user2, user1, user_karma[user2]['karma'] - user_karma[user1]['karma']))


def get_data(user1, user2):
    user_karma[user1] = {'karma':0, 'upvote':0, 'downvote':0}
    user_karma[user2] = {'karma':0, 'upvote':0, 'downvote':0}

    reddit_user_link = "https://www.reddit.com/user/"

    for user in user_karma:
        url = reddit_user_link + user + '.json'
        karmaUrl = reddit_user_link + user + '/about.json';
        response1 = requests.get(url=url, headers=headers)
        response2 = requests.get(url=karmaUrl, headers=headers)

        if response1.status_code == 200: #user exists
            data1 = json.loads(response1.text)
            data2 = json.loads(response2.text)

            for child in data1['data']['children']: #get recent upvotes and downvotes
                user_karma[user]['upvote'] = user_karma[user]['upvote'] + child['data']['ups']
                user_karma[user]['downvote'] = user_karma[user]['downvote'] + child['data']['downs']

            user_karma[user]['karma'] = user_karma[user]['karma'] + data2['data']['comment_karma']

            print('Recently, {} has {} karma, {} upvotes, and {} downvotes'
                  .format(user, user_karma[user]['karma'], user_karma[user]['upvote'], user_karma[user]['downvote']))

        else:
            print('either username is not found, or something unusual happens (return code: {})'
                  .format(response1.status_code))


def main():
    while True:
        print('\n')
        user1 = input('Enter user1: ')
        user2 = input('Enter user2: ')
        print('\n')
        get_data(user1, user2)
        compare_karma(user1, user2)


if __name__ == "__main__":
    user_karma = {}
    headers = { 'User-Agent': 'Super-awesome python bot' }
    main()