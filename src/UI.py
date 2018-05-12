#Import libraries
from ipywidgets import *
from IPython.display import display

from Users import User
from Registrar import Registrar


#Define Widgets.
search_bar = widgets.Text(
    placeholder='Search',
    description='Find Deal:',
    disabled=False,display='flex'
)

search_button = widgets.Button(description="Search",display='flex'
)

# This list will be created programatically eventually
# Filled in with title/description and clickable image from db
deal_HTML_items = [
    '<div class="grid-item">Deal description 1</div>',
    '<div class="grid-item">Deal description 2</div>',
    '<div class="grid-item">Deal description 3</div>',
    '<div class="grid-item">Deal description 4</div>',
    '<div class="grid-item">Deal description 5</div>',
    '<div class="grid-item">Deal description 6</div>',
]

welcome_banner = widgets.HTML(
    value='''
        <link rel="stylesheet" href="styles.css">
        Hi and welcome to <b>Flick Deals</b>
        <img src="http://images.clipartpanda.com/money-clipart-money-pics-free.png" height=50 width = 50>
        <h1> Check out today's hottest deals! </h1>
    ''',
)

gridItems = ''.join(deal_HTML_items)
deal_grid = widgets.HTML(
    value='''
        <div class="grid-container">
            {gridItems}
        </div>
    '''.format(gridItems=gridItems)
)
# Search bar and button horizontally next to each other
search_component = widgets.HBox([search_bar, search_button])

# Vertically arrange welcome banner, search component, and deal grid to create welcome page
welcome_page = widgets.VBox([welcome_banner, search_component, deal_grid])



# Tab component
pages = widgets.Tab()

 # Set what widget is shown on each page
pages.children = [welcome_page]

# Set name of tabs
tab_contents = ['Home', 'Search Result']
for i in range(len(tab_contents)):
    pages.set_title(i, str(tab_contents[i])) 

# Display tab component which holds all widgets
def displayWelcomePage():
    display(pages)

# Click Function
def run_deal_search_query(sender):
    reg = Registrar()
    response = reg.openDBConnectionWithBundle("PgBundle.properties")

    # Example result page based on search result
    pages.children = [welcome_page, widgets.HTML(
        value='''
            <div class="grid-container">
                <div class="grid-item">{response}</div>
            </div>
        '''.format(response=response),
    )]
    
    pages.selected_index = 1

# Query handlers
search_button.on_click(run_deal_search_query)
