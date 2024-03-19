from starlette.responses import JSONResponse


class MessageError:
    @classmethod
    def access(cls):
        return JSONResponse(status_code=404, content={"message": "Error access"})

    @classmethod
    def empty(cls):
        return JSONResponse(status_code=400, content={"message": "Body is empty"})

