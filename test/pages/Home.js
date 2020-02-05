import Base from './Base';

class Home extends Base {
    open() {
        super.open('/');        
        return this;
    }

    openTopPickBy(name) {
        $("//img[@alt=\"" + name + "\"]").scrollIntoView()
        $("//img[@alt=\"" + name + "\"]").waitForDisplayed(3000)
        $("//img[@alt=\"" + name + "\"]").click()
    }

    enterLocation(destination) {
        destination.split("").forEach(char => this.txtLocationSearch.addValue(char))
        browser.pause(3500)
        this.txtLocationSearch.addValue("\uE015" + "\uE004");
        this.txtLocationSearch.click()
    }

    submit() {
        browser.pause(3000)
        this.btnLocationSearch.click()
    }

    setFromDateInCalendar(day, month, year) {
        this.btnFromCalendar.waitForExist(5000)
        this.btnFromCalendar.waitForClickable(5000)
        this.btnFromCalendar.click()
        this.setMonth(month)
        this.setYear(year)
        this.setDay(day)
    }

    setToDateInCalendar(day, month, year) {
        this.btnToCalendar.waitForExist(5000)
        this.btnToCalendar.waitForClickable(5000)
        this.btnToCalendar.click()
        this.setDay(day)

        this.btnToCalendar.waitForClickable(5000)
        this.btnToCalendar.click()
        this.setMonth(month)
        this.setYear(year)
        this.setDay(day)
    }

    setYear(year) {
        this.txtCalYear.waitForExist(5000)
        this.txtCalYear.clearValue()
        this.txtCalYear.addValue(year)
    }

    setMonth(month) {
        this.currMonth.waitForExist(5000)
        var currMonth = this.currMonth.getText()
        while (month !== currMonth) {
            this.btnNextMonth.click()
            currMonth = this.currMonth.getText()
        }
    }

    setDay(target) {
        this.desiredDay(target).click()
    }

    completeQuiz() {
        var isSelectImgDisplayed = this.hdrSelectImg.isDisplayed()
        var imgElements = $$("//img[@alt='quiz image']")
        while (isSelectImgDisplayed) {
            imgElements[0].click()
            isSelectImgDisplayed = this.hdrSelectImg.isDisplayed()
        }
        this.hdrQuizResults.waitForDisplayed(5000)
        return this.hdrQuizResults.getText()
    }

    enterQuizLocation(destination) {
        destination.split("").forEach(char => this.txtQuizLocationSearch.addValue(char))
        this.btnQuizLocationSearch.click()
    }

    get txtLocationSearch() { return $('#homepage_location_search') }
    get btnLocationSearch() { return $("[name='Location Search Submit']") }
    get btnFromCalendar() { return $("#location-search-from-date") }
    get btnToCalendar() { return $("#location-search-to-date") }
    get txtCalYear() { return $("//input[@class='numInput cur-year']")}
    get currMonth() { return $("//span[@class='cur-month']") }
    get btnNextMonth() { return $("//span[@class='flatpickr-next-month']")}
    get btnPrevMonth() { return $("//span[@class='flatpickr-prev-month']") }
    desiredDay(day) { return $("//div[@class='flatpickr-days']//span[text()='"+day+"'][1]") }
    get hdrQuiz() { return $("//h2[contains(text(),'Discover Your Adventure Personality')]") }
    get hdrSelectImg() { return $("//h4[contains(text(),'Select An Image')]")}
    get txtQuizLocationSearch() { return $('#personality_quiz_location_search') }
    get btnQuizLocationSearch() { return $("(//input[@name='Location Search Submit'])[2]") }
    get hdrQuizResults() { return $("//span[@class='personality-result-name']") }
}

export default new Home();