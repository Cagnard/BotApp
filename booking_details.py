# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
	def __init__(
		self,
		destination: str = None,
		origin: str = None,
		travel_date_dep: str = None,
		travel_date_arr: str = None,
		unsupported_airports=None,
		budget: str = None,
	):
		if unsupported_airports is None:
			unsupported_airports = []
		self.destination = destination
		self.origin = origin
		self.travel_date_dep = travel_date_dep
		self.travel_date_arr = travel_date_arr
		self.unsupported_airports = unsupported_airports
		self.budget = budget
