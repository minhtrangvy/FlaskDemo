# FlaskDemo
This is for GA's Python Web Dev Course.
This app is a movie app! Read more about the actual purpose of the app in index.html, once you've spun up the local server.

## Instructions
1. You need the correct Twilio Auth token. It should look something like `21xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`. Set it to the `AUTH_TOKEN` environment variable.    
2. Then run `flask run`
3. Profit at `localhost:5000`

## Routes
### /, /index
Returns the Home page that describes what the app is about and how to nagivate it.
### /all_movies
Lists all the movies that are currently in theaters. More specifically, it lists all movies that were released within the last month.
### /form
Renders a form where the user can input their phone number and choose their favorite movie genres.


## References
### The Movie DB API
#### Sample curls
Fetch all movies released within a time frame
```
https://api.themoviedb.org/3/discover/movie?api_key=e8dde08f9b59d0ec23beda6b2b925cfc&primary_release_date.gte=2019-01-01&primary_release_date.lte=2019-02-18
```
#### Disclaimer
All movie information displayed in this app is pulled from The Movie DB API. Sometimes the API could have incorrect information because it is a relatively open API where anyone can edit the information online. Kind of like Wikipedia. If anything looks suspicious or wrong, don't hesitate to email me at trangandpuppies@gmail.com and I can send them a support email!
