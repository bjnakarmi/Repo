# Schema Validation ensures your api responses match the expected structure
# A critical step in maintaining API reliability during test automation


import pytest
import requests
from genson import SchemaBuilder
from jsonschema import validate


# def test_post_schema_validation():
#     url = 'https://jsonplaceholder.typicode.com/posts/1'
#     response = requests.get(url = url)
#
#     assert response.status_code == 200
#
#     #Define expected schema
#     schema = {
#         'type' : 'object',
#         'properties' : {
#             'userId' : {'type':'integer'},
#             'id' : {'type': 'integer'},
#             'title' : {'type': 'string'},
#             'body' : {'type': 'string'}
#         },
#         'required' : ['userId', 'id', 'title', 'body']
#     }
#     #Validate the response json against the schema
#     print(response.json())
#     validate(instance=response.json(), schema=schema)


# ------ Schema building and validation for a large object ------

# def test_schema_validation():
#     header = {
#         'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDAyMjY4OCwiZXhwIjoxNzU3Nzk4Njg4fQ.DEUWQemQ1aIKLc7kKIw4mDrxrTL9O3CJNdk_i_FWDLA'
#     }
#     response = requests.get("https://staging.dev.piiink.org/api/globalSetting/trainingVideo/getAllByPanel?page=1&limit=10&offset=0&trainingVideoCategoryId=23", headers=header)
#     assert response.status_code == 200
#
#     #Define Expected Schema
#     schema = {
#         'type' : 'object',
#         'properties': {
#             'status': {'type' : 'string'},
#             'data' : {'type' : 'array',
#                       'items' : {'type' : 'object',
#                                  'properties' :{
#                                      'id' : {'type': 'integer'},
#                                      'title' : {'type' : 'string'},
#                                      'slug' : {'type': 'string'},
#                                      "trainingType": {"type": "string"},
#                                      "documentType": {"type": "string"},
#                                      "videoUrl": {"type": "string", "format": "uri"},
#                                      "shortDescription": {"type": "string"},
#                                      "createdAt": {"type": "string", "format": "date-time"},
#                                      "trainingVideoCategoryId": {"type": "integer"},
#                                      "__trainingVideoCategory__": {
#                                          "type": "object",
#                                          "properties": {
#                                              "name": {"type": "string"}
#                                          },
#                                          "required": ["name"]
#                                      }
#                                  },
#                                  "required": [
#                                      "id", "title", "slug", "trainingType", "documentType",
#                                      "videoUrl", "shortDescription", "createdAt",
#                                      "trainingVideoCategoryId", "__trainingVideoCategory__"]
#                                  }
#                     },
#             'hasMore' : {'type' : 'boolean'},
#             'count' : {'type' : 'integer'},
#             'totalCount' : {'type' : 'integer'},
#             'page' : {'type' : 'integer'}
#             },
#
#          "required": ["status", "data", "hasMore", "count", "totalCount", "page"]
#
#     }
#
#     validate(instance=response.json(), schema=schema)



def test_schema_validation():
    header = {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDAyMjY4OCwiZXhwIjoxNzU3Nzk4Njg4fQ.DEUWQemQ1aIKLc7kKIw4mDrxrTL9O3CJNdk_i_FWDLA'
    }
    response = requests.get("https://staging.dev.piiink.org/api/globalSetting/trainingVideo/getAllByPanel?page=1&limit=10&offset=0&trainingVideoCategoryId=23", headers=header)
    assert response.status_code == 200

    #Define Expected Schema
    schema = {
      "type": "object",
      "properties": {
        "status": {
          "type": "string"
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "title": {
                "type": "string"
              },
              "slug": {
                "type": "string"
              },
              "trainingType": {
                "type": "string"
              },
              "documentType": {
                "type": "string"
              },
              "videoUrl": {
                "type": "string"
              },
              "shortDescription": {
                "type": "string"
              },
              "createdAt": {
                "type": "string"
              },
              "trainingVideoCategoryId": {
                "type": "integer"
              },
              "__trainingVideoCategory__": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  }
                },
                "required": [
                  "name"
                ]
              }
            },
            "required": [
              "__trainingVideoCategory__",
              "createdAt",
              "documentType",
              "id",
              "shortDescription",
              "slug",
              "title",
              "trainingType",
              "trainingVideoCategoryId",
              "videoUrl"
            ]
          }
        },
        "hasMore": {
          "type": "boolean"
        },
        "count": {
          "type": "integer"
        },
        "totalCount": {
          "type": "integer"
        },
        "page": {
          "type": "integer"
        }
      },
      "required": [
        "count",
        "data",
        "hasMore",
        "page",
        "status",
        "totalCount"
      ]
    }

    validate(instance=response.json(), schema=schema)

