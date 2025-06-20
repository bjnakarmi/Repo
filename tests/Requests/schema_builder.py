# ------- Schema Building using genson(SchemaBuilder) ------
# pip install genson
from genson import SchemaBuilder

builder = SchemaBuilder()
builder.add_object(
{
    "status": "Success",
    "data": [
        {
            "id": 91,
            "title": "gsgs",
            "slug": "gsgs",
            "trainingType": "countryOwner",
            "documentType": "file",
            "videoUrl": "https://piiink-cms.s3.ap-south-1.amazonaws.com/860eceffc2d175563a8f076c295c5d42",
            "shortDescription": "ggs",
            "createdAt": "2023-12-06T08:29:01.193Z",
            "trainingVideoCategoryId": 23,
            "__trainingVideoCategory__": {
                "name": "test"
            }
        }
    ],
    "hasMore": 'false',
    "count": 1,
    "totalCount": 1,
    "page": 1
})

print(builder.to_json(indent=2))