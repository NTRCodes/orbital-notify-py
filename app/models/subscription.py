from pydantic import BaseModel, Field, EmailStr


class Subscription(BaseModel):
    location_name: str = Field(..., min_length=1, max_length=100)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    notification_target: EmailStr
    lead_time_minutes: int = Field(default=10, ge=1, le=1440)
