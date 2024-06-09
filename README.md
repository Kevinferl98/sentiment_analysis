# Sentiment analysis

## About this project

This web service allows users to submit text for sentiment analysis. 
The analysis is conducted utilizing the TextBlob library. 

Both the user's input and the resulting sentiment analysis are stored with the use of MongoDB.

## How to run it

In order to execute this project using Docker, it a prerequisite to have Docker installed on your system.

The project can be run simply by executing the following command:

```
docker-compose up -d
```
Executing this command will initiate and run the containers for both the web application and the database. 

Then, you can access the web application by navigating to the following URL: http://localhost:5000

## How to use it

In the provided text box you can write some text, by clicking on the send button the sentiment analysis of your input will be conducted and the results will be promptly displayed. 
