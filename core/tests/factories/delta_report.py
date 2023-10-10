from datetime import datetime
from django.utils import timezone
import factory
from core.models import DeltaReport


class DeltaReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DeltaReport

    vehicle_name = factory.Faker('text', max_nb_chars=20)
    period_start = factory.fuzzy.FuzzyDateTime(
        timezone.make_aware(datetime(2020, 3, 24, 20, 0, 0))
    )
    period_end = factory.fuzzy.FuzzyDateTime(
        timezone.make_aware(datetime(2023, 3, 24, 20, 0, 0))
    )
    fact_km = factory.Faker('random_int', min=0, max=1000)
    odometer_mileage = factory.Faker('random_int', min=0, max=10000)
    trip_mileage = factory.Faker('random_int', min=0, max=1000)
    start_balance = factory.Faker('random_int', min=0, max=1000)
    start_level = factory.Faker('random_int', min=0, max=1000)
    fueling_gsm = factory.Faker('random_int', min=0, max=1000)
    total_refueled = factory.Faker('random_int', min=0, max=1000)
    actual_fuel_consumption = factory.Faker('random_int', min=0, max=1000)
    norm_fuel_consumption = factory.Faker('random_int', min=0, max=1000)
    departure = factory.Faker('random_int', min=0, max=1000)
    avg_trip_dut_consumption = factory.Faker('random_int', min=0, max=1000)
    actual = factory.Faker('random_int', min=0, max=1000)
    fuel_calculation_norm = factory.Faker('random_int', min=0, max=1000)
    departure_balance = factory.Faker('random_int', min=0, max=1000)
    end_balance = factory.Faker('random_int', min=0, max=1000)
    end_level = factory.Faker('random_int', min=0, max=1000)
    end_mech_balance = factory.Faker('random_int', min=0, max=1000)
    difference = factory.Faker('random_int', min=0, max=1000)
    deficiency = factory.Faker('random_int', min=0, max=1000)
    surplus = factory.Faker('random_int', min=0, max=1000)
    total_fuel_drained = factory.Faker('random_int', min=0, max=1000)