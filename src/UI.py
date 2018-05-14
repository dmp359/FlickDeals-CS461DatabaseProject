#Import libraries
from ipywidgets import *
from IPython.display import display

from User import User
from QueryManager import QueryManager
from Deal import Deal
from Business import Business

# Quieries required on load of app

# Given a list of business tuples, convert the data into html results grid
# @param businesses - a deals tuple response from a query
def getBusinessResultFromTuple(businesses):
    names = [i[0] for i in businesses]
    imageURLs = [i[1] for i in businesses]
    homepageURLs = [i[2] for i in businesses]

    result_page_html = ''
    for i in range(len(names)):
        result_page_html += '''
            <div class="grid-container">
                <div class="grid-item"> <a href="{homepageURL}" target="_blank">{name}</a></div>
                <div class="grid-item">
                    <img src="{imageURLs}" height=50 width=50>
                </div>
            </div>
        '''.format(homepageURL=homepageURLs[i],
                name=names[i],
                imageURLs=imageURLs[i],
                )
    return result_page_html

def run_business_all_query():
    man = QueryManager()
    res = man.openDBConnectionWithBundle("PgBundle.properties")

    # Businesses is a list of tuples in the form of
    # (name, imageURL, homepageURL)
    businesses = man.getAllRetailers()
    if (len(businesses) < 1):
        return '<div class="grid-item"> Error connecting to database. Try again soon.></div>'
    result_page_html = getBusinessResultFromTuple(businesses)
    return result_page_html



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
see_all_button = widgets.Button(description="Browse All")

# Search bar and buttons horizontally next to each other
search_component = widgets.HBox([search_bar, search_button, see_all_button])

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

business_html = widgets.HTML(value = run_business_all_query())
business_view = widgets.VBox([business_banner, business_html])

# Filled in with title/description and image from db
deal_title = [widgets.Label('Deal Title ' + str(i)) for i in range(6)]
deal_descriptions = [widgets.Label('This is a great deal. $50 off ' + str((i+1) * 100)) for i in range(6)]
rating_slider = widgets.IntSlider(
    value=5,
    min=1,
    max=5,
    step=1,
    description='Rate:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
# Rating/favorites
rating_sliders = [rating_slider for i in range(6)]
deal_button_controls = [widgets.HBox(
    [widgets.Button(description='Submit Rating'),
     widgets.Button(description='Favorite Deal')]) for i in range(6)]

# Create a dictionary of each button to associated index of deal to rate.
# Used by rate/favorite deals callback
rating_button_dict = {}
favorite_button_dict = {}
for i in range(len(deal_button_controls)):
    rating_button_dict[deal_button_controls[i].children[0]] = i
    favorite_button_dict[deal_button_controls[i].children[1]] = i

deal_detail_cols = [widgets.VBox([deal_descriptions[i], rating_sliders[i],
                    deal_button_controls[i]]) for i in range(6)]

# "See details" accordions. Children are descriptions of each deal
see_details_accordions = [widgets.Accordion(children=[deal_detail_cols[i]]) for i in range(6)]
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

# Vertically arrange welcome banner, search component, and deal grid to create welcome page
welcome_page = widgets.VBox([welcome_banner, search_component, deals_boxed])

# Tab component
pages = widgets.Tab()

# Set what widget is shown on each page on launch
pages.children = [welcome_page, business_view]

# Set name of tabs
tab_contents = ['Home', 'Businesses', 'Search Results']
for i in range(len(tab_contents)):
    pages.set_title(i, str(tab_contents[i])) 

# Display tab component which holds all widgets
# Main
def launch():
    display(pages)


# Given a list of deals tuples, convert the data into html results grid
# Used to avoid a lot of duplicate code between search and browse all
# @param deals - a deals tuple response from a query
def getDealResultFromTuple(deals):
    titles = [i[0] for i in deals]
    descriptions = [i[1] for i in deals]
    avgRatings = [i[2] for i in deals]
    imageUrls = [i[3] for i in deals]
    startDates = [i[4] for i in deals]
    endDates = [i[5] for i in deals]
    result_page_html = ''
    for i in range(len(titles)):
        result_page_html += '''
            <div class="grid-container">
                <div class="grid-item">{i}</div>
                <div class="grid-item">{title}</div>
                <div class="grid-item">{description}</div>
                <div class="grid-item">
                    <img src="{imgUrl}" height=100 width=100>
                </div>
                <div class="grid-item">Rating = {rating}/5.0</div>
                <div class="grid-item">Valid from {startDate} to {endDate}</div>
            </div>
            <br>
        '''.format(i=i,
                   title=titles[i],
                   description=descriptions[i],
                   rating=avgRatings[i],
                   imgUrl=imageUrls[i],
                   startDate=startDates[i],
                   endDate=endDates[i]
                  )

    slider = widgets.IntSlider(
            value=5,
            min=1,
            max=5,
            step=1,
            description='Rate:',
            disabled=False,
            continuous_update=False,
            orientation='horizontal',
            readout=True,
            readout_format='d'
            )

    # Search bar text
    deal_text_input = widgets.Text(
        value='',
        placeholder='Deal Number',
        description='Deal #:',
        disabled=False,
    )
    rate_button_general = widgets.Button(description="Rate")
    rate_button_general.on_click(run_rate_query) #TODO: Make this a different function to check general slider
    rating_box = widgets.HBox([slider, deal_text_input,rate_button_general])
    res_html_widget = widgets.HTML(value=result_page_html)
    result_page = widgets.VBox([res_html_widget,rating_box])
    
    return result_page


''' Click functions ----------------------------------------------'''
def run_deal_all_query(sender):
    man = QueryManager()
    res = man.openDBConnectionWithBundle("PgBundle.properties")
    deals = man.getAllDeals()
    if (len(deals) < 1): # Shouldn't ever happen unless an eror occurs
        print("Error connecting to database. Try again soon.")
        return 

    result_page = getDealResultFromTuple(deals)
    # Last tab should be search results and replaced if it already is
    l = list(pages.children)
    if len(pages.children) < 3:
        l.append(result_page)
    else:
        l[len(pages.children) - 1] = result_page # Overrite search result page
    
    pages.children = tuple(l)
    # Switch to search result page
    pages.selected_index = len(pages.children) - 1

def run_deal_search_query(sender):
    if (search_bar.value == ''):
        return
    man = QueryManager()
    res = man.openDBConnectionWithBundle("PgBundle.properties")

    # Deals is a list of tuples in the form of
    # (title, description, avgRating, imageURL, startDate, endDate)
    deals = man.searchForDeal(search_bar.value)
    # Result page of search. Create html grid for each deal
    result_page_html = ''
    if (len(deals) < 1): # If nothing matches search
        result_page_html = '''
            <div class="grid-item">No deals found having title "{val}"</div>
        '''.format(val=search_bar.value)
        result_page = widgets.HTML(value=result_page_html)
    else:
        result_page = getDealResultFromTuple(deals)

    # Last tab should be search results and replaced if it already is
    l = list(pages.children)
    if len(pages.children) < 3:
        l.append(result_page)
    else:
        l[len(pages.children) - 1] = result_page
    
    pages.children = tuple(l)

    # Switch to search result page
    pages.selected_index = 2


def run_favorite_query(sender):
    deal_index = favorite_button_dict[sender] # lookup in dict for which button was clicked
    print('You chose to favorite deal number ' + str(deal_index))
    man = QueryManager()
    res = man.openDBConnectionWithBundle("PgBundle.properties")
    print(res)

def run_rate_query(sender):
    deal_index = rating_button_dict[sender] # lookup in dict for which button was clicked
    print('You chose to rate deal number ' + str(deal_index) + ' with a value of ' + str(rating_sliders[deal_index].value))
    man = QueryManager()
    res = man.openDBConnectionWithBundle("PgBundle.properties")
    print(res)
    # TODO: Update tables appropriately to rate


''' Button handlers ----------------------------------------------'''
search_button.on_click(run_deal_search_query)
see_all_button.on_click(run_deal_all_query)
for i in range(len(deal_button_controls)):
    deal_button_controls[i].children[0].on_click(run_rate_query)
    deal_button_controls[i].children[1].on_click(run_favorite_query)
