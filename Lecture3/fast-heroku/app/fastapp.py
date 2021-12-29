from fastapi import FastAPI,Request
from app.area import area_to_acre


app=FastAPI()

@app.get('/')
async def get_input(request:Request):
    """
        Get inputs from users and call the area calculation
    """
    getInput=await request.json()
    length=getInput['length']
    width=getInput['width']
    area=area_to_acre(length,width)
    return area

