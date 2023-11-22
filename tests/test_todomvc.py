import pytest
from selene import browser, have, be


def test_complete_todo():
    browser.open('/')
    browser.element('#new-todo').should(be.blank)


    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.all('#todo-list>li').with_(timeout=2).should(have.size(3)) #ПрОВЕРКА ЧТО СОЗДАЛОСЬ 3 ЗАДАЧИ

    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c')) #ПРОВЕРИТЬ ВСЕ ЗНАЧЕНИЯ
#    browser.all('#todo-list>li').second.element('.toggle').click() #КЛИКНУТЬ ПО " ЭЛЕМЕНТУ
    browser.all('#todo-list>li').element_by(have.exact_text('b')).element('.toggle').click() # 2 ВАРИАНТ НАПИСАНИЯ
#    browser.element('.toggle').click() # 3 ВАРИАНТ НАПИСАНИЯ
    browser.all('#todo-list>li').by(have.css_class('.completed')).should(have.exact_texts('b')) # НАХОДИТ ВСЕ ЭЛЕМЕНТЫ И ПРОВЕРЯЕТ ЧТО В СПИСКЕ ТОЛЬКО С ТАКИМ ТЕКСТОМ
    browser.all('#todo-list>li').by(have.no.css_class('.completed')).should(have.exact_texts('a', 'c')) # ПРОВЕРЯЕТ ЧТО ОСТАЛЬНЫЕ ЭЛЕМЕНТЫ НЕ НАХОДЯТСЯ ПОД ЭТИМ КЛАССОМ И ИМЕЮТ ТЕКСТ А И С


