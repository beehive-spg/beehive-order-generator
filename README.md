# Beehive Order Generator
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<img src="https://i.imgur.com/VnKmMI0.png" width="20%">

beehive-order-generator generates random orders for deliveries and sends them to the simulation
engine for further processing.


## Development

### Docker

To run a new container first execute

```docker build -t beehive-order-generator .```

inside the repository directory.

Then run

```docker run --env-file=.env -it beehive-order-generator```

to start the container.

Supply the ```-d``` option to keep it running in the background.

Or run the docker-compose file with 

```docker-compose up```

for the same result.
