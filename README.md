# This is a showcase of an ecommerce store

## Software Development Life cycle (SDLC)
+ [Analysis and specification requirements](#Analysis)
+ [Design](#Design)
    - [Architecture](#Architecture)
    - [Flowchart](#Flowchart)
    - [Wireframe](#Wireframe)
+ [Coding](#Coding)
+ [Testing](#Testing)
+ [Instalation and production](#Installation)
+ [Maintenance](#Maintenance)


## ANALYSIS
Specification requirements of the client. The client has a business idea and wants to implement it with our services. The client wants to:
+ Provide people with a comfortable way of shopping online
+ Provide suppliers with a comfortable business relationship
+ Provide a fast and easy solution for customers

#### Preliminary analysis: In order to provide a business solution we will need:
+ To know the inventory and its internal structure to manipulate it with a database:
    * Name, price, size, color, category, sku, images, description, discount, number of units, order status, shipping status
+ To guide a customer through different buying stages:
    * Awareness, exploration, decision making, purchasing and retantion
+ To generate all of the actions a user can perform:
    * Browse products and information, search products using filters, add x units to cart, remove x units from cart, update profile, pay, comment and rate products, contact support, register, login, logout
+ To make a scalable and robust website:
    + Robust:
        * Secure: Authentification, Encryption
        * Fast: Loading speed less than 2 seconds
        * Reliable: QA, Testing all routes, methods and user actions
    + Scalable:
        * Evolutionary model, clean code architecture, domain driven design 
+ To make the website appealing acording to the clients brand aesthetics
    * UX/UI
+ To ask the client for all the legal information to be included and display it to the users as well as the about us and or a whitepaper
+ To solve users questions
    * FAQ
    * Customer service
+ To maintain the website
+ To understand the marketing strategies
    * SEO, email marketing, discounts

#### Based on the preliminary analysis of our costumer, we can conclude:
+ Objectives:
    * Easy-to-use website
    * Secure and reliable website
    * Fast loading website
    * Fast database
    * Website routes for the user
    * Applealing website
    * Legal compliant
    * Customer service

+ Scope:
    * Analysis and specification of requirements
    * Design of the website and database structure
    * Coding of the website and database
    * Testing of all routes, methods, and user actions
    * Installation and production of the website
    * Maintenance of the website

+ Cost-volume-profit:
    * 


## DESIGN
The design concept for our ecommerce store is centered around a modern and minimalistic style with a focus on usability and ease of navigation.
Come up with a plan or algorithm to successfully and efficiently execute the client needs based on the analysis requirements

### Architecture
The Ecommerce Web App follows a modern, microservices-based architecture that provides a flexible and scalable platform for online shopping. The app is built using the following technologies:

* FastAPI: A modern, fast, web framework for building APIs with Python. FastAPI provides high performance, automatic validation, and easy-to-use asynchronous support.
* Kafka: A distributed streaming platform that enables real-time communication between services. Kafka provides scalable and fault-tolerant messaging, making it ideal for building microservices architectures.
* PostgreSQL: A powerful and reliable relational database management system. PostgreSQL provides a flexible data model, transaction support, and advanced features such as JSON storage and full-text search.

The app consists of the following microservices:

* Backend Service: Manages the interactions with the user and displays all the information. Provides the endpoints, APIs and allows interaction
* Inventory Service: Manages and tracks the inventory levels of each product. Provides operations for updating inventory levels and interacts with the Order Service.
* Order Service: Manages payments of the order placement and fulfillment process. Provides operations for placing orders, tracking order and status.
* User Service: Manages user authentication and authorization. Provides operations for registering, logging in, and managing user accounts.
* Marketing Service: Manages marketing campaigns and product discounts. Provides mechanisms for users to benefit from the different companys strategies.
* Email Service: Manages email sent to a subscribers list. Provides a list of subscribed user to send emails to and keeps track of the sent emails.
* Analytics Service: Keeps track of all actions in the platform. Provides statistics based on user interactions, consumer behaviour and measures marketing campaigns effectiveness.

Each microservice is built as a separate Python package and runs in its own Docker container. Communication between services is handled through Kafka topics, allowing for scalable and fault-tolerant messaging. The app also includes a gateway service, built with FastAPI, that provides a unified API for clients to interact with the microservices.

Overall, the microservices architecture provides a scalable and flexible platform for building an ecommerce web app, allowing for easy scaling and maintenance of individual components.


### Features:
* User registration and authentication
* Product catalog with search and filter functionality
* Shopping cart and checkout process
* Payment processing and order tracking
* User dashboard with order history and account settings
* Analytics and marketing modules


### Wireframe
Below are some screenshots of our ecommerce store
- Credit to [@waverlylab](https://www.figma.com/@waverlylab) for the creation of such wireframe
- License: [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- No changes were made to the original work

![Homepage screenshot](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-01.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-02.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-03.png?raw=true)
![Product page screenshot](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-04.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-05.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-06.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-07.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-08.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-09.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-10.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-11.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-12.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-13.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-14.png?raw=true)
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/wireframe/wireframe-15.png?raw=true)


### Flowchart
* User lands on the landing-page
* Clicks on a product that appeals
* Selects the correct size and color
* Adds to cart
* Clicks on checkout
* Inserts billing information
* Pays
* Receives a tracking number via email
* Checks the status of the tracking number
* Receives the package


#### Overview
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/Overview.png?raw=true)
#### Main
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/main_flowchart.png?raw=true)
#### Checkout
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/checkout_flowchart.png?raw=true)
#### Process order
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/process_order_flowchart.png?raw=true)
#### Login
![alt text](https://github.com/RomanW05/ecommerce/blob/main/blob/login_flowchart.png?raw=true)


### Live demo
You can view a live demo of our ecommerce store at [TBD](TBD).


### Design tools
We used Figma for our design work and https://app.diagrams.net for the diagrams overview. You can view our design files on [Figma](https://www.figma.com/community/file/966016571279781800) and ![Drawio](https://github.com/RomanW05/ecommerce/blob/main/blob/Overview.drawio)


## CODING
The actions, planning, design and standards to be used thoughtout the project are to be discussed by the development team. The selected methodology is the Agile due to the flexibility it provides.
* Code design: In this section we will use the gathered requirements and specifications during the previous phases (Preliminary analysis and features). Based on this understanding, the development team will create a plan for the code's architecture and algorithms to be used. They will define how the different components of the system will interact with each other, and the protocols to be used. The web application will use RESTful APIs to communicate with the database, and Kafka to handle real-time data streaming.
    - The development team must design the code structure and its functionality. They will create a detailed plan for the code's structure and algorithms to be used. The specific services that require such algorithms are the analytics, marketing and email. TODO (in the meantime we can start with the architecture, routes, tests and ![database code](https://github.com/RomanW05/ecommerce/blob/main/databases.py), ![database diagram](https://github.com/RomanW05/ecommerce/blob/main/blob/Overview.drawio), ![database overview](https://github.com/RomanW05/ecommerce/blob/main/blob/database_overview.png?raw=true))

* Coding standards: TODO
* Implementation: TODO
* Version control: The tools to organize the work will be Github
* Code review: TODO after implementation
* Integration testing: TODO
* Deployment: TODO