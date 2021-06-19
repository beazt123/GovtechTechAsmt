# API documentation

## Contents
- [API documentation](#api-documentation)
  - [Contents](#contents)
  - [`POST /users/upload`](#post-usersupload)
    - [Test cases](#test-cases)
  - [`GET /users`](#get-users)
    - [Request args](#request-args)
    - [Test cases](#test-cases-1)


## `POST /users/upload`
- Upload in multipart/formdata -> 'text/csv'
- Optional to support concurrent upload
- Reject upload if any rows fail validation

### Test cases
- Good data file
- Reject Empty file
- Reject too many/too few columns -> Must be exact
- Reject incorretly formatted salaries
- reject salary <0
- Upload 2 files concurrently

## `GET /users`
### Request args
Arg | Description
-|-
`minSalary` |  float
`maxsalary` | float
`offset` | integer
`limit` | 30 (Defaulted and fixed. Not exposed)
`sort`  |(+-) (by) i.e. +name := ascending order of name

### Test cases
- All args compulsory and must be valid, else 400
- Successful repsonse:
```
    {
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
```