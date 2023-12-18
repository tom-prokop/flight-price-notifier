from duffel_api import Duffel

duffel = Duffel(access_token="duffel_test_TKTr4Fa_vRhW4JPG88zltoYm2SQJXmwPqM5Q-zDckVq")

slices = [
    {"origin": "NYC", "destination": "ATL", "departure_date": "2023-06-21"},
    {"origin": "ATL", "destination": "NYC", "departure_date": "2023-07-21"},
]
passengers = [{"type": "adult"}, {"type": "adult"}, {"age": 1}]
here = (
    duffel.offer_requests.create()
    .slices(slices)
    .passengers(passengers)
    .cabin_class("business")
    .execute()
)
print(here)
