from pydantic import BaseModel, Field, constr
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from spectree.models import ValidationError


class Profile(BaseModel):
    name: constr(min_length=1, max_length=50)
    age: int = Field(..., gt=0, lt=130, description="Age of the user")

    class Config:
        schema_extra = {
            "example": {"name": "John Doe", "age": 25},
        }


class Message(BaseModel):
    text: constr(min_length=1, max_length=50)


app = Flask(__name__)
api = FlaskPydanticSpec("flask")


@app.route("/api/v1/user", methods=["POST"])
@api.validate(
    body=Request(Profile),
    resp=Response(HTTP_201=Message, HTTP_422=ValidationError),
    tags=["api"],
)
def create_user():
    print(Profile.schema_json(indent=2))
    return jsonify(text="User Created"), 201


if __name__ == "__main__":
    api.register(app)
    app.run(port=5000)
