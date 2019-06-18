// Configurable Data Used by Test Suite

// Set the browser to use here.
exports.browser = 'chrome'

exports.spec1 = {
		input: {
			// Search for this term at https://www.peek.com main page at beginning of test.
			searchTerm: 'New York',
			
			// For search filter test, check on these checkboxes.
			filter: [
				'Under $50'
				]
		},
		output: {
			// For search filter test, verify the number of results after the filter(s) is checked.
			results: 84,
			
			// For category test, verify that the following categories and quantities appear in the provided order.
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
			// For the personality quiz, set the answers to provide for the nine questions.  0 = click on the left image, 1 = click on the right image
			q: [1, 0, 1, 0, 1, 0, 1, 0, 1]
		}
}

exports.spec3 = {
		input: {
			// Go to this page to begin the activity booking test.
			url: 'https://www.peek.com/san-diego_two-hour-off-road-jeep-tour-of-anza-borrego-state-park-a17YO5',
			
			// For ticket test, set the maximum number of tickets allowed for this activity.
			ticketsMax: 4
		}
}