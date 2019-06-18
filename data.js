// Configurable Data Used by Test Suite
exports.browser = 'chrome'

exports.spec1 = {
		input: {
			searchTerm: 'New York',
			filter: [
				'Under $50'
				]
		},
		output: {
			results: 84,
			cat: [
				{ name: 'Tours & Sightseeing', quantity: 60 },
				{ name: 'Cultural & Theme Tours', quantity: 58 },
				{ name: 'Food, Wine & Nightlife', quantity: 42 },
				{ name: 'Workshops & Classes', quantity: 28 },
				{ name: 'Outdoor Activities', quantity: 25 },
				{ name: 'Cruises, Sailing & Boat Tours', quantity: 24 },
				{ name: 'Attraction Tickets & Passes', quantity: 14 },
				{ name: 'Plane, Helicopter & Balloon Tours', quantity: 14 },
				{ name: 'Shows, Concerts & Sports', quantity: 12 }						
				]
		}
}

exports.spec2 = {
		input: {
			q: [1, 0, 1, 0, 1, 0, 1, 0, 1]
		}
}

exports.spec3 = {
		input: {
			url: 'https://www.peek.com/san-diego_two-hour-off-road-jeep-tour-of-anza-borrego-state-park-a17YO5',
			ticketsMax: 4
		}
}