# Watch Next Movie

This project helps you find the most similar movie to watch next based on the description of a movie you've already watched.

## Requirements

- Docker

## How to run

1. Build the Docker image:

docker build -t watch_next .


2. Run the Docker container, passing the movie description as an argument:

docker run -it --rm watch_next "Movie description here"
