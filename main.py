from csv import reader
import csv

#input an array of genres and returns array of all movie_ids that correspond to the genre types
def genre_search(input_genres):

    moviesFile='tmdb_5000_movies.csv'
    id_array=[]

    with open(moviesFile,'r',encoding="utf8") as read_obj:
        csv_reader=reader(read_obj)

        #skips the first line in the csv files cause those are headings
        iterReader = iter(csv_reader)
        next(iterReader)

        for row in iterReader:
            budget,genres,homepage,id,keywords,original_language,original_title,overview,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,vote_average,vote_count=row

            for each_genre in input_genres:
                if (each_genre in genres.casefold()):
                    id_array.append(id)

    return(id_array)

#input an array of actors and returns array of all movie_ids that correspond to the actors
def actor_search(input_actors):

    moviesFile='tmdb_5000_credits.csv'
    id_array=[]

    with open(moviesFile,'r',encoding="utf8") as read_obj:
        csv_reader=reader(read_obj)

        iterReader = iter(csv_reader)
        next(iterReader)

        for row in iterReader:
            movie_id,title,cast,crew=row

            for each_actor in input_actors:
                if (each_actor in cast ):
                    id_array.append(movie_id)

    return(id_array)


#input an array of production companies and returns array of all movie_ids that correspond to those production companies
def production_company_search(input_production_comp):

    moviesFile='tmdb_5000_movies.csv'
    id_array=[]

    with open(moviesFile,'r',encoding="utf8") as read_obj:
        csv_reader=reader(read_obj)

        iterReader = iter(csv_reader)
        next(iterReader)

        for row in iterReader:
            budget,genres,homepage,id,keywords,original_language,original_title,overview,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,vote_average,vote_count=row

            for each_comp in input_production_comp:
                if (each_comp in production_companies):
                    id_array.append(id)

    return(id_array)


#input an array of production companies and returns array of all movie_ids that correspond to those production companies
def languages_search(input_languages):

    moviesFile='tmdb_5000_movies.csv'
    id_array=[]

    with open(moviesFile,'r',encoding="utf8") as read_obj:
        csv_reader=reader(read_obj)

        iterReader = iter(csv_reader)
        next(iterReader)

        for row in iterReader:
            budget,genres,homepage,id,keywords,original_language,original_title,overview,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,vote_average,vote_count=row

            for each_language in input_languages:
                if (each_language in spoken_languages):
                    id_array.append(id)

    return(id_array)

#input an decimal number of popularity and returns array of all movie_ids that are more or just as popular
def popularity_search(input_popularity):

    moviesFile='tmdb_5000_movies.csv'
    id_array=[]

    with open(moviesFile,'r',encoding="utf8") as read_obj:
        csv_reader=reader(read_obj)

        iterReader = iter(csv_reader)
        next(iterReader)

        for row in iterReader:
            budget,genres,homepage,id,keywords,original_language,original_title,overview,popularity,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,vote_average,vote_count=row
            if (float(input_popularity)<=float(popularity)):
                id_array.append(id)

    return(id_array)

#input an array of movie ids and returns an array of movie names that correspond to the movie ids
def movie_name_search(input_movie_ids):

    creditsFile='tmdb_5000_credits.csv'
    movie_name_array=[]

    with open(creditsFile,'r',encoding="utf8") as read_obj:
        csv_reader=reader(read_obj)

        iterReader = iter(csv_reader)
        next(iterReader)

        for row in iterReader:
            movie_id,title,cast,crew=row

            if (movie_id in input_movie_ids):
                movie_name_array.append(title)

    return(movie_name_array)



#main program

genre_preferences=[]
actor_preferences=[]
company_preferences=[]
language_preferences=[]
popularityf=0

genre=None
actor=None
company=None
language=None
popularity=0

print("Welcome, Enter preferences to get a movie recommendation")
print(" ")

while(genre!="!"):
    genre=input("Enter your genre preference(Enter ! to escape): ")
    if ((genre!="!") and (genre not in genre_preferences)):
        genre_preferences.append(genre)

print(" ")

while(actor!="!"):
    actor=input("Enter your actor preference(Enter ! to escape): ")
    if ((actor!="!") and (actor not in actor_preferences)):
        actor_preferences.append(actor)

print(" ")

while(company!="!"):
    company=input("Enter your production company preference(Enter ! to escape): ")
    if ((company!="!") and (company not in company_preferences)):
        company_preferences.append(company)

print(" ")

while(language!="!"):
    language=input("Enter your language preference(Enter ! to escape): ")
    if ((language!="!") and (language not in language_preferences)):
        language_preferences.append(language)

print(" ")

while(popularity!="!"):
    popularity=input("Enter your popularity preference(Enter ! to escape): ")
    if (popularity!="!"):
        popularityf=popularity

print(" ")

genre_ids=genre_search(genre_preferences)
actor_ids=actor_search(actor_preferences)
company_ids=production_company_search(company_preferences)
language_ids=languages_search(language_preferences)
popularity_ids=popularity_search(popularityf)

movie_ids=[]

with open('tmdb_5000_credits.csv', 'r', encoding='utf8') as read_obj:
    csv_reader = reader(read_obj)

    iterReader = iter(csv_reader)
    next(iterReader)

    for row in iterReader:
        movie_id, title, cast, crew = row
        movie_ids.append(movie_id)

movie_id_and_count=[]
count=0

for i in movie_ids:
    count=0
    if i in genre_ids:
        count+=1
    if i in language_ids:
        count+=1
    if i in company_ids:
        count+=1
    if i in language_ids:
        count+=1
    if i in popularity_ids:
        count+=1
    movie_id_and_count.append((i,count))


for i in range(len(movie_id_and_count)):
    # We assume that the first item of the unsorted segment is the smallest
    lowest_value_index = i
    # This loop iterates over the unsorted items
    for j in range(i + 1, len(movie_id_and_count)):
        if movie_id_and_count[j][1] < movie_id_and_count[lowest_value_index][1]:
            lowest_value_index = j
    # Swap values of the lowest unsorted element with the first unsorted
    # element
    movie_id_and_count[i], movie_id_and_count[lowest_value_index] = movie_id_and_count[lowest_value_index], movie_id_and_count[i]

final_movie_ids=[]

movie_id_and_count_length=len(movie_id_and_count)

for i in range(1,6):
    final_movie_ids.append(movie_id_and_count[movie_id_and_count_length-1][0])
    movie_id_and_count_length=movie_id_and_count_length-1

print("Your recommendations are: ")
print(movie_name_search(final_movie_ids))

with open('fish-output.csv','w',newline='') as write_obj:
    csv_writer=csv.writer(write_obj)
    csv_writer.writerow(movie_name_search(final_movie_ids))
    csv_writer.writerow('\n')







