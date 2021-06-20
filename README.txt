This is my first micro-services architecture based web application.

The application's main purpose (besides learning) is to create and manage data about plants.

The application currently has one service that manages the plants, which is connected to MongoDB,
and it is accessible through an Nginx web server.

The application exposes a RESTfull API to manage plants (/v1/plants).