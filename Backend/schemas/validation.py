from pydantic import BaseModel,Field,field_validator
from .transform import transform_text
from typing import Annotated


class Input(BaseModel):
    message:Annotated[str,Field(...,description="This is the message for spam prediction",title="Message for Spam Detection")]

    @field_validator('message')
    @classmethod
    def validate_message(cls,value):
        msg=transform_text(value)
        return msg
    

# msg={'message':"Did you finish your work?"}

# test=Input(**msg)

# print(test.message)