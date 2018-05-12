#Import libraries
from ipywidgets import *
from IPython.display import display

from Users import User
from QueryManager import QueryManager
from Deals import Deal

#Define Widgets----

# Search bar text
search_bar = widgets.Text(
    value='',
    placeholder='Search',
    description='Find Deal:',
    disabled=False,
)

# Search bar button
search_button = widgets.Button(description="Search")

# Welcome banner and picture
welcome_banner = widgets.HTML(
    value='''
        <link rel="stylesheet" href="styles.css">
        Hi and welcome to <b>Flick Deals</b>
        <img src="http://images.clipartpanda.com/money-clipart-money-pics-free.png" height=50 width = 50>
        <h1> Check out today's hottest deals! </h1>
    ''',
)

# Business banner and picture
business_banner = widgets.HTML(
    value='''
        <link rel="stylesheet" href="styles.css">
        Check out <b>top retailers</b>! 
        <img src="https://openclipart.org/download/279010/Simple-Isometric-Store.svg" height=50 width = 50>
    ''',
)

# This will maybe be created programatically eventually
# Filled in with title/description and image from db
deal_title = [widgets.Label('Deal Title ' + str(i)) for i in range(6)]

# TODO: Query database
deal_descrptions = [widgets.Label('This is a great deal. $50 off ' + str((i+1) * 100)) for i in range(6)]

# "See details" accordions. Children are descriptions of each deal and should be created all at once at start (not on click)
see_details_accordions = [widgets.Accordion(children=[deal_descrptions[i]]) for i in range(6)]
for i in range(len(see_details_accordions)):
    see_details_accordions[i].selected_index = None # Collapse accordions
    see_details_accordions[i].set_title(0, 'See details')

# Format into 3 columns of 2 widgets, vertically set on top of each other to create a grid like
'''
Deal Deal Deal
Deal Deal Deal
'''
col1 = widgets.VBox([deal_title[0], see_details_accordions[0], deal_title[1], see_details_accordions[1]])
col2 = widgets.VBox([deal_title[2], see_details_accordions[2], deal_title[3], see_details_accordions[3]])
col3 = widgets.VBox([deal_title[4], see_details_accordions[4], deal_title[5], see_details_accordions[5]])
deals_boxed = widgets.HBox([col1, col2, col3])

# Search bar and button horizontally next to each other
search_component = widgets.HBox([search_bar, search_button])

# Vertically arrange welcome banner, search component, and deal grid to create welcome page
welcome_page = widgets.VBox([welcome_banner, search_component, deals_boxed])

# Tab component
pages = widgets.Tab()

# Set what widget is shown on each page on launch
pages.children = [welcome_page, business_banner]

# Set name of tabs
tab_contents = ['Home', 'Businesses', 'Search Results']
for i in range(len(tab_contents)):
    pages.set_title(i, str(tab_contents[i])) 

# Display tab component which holds all widgets
def displayWelcomePage():
    display(pages)

# Click Function
def run_deal_search_query(sender):
    man = QueryManager()
    res = man.openDBConnectionWithBundle("PgBundle.properties")

    # Example result page based on search result
    # TODO: Select deal where deal name = search bar value
    #deal_searched = Deal(name=search_bar.value)
    deals = man.searchForDeal()
    result_page = widgets.HTML(
        value='''
            <div class="grid-container">
                <div class="grid-item">{deals}</div>
            </div>
        '''.format(deals=deals),
    )

    # Last tab should be search results and replaced if it already is
    l = list(pages.children)
    if len(pages.children) < 3:
        l.append(result_page)
    else:
        l[len(pages.children) - 1] = result_page
    
    pages.children = tuple(l)

    # Switch to search result page
    pages.selected_index = 2

# Query handlers
search_button.on_click(run_deal_search_query)
