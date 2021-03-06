# sobel

this is a demo to confirm availability of docker, cookie-cutter and flask. In this app, we can understand how sobel filter affect on images.
You can add your photo in the application, and you get an image processed by sobel filter.


## Setup development environment

We setup the development environment in a Docker container with the following command.

- `make init`

This command gets the resources for training and testing, and then prepares the Docker image for the experiments.
After creating the Docker image, you run the following command.

## Easiest Instruction

0. git clone this repository
1. make init
2. docker run -it --rm -p 8888:5000 -v $PWD:/work sobel-image
3. open "http://0.0.0.0:8888/" in your browser




## Usage

This section shows the detailed usages.

### Development

When we need to add libraries in `Dockerfile` or `requirements.txt`
which are added to working environment in the Docker container, we need to drop the current Docker container and
image, and then create them again with the latest setting. To remove the Docker the container and image, run `make clean-docker`
and then `make init-docker` command to create the Docker container with the latest setting.

### Login Docker container

Only the first time you need to create a Docker container, from the image created in `make init` command.
`make create-container` creates and launch the sobel container.
After creating the container, you just need run `make start-container`.

### Logout from Docker container

When you logout from shell in Docker container, please run `exit` in the console.

### Run linter

When you check the code quality, please run `make lint`

### Run test

When you run test in `tests` directory, please run `make test`

### Sync data source to local data directory

When you want to download data in remote data sources such as S3 or NFS, `sync-from-remote` target downloads them.

### Sync local data to remote source

When you modify the data in local environment, `sync-to-remote` target uploads the local files stored in `data` to specified data sources such as S3 or NFS directories.

### Show profile of Docker container

When you see the status of Docker container, please run `make profile` in host machine.

### Use Jupyter Notebook

To launch Jupyter Notebook, please run `make jupyter` in the Docker container. After launch the Jupyter Notebook, you can
access the Jupyter Notebook service in http://localhost:8888.

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [cookiecutter-docker-science](https://docker-science.github.io/) project template.

# notice

This repository is a reproduction of the content of 2018 summer internship. Thank you.

