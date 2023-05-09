# This is a showcase of an ecommerce store

## Life cycle
+ [Analysis and specification requirements](#Analysis)
+ [Design](#Design)
    - [Flowchart](#Flowchart)
    - [Wireframe](#Wireframe)
+ [Coding](#Coding)
+ [Testing](#Testing)
+ [Instalation and production](#Installation)
+ [Maintenance](#Maintenance)


## Analysis
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


## Design
The design concept for our ecommerce store is centered around a modern and minimalistic style with a focus on usability and ease of navigation.
Come up with a plan or algorithm to successfully and efficiently execute the client needs based on the analysis requirements

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
We used Figma for our design work. You can view our design files on [Figma](https://www.figma.com/community/file/966016571279781800). Credit to @waverlylab for the creation of such wireframe 

### Technologies
We need a database like postgres, a data bus like kafka, an API like FastAPI