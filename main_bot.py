import praw
import config
import time


def bot_login():
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent ="F1 reddit bot test ")

    return r


def run_bot(rLog, comments_done):
    count_vettel = 1
	count_maldonado = 1
	count_stroll = 1
    for comm in rLog.subreddit('formula1').comments(limit=100):
		comment = comm.body
		if comm.id not in comments_done and comm.author != r.user.me():
			if "vettel" in comment.lower() and "hamilton" in comment.lower() and "2017" in comment.lower:
				comm.reply("I see you talking about the 2017, Vettel will win relax http://www.hyperveloce.com/wp-content/uploads/2015/07/Vettel.jpg")
				print("Vettel = ", counter, " times")
				count_vettel += 1
			elif "maldonado" in comment.lower():
				comm.reply("Atleast I made the races interesting!") # Enter Maldonado picture here
				print("Maldonado = ", counter, " times")
				count_maldonado += 1
			elif "stroll" in comment.lower() and "crash" in comment.lower():
				comm.reply("Let's see! https://www.hasstrollcrashedyet.com/")
				print("Stroll = ", counter, " times")
				count_stroll += 1 
			comments_done.append(comm.id)
			
			with open ("comments_checked.txt", "a") as f:
				f.write(comm.id + "\n")
			
	# The bot will run every 100 seconds
    time.sleep(100)

	
def get_checked_comments():
	if not os.path.isfile("comments_checked.txt"):
		comments_done = []
	else:
		with open("comments_done.txt", "r") as f:
			comments_done = f.read()
			comments_done = comments_checked.split("\n")
			comments_done = filter(None, comments_done)

	return comments_replied_to

	
r = bot_login()
comments_done = get_checked_comments()
while True:
    run_bot(r, comments_done)

	
