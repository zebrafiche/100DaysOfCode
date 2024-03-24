import requests
import os
import tmdb

key = os.environ.get("API_Key")
url = "https://api.themoviedb.org/3/search/movie?query=The Shawshank"
id = 278
url2 = "https://api.themoviedb.org/3/movie/"
# print(url2+str(id))


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MDEyNTgwMDk2ODZmN2I1MGNiNDE5NzQ1MDcxZjNmMCIsInN1YiI6IjY1ZjY1OWYyZTE5NGIwMDE3Y2JlMjhjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dqlbbAIBebEWNSAoDyf7jKb9UGTp49JektSiVEWkBOs",
    # "API_Key": key
}

response = requests.get(url2+str(id), headers=headers)

print(response.json())
movie_detail = response.json()
print(movie_detail['original_title'])
print(movie_detail['release_date'][:4])
print(movie_detail['overview'])
print(movie_detail['poster_path'])
# print(type(response.json()))
# print(response.json()["results"])

# response = requests.get(f'https://api.themoviedb.org/3/movie/11?api_key={key}')
# print(response.text)

# results_dict = []
# for item in response.json()["results"]:
#     print(item['original_title'])
#     print(item['release_date'])
#     results_dict.append({"title": item['original_title'], "date": item['release_date']})
#     print(results_dict)


# movie_query = tmdb.MovieQuery()
# movie = movie_query.search('Reacher')
# print(movie)


