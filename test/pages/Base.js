class Base {
    open(path) {
        browser.url(path);
        return this;
    }
}

export default Base;