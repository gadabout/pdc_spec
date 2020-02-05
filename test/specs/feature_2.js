import Home from '../pages/Home'

describe('As a consumer visiting Peek.com I would like to take a personality quiz to cater search results to my preferences', () => {

    before(() => {
        browser.maximizeWindow()
        Home.open()
    })

    it('When completed, the quiz should provide a search form - when I search I should see my classification listed at the top of my search results', () => {
        Home.hdrQuiz.scrollIntoView()
        const result = Home.completeQuiz();
        expect(["A Nature Lover", "An Explorer", "An Insider", "A Culture Seeker", "A Foodie"]).to.include(result)
    })
})