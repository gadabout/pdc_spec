import Home from '../pages/Home'
import Activity from '../pages/Activity'

describe('As a consumer visiting Peek.com I would like to be able to book an activity', () => {

    beforeEach(() => {
        browser.maximizeWindow()
        Home.open()
    })

    it('The activity\'s calendar widget populates with bookable days', () => {
        Home.openTopPickBy("Two Hour Off-Road Jeep Tour of Anza Borrego State Park")
        Activity.openBookNowModal()
        expect(Activity.lblAvailable.isDisplayed()).to.equal(true)
    })

    it('Increasing the number of selected tickets beyond the availability prevents me from booking that timeslot', () => {
        Home.openTopPickBy("Two Hour Off-Road Jeep Tour of Anza Borrego State Park")
        Activity.openBookNowModal()
        Activity.selectAvailableDay("24")
        Activity.selectAvailableTime("9:00am")
        Activity.increaseTicketsTo(10)
        expect(Activity.lblSoldOut.isDisplayed()).to.equal(true)
    })

    it('The "Book Now" Button opens a widget flow with my timeslot and ticket(s) selected at checkout', () => {
        Home.openTopPickBy("Two Hour Off-Road Jeep Tour of Anza Borrego State Park")
        Activity.bookNow()
        expect(Activity.lblPaymentInfo.getText()).to.equal("Your Payment Information")
    })
})