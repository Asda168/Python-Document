from fastapi.responses import JSONResponse


def success(data=None):
    return JSONResponse(
        status_code=200,
        content={
            "success": True, 
            "data": data
        }
    )


def fail(message=None, code=400, data=None):
    return JSONResponse(
        status_code=code,
        content={
            "success": False, 
            "message": message, 
            "data": data
        }
    )