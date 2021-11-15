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



### API Docs
API Spec available at:
http://localhost:8000/docs

### API Routes
**Fetch objects**
[GET]
```
/
/user_behaviour/json
/user_behaviour/dodgy_endpoint
/user_behaviour_10k/json
```

### Generate Dummy Data
Generate dummy script usage:

```
usage: generate_userbehaviour_rows.py [-h] --rows ROWS
```

To generate 10000 new JSON Objects run the following command:

```
python ./bin/generate_userbehaviour_rows.py --rows 10000
```

Data is available in the `data/` directory