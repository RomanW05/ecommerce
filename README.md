# This is a showcase of an ecommerce store

## Software Development Lifecycle (SDLC)
<ul>
    <li><a href="#overview">0. Overview</a></li>
    <li><a href="#analysis">1. Analysis and specification requirements</a></li>
    <li><a href="#design">2. Design</a></li>
        <ul>
            <li><a href="#Architecture">2.1 Architecture</a></li>
            <li><a href="#Flowchart">2.2 Flowchart</a></li>
            <li><a href="#Wireframe">2.3 Wireframe</a></li>
            <li><a href="">2.4 Overview</a></li>
                <ul>
                    <li><a href="#Overview">2.4.1 Overview</a></li>
                    <li><a href="#Main">2.4.2 Main</a></li>
                    <li><a href="#Checkout">2.4.3 Checkout</a></li>
                    <li><a href="#Process-order">2.4.4 Process order</a></li>
                    <li><a href="#Login">2.4.5 Login</a></li>
                    <li><a href="#Project-sturcture">2.4.6 Project structure</a></li>
                </ul>
        </ul>
    <li><a href="#coding">3. Coding</a></li>
        <ul>
            <li><a href="#31-coding-standards">3.1 Coding Standards</a></li>
                <ul>
                <li><a href="#311-General-coding-standards">3.1.1 General Coding Standards</a></li>
                    <ul>
                        <li><a href="#3111-Formatting-and-Style-Guidelines">3.1.1.1 Formatting and Style Guidelines</a></li>
                        <li><a href="#3112-Code-Organization">3.1.1.2 Code Organization</a></li>
                        <li><a href="#3113-documentation">3.1.1.3 Documentation</a></li>
                        <li><a href="#3114-Type-Hints">3.1.1.4 Type Hints</a></li>
                        <li><a href="#3115-Best-Practices">3.1.1.5 Best Practices</a></li>
                    </ul>
                </ul>
        </ul>
    <li><a href="#testing">4. Testing</a></li>
    <li><a href="#deployment">5. Deployment</a></li>
    <li><a href="#maintenance">6. Maintenance</a></li>
</ul>

## OVERVIEW
#### Microservice architecture
![Architecture overview](https://github.com/RomanW05/ecommerce/blob/main/blob/Overview.drawio.png)
#### Database structure
![Database overview](https://github.com/RomanW05/ecommerce/blob/main/blob/database_diagram.drawio.png)


## ANALYSIS
![Analysis and requirements](https://github.com/RomanW05/ecommerce/blob/main/documentation/1.Analysis.md)


## DESIGN
![Design](https://github.com/RomanW05/ecommerce/blob/main/documentation/2.Design.md)


## CODING
The actions, planning, design and standards to be used thoughtout the project are to be discussed by the development team. The selected methodology is the Agile due to the flexibility it provides.
* Code design: In this section we will use the gathered requirements and specifications during the previous phases (Preliminary analysis and features). Based on this understanding, the development team will create a plan for the code's architecture and algorithms to be used. They will define how the different components of the system will interact with each other, and the protocols to be used. The web application will use RESTful APIs to communicate with the database, and Kafka to handle real-time data streaming.
    - The development team must design the code structure and its functionality. They will create a detailed plan for the code's structure and algorithms to be used. The specific services that require such algorithms are the analytics, marketing and email. TODO (in the meantime we can start with the architecture, routes, tests and ![database code](https://github.com/RomanW05/ecommerce/blob/main/databases.py), ![database diagram](https://github.com/RomanW05/ecommerce/blob/main/blob/Overview.drawio), ![database overview](https://github.com/RomanW05/ecommerce/blob/main/blob/database_overview.png?raw=true))

*    1. Coding standards:

    The coding standards outlined in this document are intended to ensure consistency, maintainability, and code quality for the E-Commerce Store project. This project utilizes Python, Django, Kafka, and Docker Compose.
            1.1. General coding standards
                1.1.1. Formatting and Style Guidelines
                    - Follow the PEP 8 style guide for Python code formatting.
                    - Use four spaces for indentation.
                    - Limit lines to 79 characters for code and 72 characters for docstrings.
                    - Flake8 will be applied to all code in order to speed up the coding process
                    - Use clear and descriptive variable and function names.
                    - Avoid excessive nesting and maintain concise code blocks.
                1.1.2 Code Organization
                    - Follow a clear directory structure for the project. The struture will be the same for every microservice using Django-Rest-Framework(DRF) and will be implemented using cookiecutter https://github.com/Ohuru-Tech/drf-cookiecutter.
                    - Organize code into modules and packages with meaningful names.
                    - Use meaningful names for files and directories.
                    - Group related code together within modules.
                1.1.3 Documentation
                    - Use docstrings for functions, classes, and modules.
                    - Document function and class parameters and return values.
                    - Include module-level documentation describing the purpose and usage.
                    - Maintain consistency in documentation format and style.
                1.1.4 Type Hints
                    - Use type hints for function and variable declarations (Python 3.5+).
                    - Clearly specify function parameter types and return types.
                    - Ensure that type hints accurately reflect the code's behavior.
                1.1.5 Best Practices
                    - Follow the DRY, SOLID principles.
                    - Write unit tests using unittest or pytest for code quality.
                    - Avoid magic numbers and hardcoding values. Use constants or configuration files.
                    - Keep functions and methods concise and focused on a single task.
            1.2 Django-specific coding standards
                1.2.1 Code Organization
                    - Follow Django's recommended project directory structure.
                    - Use Django's app structure to modularize components.
                    - Keep views and templates simple and separated by concerns.
                    - Use Django's ORM for database interactions.
                    - Create clear and well-documented database models and migrations.
                    - Use efficient querying practices to optimize database performance.
                    - Implement caching for frequently accessed data.
            1.3 Kafka-specific coding standards
                1.3.1 Code Organization
                    - Follow Confluent Platform's naming conventions for Kafka topics.
                    - Define clear message schemas for Kafka topics.
                    - Use meaningful and descriptive topic names.
                    - Configure consumer group names and offsets properly.
                    - Handle message deserialization and validation securely.
                    - Implement error handling and retry mechanisms for message processing.
            1.4 Docker-Compose-specific coding standards
                1.4.1 Code Organization
                    - Write clear and well-documented Dockerfiles for services.
                    - Define services and dependencies in a docker-compose.yml file.
                    - Use named volumes for persistent data.
                    - Configure environment variables for service settings securely.
                    - Use network modes and labels for service communication.
                    - Keep Docker images up to date and address security vulnerabilities.
            1.5 Version Control Integration
                Maintain the coding standards document in the project's version control repository.
                Update the document when coding standards evolve.


## TESTING

    It will consist of unitary tests, performance tests, integration tests and deployment tests


## DEPLOYMENT

    Gitlab will be used to create a Continious Integration and Continious Deployment (CI/CD) pipeline using the configuration file ".gitlab-ci.yml". Each microservice has its own Dockerfile image to meet the Gitlab criteria and apply automatically the specified steps.
    Azure will be used to host the application in the form of a docker-compose image containing all the microservices. A configuration file for the Azure platform is needed to pull the microservices from Gitlab "deploy-task.yaml"
    - First: The code is commited and pushed to Gitlab where integration and deployment tests are held in the file "docker-compose.test.yml".
    - Second: The docker-compose application is deployed to Azure using the gitlab configuration file

    Gitlab will 

## MAINTENANCE



## CURRENT STATUS
* Implementation: Ongoing
* Version control: The tools to organize the work will be Github
* Code review: After implementation
* Deployment: Jenkins will integrate the source code into a pipe to make the Continious Development/Continious Integration seemless


















