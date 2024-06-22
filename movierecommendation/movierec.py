import requests


def get_movie_recommendations(movie_title):
    api_key = 'YOUR_API_KEY'         # Replace 'YOUR_API_KEY' with your own TMDB API key
    base_url = 'https://api.themoviedb.org/3'
    search_endpoint = '/search/movie'
    recommendation_endpoint = '/movie/{movie_id}/recommendations'


    search_params = {'api_key': api_key, 'query': movie_title}
    search_response = requests.get(base_url + search_endpoint, params=search_params)
    search_results = search_response.json()

    if search_results['total_results'] == 0:
        return "No movie found with that title. Please try again."


    movie_id = search_results['results'][0]['id']


    recommendation_url = base_url + recommendation_endpoint.format(movie_id=movie_id)
    recommendation_params = {'api_key': api_key}
    recommendation_response = requests.get(recommendation_url, params=recommendation_params)
    recommendation_results = recommendation_response.json()

    recommendations = []
    for result in recommendation_results['results']:
        recommendations.append(result['title'])

    return recommendations


movie_title = input("Enter the title of a movie: ")
recommendations = get_movie_recommendations(movie_title)

if isinstance(recommendations, str):
    print(recommendations)
else:
    print("Recommended movies based on", movie_title, ":")
    for recommendation in recommendations:
        print(recommendation)
