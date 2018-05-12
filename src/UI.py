#Import libraries
from ipywidgets import *
from IPython.display import display

from Users import User
from Registrar import Registrar

#Define Widgets.

# Search bar text
search_bar = widgets.Text(
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

# This will maybe be created programatically eventually
# Filled in with title/description and clickable image from db
deal_texts = [widgets.Label('Deal' + str(i)) for i in range(6)]
deal_go_buttons = [widgets.Button(description='Go') for i in range(6)]


col1 = widgets.VBox([deal_texts[0], deal_go_buttons[0], deal_texts[1], deal_go_buttons[1]])
col2 = widgets.VBox([deal_texts[2], deal_go_buttons[2], deal_texts[3], deal_go_buttons[3]])
col3 = widgets.VBox([deal_texts[4], deal_go_buttons[4], deal_texts[5], deal_go_buttons[5]])

deals_boxed = widgets.HBox([col1, col2, col3])

# Search bar and button horizontally next to each other
search_component = widgets.HBox([search_bar, search_button])

# Vertically arrange welcome banner, search component, and deal grid to create welcome page
welcome_page = widgets.VBox([welcome_banner, search_component, deals_boxed])

# Tab component
pages = widgets.Tab()

# Set what widget is shown on each page. To start, only show welcome page.
pages.children = [welcome_page]

# Set name of tabs
tab_contents = ['Home', 'Search Result', 'Deal Details']
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
    
    # Switch to search result page
    pages.selected_index = 1

# Query handlers
search_button.on_click(run_deal_search_query)

for go_button in deal_go_buttons:
    go_button.on_click(run_deal_search_query)