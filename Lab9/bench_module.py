def praw_reddit(nombre_subreddit="chile", n_hot=1000):
    reddit = praw.Reddit(
        client_id="-w2hyFINxZ8T3g",
        client_secret="zGPCI4s3g6Ic6AsRi7vIpP0NoxbFdw",
        password="ClasesMDS7202",
        user_agent="Clases",
        username="DocenciaDataScience",
        check_for_async=False,
    )
    subreddit = reddit.subreddit(nombre_subreddit)

    votes, post, url = {}, {}, {} #3 diccionarios. votos, posts y urls
    top_submissions = list(subreddit.hot(limit=n_hot)) # se almacenan las submissions según el límite dado
    for it, top_n in enumerate(range(50, len(top_submissions), 50)): #it: contador| top_n: 50
        top_n_submissions = top_submissions[:top_n] #revisa las 50, 100, 150, 200, 250...
        upvotes, downvotes, url[it], post[it] = [], [], [], []

        for submission in top_n_submissions: #se revisa cada submission del filtro hecho
            try:
                ratio = submission.upvote_ratio #parámetro de la submission
                ups = int(
                    round((ratio * submission.score) / (2 * ratio - 1))
                    if ratio != 0.5 #si ratio!= 0.5 se aplica la fó
                    else round(submission.score / 2) #en caso contrario se redondea la división de 2
                )
                upvotes.append(ups) #se añade el elemento ups
                downvotes.append(ups - submission.score) # se añade el elemento down
                post[it].append(submission.title) #se añade el titulo del post
                url[it].append(submission.url) #se añade la url
            except Exception as e:
                continue
        votes[it] = np.array([upvotes, downvotes]).T #se añade la tupla/lista de upvotes,downvotes a votes
    return votes, post, url 
