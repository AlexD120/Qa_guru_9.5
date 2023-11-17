from selene import browser, have, be

def test_complete_todo():
    browser.config.base_url("https://todomvc.com/examples/emberjs/")
    browser.open('/')
    browser.element()

    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').should(have.size(3)) #ПрОВЕРКА ЧТО СОЗДАЛОСЬ 3 ЗАДАЧИ
