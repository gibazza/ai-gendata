Azure OpenAI generated Employee Records
=======================================

Produces 10 employee records and randomly generates values specified in the ./schema/person_schema.json file.

For example:
```
{
  "rows": [
    {
      "firstName": "Jeanne",
      "surname": "Dubois",
      "displayName": "Jeanne Dubois",
      "department": "Sales",
      "employeeID": "1000",
      "jobTitle": "Sales Manager",
      "startDate": "2015-06-12",
      "leaveDate": "",
      "manager": null
    },
    {
      "firstName": "Mohammed",
      "surname": "Ali",
      "displayName": "Mohammed Ali",
      "department": "Sales",
      "employeeID": "1001",
      "jobTitle": "Sales Executive",
      "startDate": "2018-09-03",
      "leaveDate": "",
      "manager": "1000"
    },
    {
      "firstName": "Emma",
      "surname": "Chen",
      "displayName": "Emma Chen",
      "department": "Marketing",
      "employeeID": "1002",
      "jobTitle": "Marketing Manager",
      "startDate": "2014-02-18",
      "leaveDate": "",
      "manager": null
    },
    {
      "firstName": "Carlos",
      "surname": "Lopez",
      "displayName": "Carlos Lopez",
      "department": "Marketing",
      "employeeID": "1003",
      "jobTitle": "Marketing Executive",
      "startDate": "2019-05-02",
      "leaveDate": "",
      "manager": "1002"
    },
    {
      "firstName": "Hiroshi",
      "surname": "Nakamura",
      "displayName": "Hiroshi Nakamura",
      "department": "Product Development",
      "employeeID": "1004",
      "jobTitle": "Product Development Manager",
      "startDate": "2012-11-24",
      "leaveDate": "",
      "manager": null
    },
    {
      "firstName": "Luisa",
      "surname": "Gonzalez",
      "displayName": "Luisa Gonzalez",
      "department": "Product Development",
      "employeeID": "1005",
      "jobTitle": "Product Development Engineer",
      "startDate": "2016-03-10",
      "leaveDate": "",
      "manager": "1004"
    },
    {
      "firstName": "Aya",
      "surname": "Tanaka",
      "displayName": "Aya Tanaka",
      "department": "Finance",
      "employeeID": "1006",
      "jobTitle": "Finance Manager",
      "startDate": "2013-08-17",
      "leaveDate": "",
      "manager": null
    },
    {
      "firstName": "Miguel",
      "surname": "Martinez",
      "displayName": "Miguel Martinez",
      "department": "Finance",
      "employeeID": "1007",
      "jobTitle": "Financial Analyst",
      "startDate": "2017-01-05",
      "leaveDate": "",
      "manager": "1006"
    },
    {
      "firstName": "Sofia",
      "surname": "Ramos",
      "displayName": "Sofia Ramos",
      "department": "IT",
      "employeeID": "1008",
      "jobTitle": "IT Manager",
      "startDate": "2015-10-20",
      "leaveDate": "",
      "manager": null
    },
    {
      "firstName": "Mateusz",
      "surname": "Novak",
      "displayName": "Mateusz Novak",
      "department": "IT",
      "employeeID": "1009",
      "jobTitle": "Software Engineer",
      "startDate": "2016-09-12",
      "leaveDate": "2021-01-31",
      "manager": "1008"
    }
  ]
}
```