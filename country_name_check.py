def check_country_name(cd_name):

    us_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi",
                 "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

    res_name = ""
    c_name = cd_name.lower()
    if c_name == "usa":
        res_name = "united states"

    elif c_name == "burma":
        res_name = "myanmar"

    elif c_name == "ussr" or c_name == "russia":
        res_name = "russian federation"

    elif c_name == "the netherlands":
        res_name = "netherlands"

    elif c_name == "uk" or c_name == "england" or c_name == "wales" or c_name == "scotland" or c_name == "the united kingdom" or c_name == "northern ireland":
        res_name = "united kingdom"

    elif c_name == "somaliland":
        res_name = "somalia"

    elif c_name == "eswatini":
        res_name = "swaziland"

    elif c_name == "kingdom of saudi arabia":
        res_name = "saudi arabia"

    elif c_name.title() in us_states:
        res_name = "united states"
    else:
        res_name = c_name

    return (res_name)


# checker = check_country_name("ussr")

# print(checker)
