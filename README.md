# Real Time Data Streaming Analytics System for tracking pedestrians

## The Project GOAL 

![Screenshot (488)](https://user-images.githubusercontent.com/74468388/146798688-c5035625-2ee2-4e0b-bece-72cf5d27cdd7.png)

## The Main Project Functional Architecture 

![Screenshot (487)](https://user-images.githubusercontent.com/74468388/146799004-0b42f1e7-60c3-4b65-a16c-37e7d765b2b0.png)

## The Technical Project Architecture


![I-track - Technical architecture](https://user-images.githubusercontent.com/74468388/149933820-f1df134b-f7d7-473b-98a1-917e1c0d247c.png)

<details><summary>Project Description</summary>
<p>
First of all, we chosed traccar server as data source generator. We installed on our users' phones the traccar client application to establish a connection with traccar server, the data generated from the application will be sent to traccar server and mongoDB will act as a database for traccar server. the connection between these two components was established with the help of a websocket API using a python program for this purpose. 
</p>
  
<p>
After generating the data, two main phases are coming in the picture, batch processing and stream processing. For the batch phase we used S3 as a cloud simple storage datalake service for advanced analytics and ML algorithms purpose using a python program that stores the data generated from traccar Server as excel file every 24 hours and store it in S3, then we connected S3 with the sageMaker service to manipulate this for and build an adequate models.
</p>  

<p>
Let's move now the stream processing phase, Kafka was used as a data ingestion tool between mongoDB and spark streaming, so here mongoDB were acting as a producer and spark as consumer that subscribes to our kafka topic. 
</p>   
</details>


## Data source

- **The application name :** traccar client
- **The application url      :** https://play.google.com/store/apps/details?id=org.traccar.client

Description :  
![Capture](https://user-images.githubusercontent.com/74468388/142759290-c207da1e-ef2b-44a4-99b5-978956642716.PNG)

Traccar Client is an app that allows you to use your mobile device as a GPS tracker. It reports location to your own or hosted server with selected time intervals.

By default application is configured to use free Traccar service (address - demo.traccar.org, port - 5055). To see your device on map register on http://demo.traccar.org/ and add your device with identifier.

Traccar (Server) is a free open source server that supports more than 100 different protocols and GPS tracking devices. You can use this application with your own hosted instance of Traccar. For more information visit https://www.traccar.org/.

## Traccar Server 

We installed traccar server on a digitalocean VPC, it will cost us 5$ for one month from 100$ promo credit ( i used github student offer ) 

So the traccar is accessible publicly for now you and anyone can access it using this link : 

http://167.99.215.40:8082/

The traccar server is using h2 in memory database by default and we have to configure our custom mongoDB database as a next step. 

![Screenshot (481)](https://user-images.githubusercontent.com/74468388/146070938-1a731c94-5de5-4a75-bd9c-5a4c4745b9b4.png)

## Traccar and mongoDB nosql database connection

We used python sdk to connect the traccar server and the mongodb using the websocket.

## The Technical Project Architecture
