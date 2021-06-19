Pdt Backlog
Features:
- Upload CSV file
    - Ignore first row of headings
    - All fields mandatory
    - Ignore #
    - id & login is unique globally

    - If ID exists in DB, PATCH, otherwise, POST
        - if a `login` is PATCHed, make sure it remains unique within DB
        - Possible to build a login ID swapping by using a temporary unique ID
    - Return a confirmation of success/failure
    - API
        - POST /users/upload
        - multipart formdata
        - mimetype: 'text/csv'
        - 200 or appropriate error code

- Optional to support concurrent uploads:
    - If don't support, throw error when an upload is requested while another is taking place


- Employee dashboard
    - Max per call = 30
    - API
        - GET /users
        - args
            - minSalary
            - maxsalary
            - offset
            - limit
            - sort: (+-) (by) i.e. +name := ascending order of name
        - All params compulsory, else 400
        - invalid request, 400
        - response
            - {
                results: [
                    {
                        "id": 3fr,
                        "name": "rwfq",
                        "salary": 1223
                    },
                    {...},
                    ...
                ]
            }