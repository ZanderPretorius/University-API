def check_country_name(cd_name):
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

    elif c_name == "uk" or c_name == "england" or c_name == "wales" or c_name == "scotland" or c_name=="the united kingdom" or c_name=="northern ireland":
        res_name = "united kingdom"

    else:
        res_name = c_name

    return (res_name)


# checker = check_country_name("ussr")

# print(checker)
