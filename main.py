if __name__ == '__main__':
    from test1 import test1
    from test2 import test2
    from test3 import test3
    from test4 import test4
    from test5 import test5
    from test6 import test6
    from excel_utils import Excel_utils

    data_sheet = 'C:/Users/dpenn/Desktop/Projects/Resolver/resolver.xlsx'
    data_in = Excel_utils(data_sheet, 'main', 'in')
    url = data_in.sht.cell(1,1).value # Get the URL of the test site
    test1(url,data_sheet)
    test2(url,data_sheet)
    test3(url,data_sheet)
    test4(url,data_sheet)
    test5(url,data_sheet)
    test6(url,data_sheet)
