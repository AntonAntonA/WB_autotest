

def utest_add_item_to_basket(app):
    item_name = 'Doom'
    main_page = app.main_page

    search_results_page = main_page.search_item(item_name)
    item = search_results_page.get_item(1)

    item_page = item.go_to_item_page()
    item_page.add_to_basket()
    print('URL:', item_page.get_URL())



