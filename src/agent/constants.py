"""Set of constants."""
DEFAULT_CANDIDATE_COUNT = 1
DEFAULT_TEMPERATURE = 1.
DEFAULT_TOP_K = 20
DEFAULT_TOP_P = 0.8
DEFAULT_NUM_OUTPUTS = 5096  # tokens

keywords = ["heineken", "tiger", "biaviet", "larue", "bivina",
            "edelweiss", "bialacviet", "strongbow", "biasaigon"]

PREDEFINED_CLASS = """
heineken_logo
tiger_logo
biaviet_logo
larue_logo
bivina_logo
edelweiss_logo
bialacviet_logo
strongbow_logo
biasaigon_logo
heineken_boxes
tiger_boxes
biaviet_boxes
larue_boxes
bivina_boxes
edelweiss_boxes
bialacviet_boxes
strongbow_boxes
biasaigon_boxes
heineken_poster
heineken_banner
heineken_billboard
heineken_table_tent
heineken_digital_screen
heineken_standee
tiger_poster
tiger_banner
tiger_billboard
tiger_table_tent
tiger_digital_screen
tiger_standee
biaviet_poster
biaviet_banner
biaviet_billboard
biaviet_table_tent
biaviet_digital_screen
biaviet_standee
larue_poster
larue_banner
larue_billboard
larue_table_tent
larue_digital_screen
larue_standee
bivina_poster
bivina_banner
bivina_billboard
bivina_table_tent
bivina_digital_screen
bivina_standee
edelweiss_poster
edelweiss_banner
edelweiss_billboard
edelweiss_table_tent
edelweiss_digital_screen
edelweiss_standee
bialacviet_poster
bialacviet_banner
bialacviet_billboard
bialacviet_table_tent
bialacviet_digital_screen
bialacviet_standee
strongbow_poster
strongbow_banner
strongbow_billboard
strongbow_table_tent
strongbow_digital_screen
strongbow_standee
biasaigon_poster
biasaigon_banner
biasaigon_billboard
biasaigon_table_tent
biasaigon_digital_screen
biasaigon_standee
heineken_beer_keg
heineken_beer_bottle
heineken_beer_can
heineken_special_edition_package
tiger_beer_keg
tiger_beer_bottle
tiger_beer_can
tiger_special_edition_package
biaviet_beer_keg
biaviet_beer_bottle
biaviet_beer_can
biaviet_special_edition_package
larue_beer_keg
larue_beer_bottle
larue_beer_can
larue_special_edition_package
bivina_beer_keg
bivina_beer_bottle
bivina_beer_can
bivina_special_edition_package
edelweiss_beer_keg
edelweiss_beer_bottle
edelweiss_beer_can
edelweiss_special_edition_package
bialacviet_beer_keg
bialacviet_beer_bottle
bialacviet_beer_can
bialacviet_special_edition_package
strongbow_beer_keg
strongbow_beer_bottle
strongbow_beer_can
strongbow_special_edition_package
biasaigon_beer_keg
biasaigon_beer_bottle
biasaigon_beer_can
biasaigon_special_edition_package
person
"""

PREDEFINED_CLASSES_BY_GROUP = {
    "in the outdoor_venue": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer carton", "Beer bottle", "Beer can"
    ],
    "People are shopping": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer carton", "Beer bottle", "Beer can", "Buyer/Customer",
    ],
    "in the bar or the pub or the night_club": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer carton", "Beer crate", "Beer bottle", "Beer can",
        "Drinker", "Promotion Girl", "Seller", "Buyer/Customer",
        "Eating", "Drinking", "Smiling", "Talking", "Shopping",
        "Happy", "Angry", "Enjoyable", "Relaxed", "Neutral",
        "Ice bucket", "Ice box", "Fridge", "Signage, billboard, poster, standee", "Tent card, display stand, tabletop", "Parasol"
    ],
    "in the restaurant": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer crate", "Beer bottle", "Beer can",
        "Drinker", "Promotion Girl", "Seller", "Buyer/Customer",
        "Eating", "Drinking", "Smiling", "Talking", "Shopping",
        "Happy", "Angry", "Enjoyable", "Relaxed", "Neutral",
        "Fridge", "Signage, billboard, poster, standee"
    ],
    "in the store": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer carton", "Beer crate", "Beer bottle", "Beer can", "Fridge"
    ],
    "in the big supermarket": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer carton", "Beer crate", "Beer bottle", "Beer can", "Fridge"
    ],
    "A display counter": ["Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
                          "Beer carton", "Beer bottle", "Beer can"],
    "A party or the celebration": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer crate", "Beer bottle", "Beer can",
        "Drinker", "Promotion Girl", "Seller", "Buyer/Customer",
        "Eating", "Drinking", "Smiling", "Talking", "Shopping",
        "Happy", "Angry", "Enjoyable", "Relaxed", "Neutral",
        "Fridge", "Signage, billboard, poster, standee"
    ],
    "A gathering": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer crate", "Beer bottle", "Beer can",
        "Drinker", "Promotion Girl", "Seller", "Buyer/Customer",
        "Eating", "Drinking", "Smiling", "Talking", "Shopping",
        "Happy", "Angry", "Enjoyable", "Relaxed", "Neutral",
        "Fridge", "Signage, billboard, poster, standee"
    ],
    "A happy hour, or a fun time": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer crate", "Beer bottle", "Beer can",
        "Drinker", "Promotion Girl", "Seller", "Buyer/Customer",
        "Eating", "Drinking", "Smiling", "Talking", "Shopping",
        "Happy", "Angry", "Enjoyable", "Relaxed", "Neutral",
        "Fridge", "Signage, billboard, poster, standee"
    ],
    "There are some beer carton": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Beer carton", "Beer crate", "Beer bottle", "Beer can", "Fridge"
    ],
    "There are some Promotional Material: Signage, billboard, poster, standee ": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Fridge", "Signage, billboard, poster, standee"
    ],
    "People is taking photo": [
        "Heineken logo", "Tiger logo", "Bia Viet logo", "Larue logo", "Bivina logo", "Edelweiss logo", "Strongbow logo",
        "Fridge", "Signage, billboard, poster, standee"
    ],

}

FOCUSED_CRITERIA = """
Criteria:
1. Brand Logos: Identify any brand logos mentioned in the description or OCR results.
2. Products: Mention any products such as beer kegs and bottles.
3. Customers: Describe the number of customers, their activities, and emotions.
4. Promotional Materials: Identify any posters, banners, and billboards.
5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket).
"""

CONTEXT = ["in the outdoor_venue",
           "People are shopping",
           "in the bar or the pub or the night_club",
           "in the restaurant",
           "in the store",
           "in the big supermarket",
           "A display counter",
           "A party or the celebration",
           "A gathering",
           "A happy hour, or a fun time",
           "There are some beer carton",
           "There are some Promotional Material: Signage, billboard, poster, standee ",
           "People is taking photo"]
