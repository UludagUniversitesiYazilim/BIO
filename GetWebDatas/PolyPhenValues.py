def get_values(args: tuple) -> str:
    """This is an only function that is able to accessed from
    another functions. This means it is a 'module' function.

    This function returns a string value which this had made requests
    to mutationtaster website an got response then parsed it.

    Future Plan -- This function can parse and return the value what
    the user wants.
    """

    resp = _get_all_response(args)
    summary_info = _parse_to_summary(resp)
    
    return summary_info

def get_file(mode: str):
    f = open("ppresponse.html", mode)
    return f
        
def _get_all_response(args: tuple) -> None:
    """This edits the post message and sends it. Then
    gets all html value and writes all html to a file via
    write_file func. 
    """

    import get_response, bs4, requests

    url = "http://genetics.bwh.harvard.edu/cgi-bin/ggi/ggi2.cgi"

    post_values = {
        "_ggi_project" : "PPHWeb2", 
        "_ggi_origin": "query",
        "_ggi_target_submit": "submit",
        "accid" : args[0],
        "seqres": args[1],
        "seqpos" : args[2],
        "seqvar1" : args[3],
        "seqvar2" : args[4],
        #"description":args[5]
    }
        
    
    response = get_response.get_response(url, post_values)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    sid = soup.find("input").get("value")

    link = _get_link(sid)

    s  = requests.session()
    response = s.post(link)

    
    """file = get_file("w")
    file.write(response.text)
    file.close()"""
    
    return response.text
    
def _refresh(sid: str):
    import bs4, requests

    url = "http://genetics.bwh.harvard.edu/cgi-bin/ggi/ggi2.cgi"
    data = {"sid" : sid,
        "sidreset" : "1",
        "delpend" : "4948667",
        "_ggi_project" : "PPHWeb2",
        "_ggi_origin" : "manage",
        "_ggi_target_manage" : "Refresh"
    }


    session = requests.session()
    r = session.post(url, verify=0, data = data)

    return r

def _get_link(sid: str):
    import bs4, time

    response = _refresh(sid)
    i = 0
    
    while (i < 5):
        link = bs4.BeautifulSoup(response.text, 'html.parser').find_all("a")[-2].get("href")
        if  link[0] == '/':
            return "http://genetics.bwh.harvard.edu" + link
        else :
            response = _refresh(sid)
            time.sleep(1)
        i += 1

def _parse_to_summary(unparsed)-> str:
    """
    This function parses whole html for just summary part.
    
    This gets the html text from the html file which "_get_all_response"
    function has writen.
    """
    #unparsed_file = get_file("r")
    import bs4

    soup = bs4.BeautifulSoup(unparsed, "html.parser")
    #unparsed_file.close()

    # table = soup.find("table").find_next_sibling()
    # row = table.find("tr").find_next_sibling()
    # summary = row.find("ul")

    summary = soup.find("table")
    summary = summary.find("tr").find_next_sibling()
    summary = summary.find_all("td")[-1].get_text()
    return summary
    
    
if __name__ == "__main__":
    t = ("P41567", '', '59', 'L', 'P', '')
    print(get_values(t))
