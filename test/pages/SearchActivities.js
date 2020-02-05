import Base from './Base';

class SearchActivities extends Base {
    open() {
        super.open('/search?lat=40.690&lng=-74.0083&place=New%20York&startDate=&endDate=')
        return this;
    }

    sortBy(target) {
        this.btnSortBy.click()
        $('=' + target).waitForClickable(5000)
        $('='+target).click()
        browser.pause(1500)
    }

    filterBy(target) {
        this.btnFilterBy.click()
        $('(//input[@name="'+target+'"])[2]').waitForClickable(5000)
        $('(//input[@name="'+target+'"])[2]').click()
        browser.pause(1500)
    }

    get btnSortBy() { return $("//div[@class='containers-Search-styles---sideNav']//div[@class='containers-Search-styles---sortBar']") }
    get btnFilterBy() { return $("//div[@class='containers-Search-styles---sideNav']//div[@class='containers-Search-styles---filterSortByInline']") }
    get locationHeader() { return $("//strong") }
}

export default new SearchActivities();