# Thrivey Dummy Data API
Data API built on Python **FastAPI** with local **sqlite** db.


## Get Started

**LOCAL**

0. Run tox to install deps, build & test
    
    ```
    tox
    ```

1. Execute DB preperation script:

    ```
    $SHELL bin/prep-db.sh
    ```

2. Run API with default params

    ```
    $SHELL bin/run-api.sh
    ```


**DOCKER**

0. Build docker container
    
    ```
    docker build -t thrivey-api-local .
    ``` 

1. Run Containerized API on http://localhost:8000

    ```
    docker run -p 8000:8000 thrivey-api-local
    ```



### API Routes
**Fetch objects**
[GET]
```
/
/user/table
/behaviour/table
/user_behaviour/table
/user_behaviour/json
```
**Validate objects**
[POST]
```
/user/validate
/behaviour/validate
/user_behaviour/validate
```