import Base from './Base';

class Activity extends Base {
    open() {
        super.open('/');

        return this;
    }

    openBookNowModal() {
        while (this.bookNowModal.isDisplayed() === false) {
            this.btnBookNow.click()
            browser.pause(3500)
        }

        browser.switchToFrame(1)

        browser.waitUntil(() => {
            return this.lblAvailable.isDisplayed() === true
        }, 10000, 'modal fully loaded after 10s');
    }

    increaseTicketsTo(number) {
        for (let i = 0; i < number; i++) {
            this.btnAddTicket.click();
            browser.pause(500)
        }

        browser.pause(3500)
    }

    bookNow() {
        this.openBookNowModal()
        this.selectAvailableDay("20")
        this.selectAvailableTime("9:00am")
        this.txtFirstName.addValue("John")
        this.txtLastName.addValue("Smith")
        this.txtPhone.addValue("1 231-231-1111")
        this.txtEmail.addValue("johnsmith@faker.com")
        this.btnAddTicket.click()

        browser.execute(() => {
            document.querySelector("div.ui-element-disabled-opaque").classList.remove('ui-element-disabled-opaque');
            document.querySelectorAll("div.ui-element-loader-inner div.ui-elements-button-action a")[5].click()
        });
        
        this.lblPaymentInfo.waitForDisplayed(3000)
    }

    get btnBookNow() { return $('#book-now-spinnaker') }
    get lblAvailable() { return $('div.availability-tile') }
    get lblSoldOut() { return $$('div.availability-tile')[1] }
    selectAvailableDay(day) {
        const availableDays = $$('div.day div.has-availability span.calendar-date-text')
        for (let i = 0; i < availableDays.length; i++) {
            let availableDay = availableDays[i]
            if (availableDay.getText() === day) {
                availableDay.waitForClickable(3000)
                availableDay.click()
                break
            }
        }
    }
    selectAvailableTime(time) {
        const availableTimes = $$('a.time-option')
        for (let i = 0; i < availableTimes.length; i++) {
            let availableTime = availableTimes[i]
            if (availableTime.getText() === time) {
                availableTime.waitForClickable(3000)
                availableTime.click()
                break
            }
        }
    }
    get txtFirstName() { return $$('input.pro-form-textfield')[2] }
    get txtLastName() { return $$('input.pro-form-textfield')[3] }
    get txtPhone() { return $$('input.pro-form-textfield')[4] }
    get txtEmail() { return $$('input.pro-form-textfield')[5] }
    get btnAddTicket() { return $$('a.fancy-quantity-link span.fa-plus')[1] }
    get btnCloseModal() { return $("//div[@id='booking-flow-close']")}
    get bookNowModal() { return $('iframe#peek-embedded-frame')}
    get lblPaymentInfo() { return $$(".ui-theme-aqua-dreams .pod>.component-items-wrap>.ui-element-loader-shell.visible-element.first-sub-item")[0] }
}

export default new Activity();