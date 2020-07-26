# New doc extractor
print('''This script is for a device running Windows, with python installed. It requires the following modules:
-sys
-selenium/webdriver
-requests
-docx/Document
Make sure that you have these modules before beginning.
Do you have these modules installed? If not, you can check by going into your python folder, then running cmd, then using the pip install <module name> command to see if the module is intalled.''')
print('')
try:
    import sys
    from selenium import webdriver
    import requests
    from docx import Document
    print('''Extract things from a website using Firefox-inator''')
    print('')
    print('''This script will walk you through extracting text from a webpage using inspect element and copying its HTML "type" like XPATH, CSS Selector, etc.''')
    print('''(Right click on item > copy > whatever you want)''')
    print('''Then, it will produce a word document with the extracted data.''')
    def browserexit():
        try:
            browser.quit()
            sys.exit()
        except NameError:
            sys.exit()

    while True:
        print('''Which of the following are you going to use?
    -xpath
    -css selector
    -name
    -link text
    -partial link text
    -tag name
    -class name
    Type in the method you are going to use in all lower/upper case.''')
        option=input()
        if option=='quit' or option=='QUIT' or option=='Q' or option=='q':
            browserexit()
        elif option!='name' and option!='NAME' and option!='xpath' and option!='XPATH' and option!='link text' and option!='linktext' and option!='LINK TEXT' and option!='LINKTEXT' and option!='partial link text' and option!='PARTIAL LINK TEXT' and option!='partiallinktext' and option!='PARTIALLINKTEXT' and option!='tag name' and option!='TAG NAME' and option!='tagname' and option!='TAGNAME' and option!='class name' and option!='CLASS NAME' and option!='classname' and option!='CLASSNAME' and option!='css selector' and option!='CSS SELECTOR' and option!='cssselector' and option!='CSSSELECTOR':
            print('Invalid method')
        else:
            browser=webdriver.Firefox()
            doc=Document()
            print('''What is the URL that you are extracting data from?''')
            url=input()
            if url=='quit' or url=='QUIT' or url=='q' or url=='Q':
                browserexit()
            else:
                try:
                    res=requests.get(str(url))
                    isonline=res.status_code
                    str_isonline=str(isonline)
                    if str_isonline=='200':
                        browser.get(str(url))
                        print('''What is the '''+ option+''' you want to use?''')
                        name=input()
                        if option=='name' or option=='NAME':
                            elem=browser.find_elements_by_name(str(name))
                        elif option=='xpath' or option=='XPATH':
                            elem=browser.find_elements_by_xpath(str(name))
                        elif option=='link text' or option=='linktext' or option=='LINK TEXT' or option=='LINKTEXT':
                            elem=browser.find_elements_by_link_text(str(name))
                        elif option=='partial link text' or option=='PARTIAL LINK TEXT' or option=='partiallinktext' or option=='PARTIALLINKTEXT':
                            elem=browser.find_elements_by_partial_link_text(str(name))
                        elif option=='tag name' or option=='TAG NAME' or option=='tagname' or option=='TAGNAME':
                            elem=browser.find_elements_by_tag_name(str(name))
                        elif option=='class name' or option=='CLASS NAME' or option=='classname' or option=='CLASSNAME':
                            elem=browser.find_elements_by_class_name(str(name))
                        elif option=='css selector' or option=='CSS SELECTOR' or option=='cssselector' or option=='CSSSELECTOR':
                            elem=browser.find_elements_by_css_selector(str(name))
                        elif name=='quit' or name=='QUIT' or name=='q' or name=='Q':
                            browserexit()
                        else:
                            print('''Something went wrong. Please try again.''')
                    else:
                        print("Something went wrong (HTML error)!")
                    for items in elem:
                        print(items.text)
                        para=doc.add_paragraph(str(items.text))
                    print('''What do you want to save the document as?''')
                    docname=input()
                    if docname=='quit' or docname=='QUIT' or docname=='q' or docname=='Q':
                        browserexit()
                    else:
                        doc.save(str(docname) + '.docx')
                        browser.quit()
                except requests.exceptions.MissingSchema:
                    browser.quit()
                    print('''Something went wrong. Did you type in a URL correctly? (Copy-paste is recommended)''')
                    print('''MissingSchema(Error).''')
                except NameError:
                    browser.quit()
                    print('''Something went wrong. Did you type in a URL correctly? (Copy-paste is recommended)''')
                    print('''NameError.''')
                except ConnectionError:
                    browser.quit()
                    print('''Something went wrong. Did you type in a URL correctly? (Copy-paste is recommended)''')
                    print('''ConnectionError.''')
except ImportError:
    print('''It looks like there was an issue importing the modules.''')
    print('''Check to make sure that all the modules are installed in your python folder.''')
    sys.exit()
