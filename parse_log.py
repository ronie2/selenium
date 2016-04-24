def parse_log(log_file):
    '''Returns list of JSON like dicts from log file'''
    
    import re
    import json
    
    pattern = re.compile("\[{.*}\]")
    insp_array = []
    json_array = []
    #Appends strings with JSON obj to insp_array list
    with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    insp_array.append(re.search(pattern, line).group())
                except:
                    pass
    
    #Try to decode and append JSON obj to json_array list
    for arr in insp_array:
        try:
            json_array.append(json.loads(arr))
        except:
            pass
    
    return json_array