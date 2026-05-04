from pydantic import BaseModel, Field, EmailStr, field_validator


class Subscription(BaseModel):
    """
    Validated input schema for subscription requests that drive
    orbital event ingestion and notification workflows.
    """

    location_name: str = Field(..., min_length=1, max_length=100)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    notification_target: EmailStr
    lead_time_minutes: int = Field(default=10, ge=1, le=1440)

    @field_validator("location_name")
    @classmethod
    def strip_location(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("location_name cannot be empty")
        return v
