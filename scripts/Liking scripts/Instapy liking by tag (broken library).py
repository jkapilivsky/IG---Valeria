"""Example Case of the Script"""
from instapy import InstaPy

while True:
    session = InstaPy(username='linethmm', password='I1232123you')

    try:
        # if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment

        """Logging in"""
        # logs you in with the specified username and password
        session.login()

        # like X random posts of each given username
        # session.like_by_users(usernames=['sherlockchang'], amount=1, random=False)

        # Like X number of posts on main feed
        # session.like_by_feed(amount=50)

        # Sets to only look for images with likes between 25 and 500
        session.set_lower_follower_count(limit=30)
        session.set_upper_follower_count(limit=8000)

        # TODO - Automate this list
        session.like_by_tags(['#follow', '#photooftheday', '#happy'
                              '#beautiful', '#dogs', '#cats', '#instadaily', '#Adobe', 'watercolors', '#smile',
                              '#nofilter', '#instadaily', '#instagood', '#cute'], amount=30)

        # session.like_by_tags([ '#artdirector', '#advertising', '#illustration', '#animation',
        #                       '#illustrations', '#animations', '#photoshop', '#photography', '#DSLR',
        #                       '#BOKEH','#stopmotion', '#vectorart', '#illustrator', '#Adobe',
        #                       '#drawing', '#painting', '#digitalpainting','#watercolors',
        #                       '#cats', '#creative', '#dogs', '#circlelens', '#cosplay', '#art'], amount=40)

        # session.like_by_tags(['#smile',
        #                       '#instadaily', '#igers'', #illustration', '#animation',
        #                       '#illustrations', '#animations', '#photoshop', '#photography', '#instagood', '#cute',
        #                       '#follow', '#photooftheday', '#happy', '#beautiful'], amount=25)

        """Ending the script"""
        # clears all the cookies, deleting you password and all information from this session
        session.end()

    except:
        session.end()
        pass
