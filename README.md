To build the docker image:

`docker build -t tj-app .`

To run the container:
We need to pass the secret key, remember to backspace the "!" characters.
`docker run --env-file .env  -p 8000:8000 tj-app-2`
