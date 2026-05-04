import pytest
from pydantic import ValidationError

from app.models.subscription import Subscription


def test_valid_subscription_model():
    subscription = Subscription(
        location_name="Henderson, NV",
        latitude=36.0395,
        longitude=-114.9817,
        notification_target="nigel@example.com",
        lead_time_minutes=10,
    )

    assert subscription.location_name == "Henderson, NV"
    assert subscription.latitude == 36.0395
    assert subscription.longitude == -114.9817
    assert subscription.notification_target == "nigel@example.com"
    assert subscription.lead_time_minutes == 10


@pytest.mark.parametrize("latitude", [-91, 91])
def test_subscription_rejects_invalid_latitude(latitude):
    with pytest.raises(ValidationError):
        Subscription(
            location_name="Invalid Latitude",
            latitude=latitude,
            longitude=-114.9817,
            notification_target="nigel@example.com",
            lead_time_minutes=10,
        )


@pytest.mark.parametrize("longitude", [-181, 181])
def test_subscription_rejects_invalid_longitude(longitude):
    with pytest.raises(ValidationError):
        Subscription(
            location_name="Invalid Longitude",
            latitude=36.0395,
            longitude=longitude,
            notification_target="nigel@example.com",
            lead_time_minutes=10,
        )


@pytest.mark.parametrize("lead_time", [0, -1, 1441])
def test_subscription_rejects_invalid_lead_time(lead_time):
    with pytest.raises(ValidationError):
        Subscription(
            location_name="Invalid Lead Time",
            latitude=36.0395,
            longitude=-114.9817,
            notification_target="nigel@example.com",
            lead_time_minutes=lead_time,
        )


def test_subscription_rejects_invalid_notification_target():
    with pytest.raises(ValidationError):
        Subscription(
            location_name="Invalid Email",
            latitude=36.0395,
            longitude=-114.9817,
            notification_target="not-an-email",
            lead_time_minutes=10,
        )


def test_subscription_rejects_empty_location_name():
    with pytest.raises(ValidationError):
        Subscription(
            location_name="",
            latitude=36.0395,
            longitude=-114.9817,
            notification_target="nigel@example.com",
            lead_time_minutes=10,
        )
