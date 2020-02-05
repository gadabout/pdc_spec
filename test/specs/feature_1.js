import Home from '../pages/Home'
import SearchActivities from '../pages/SearchActivities'

describe('As a consumer visiting Peek.com I would like to be able to search for activities near me', () => {

    beforeEach(() => {
        browser.maximizeWindow()
        Home.open()
    })

    it('Search filters correctly apply after initial search', () => {
        Home.enterLocation("")
        Home.setFromDateInCalendar(21, "March", 2020)
        Home.setToDateInCalendar(5, "May", 2021)
        Home.submit()

        SearchActivities.sortBy('Lowest Price')
        SearchActivities.filterBy('Under $50')
    })

    it('Categories appear based on location inventory', () => {
        Home.enterLocation("New York")
        Home.setFromDateInCalendar(11, "April", 2020)
        Home.setToDateInCalendar(23, "June", 2021)
        Home.submit()

        expect(SearchActivities.locationHeader.getText()).to.equal("New York")
    })
})