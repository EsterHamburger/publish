from pydantic import BaseModel


class message_details(BaseModel):
    name: str
    shapefile_path: str
    tiffs_path: str
    sensor: str
    logs_path: str
