import requests


# url = "https://api.themoviedb.org/3/search/movie?query="


class MovieQuery:
    def __init__(self):
        self.url = f"https://api.themoviedb.org/3/search/movie?query="
        self.url_id = f"https://api.themoviedb.org/3/movie/"
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MDEyNTgwMDk2ODZmN2I1MGNiNDE5NzQ1MDcxZjNmMCIsInN1YiI6IjY1ZjY1OWYyZTE5NGIwMDE3Y2JlMjhjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dqlbbAIBebEWNSAoDyf7jKb9UGTp49JektSiVEWkBOs",
            }
        self.results = []
        self.results_by_id = {}

    def search(self, movie_name):
        response = requests.get(self.url+movie_name, headers=self.headers)
        for item in response.json()["results"]:
            self.results.append({"id": item['id'], "title": item['original_title'], "date": item['release_date']})
        return self.results

    def search_by_id(self, movie_id):
        response = requests.get(self.url_id+str(movie_id), headers=self.headers)
        movie_detail = response.json()
        # print(movie_detail)
        self.results_by_id["movie_title"] = movie_detail['original_title']
        self.results_by_id["movie_release_date"] = movie_detail['release_date']
        self.results_by_id["movie_overview"] = movie_detail['overview']
        self.results_by_id["movie_poster"] = movie_detail['poster_path']
        return self.results_by_id



