

def get_values(args: tuple) -> str:
    """This is an only function that is able to accessed from
    another functions. This means it is a 'module' function.

    This function returns a string value which this had made requests
    to mutationtaster website an got response then parsed it.

    Future Plan -- This function can parse and return the value what
    the user wants.
    """

    unparsed_html = _get_all_response(args)
    summary_info = _parse_to_summary(unparsed_html)
    
    return summary_info

def get_file_name():
    return "mtresponse{}.html".format()

def get_file(mode: str):
    f = open("mtresponse.html", mode)
    return f

def _get_all_response(args: tuple) -> None:
    """This edits the post message and sends it. Then
    gets all html value and writes all html to a file via
    write_file func. 
    """

    import get_response

                   
    post_values = {"gene": args[0],
                   "transcript_stable_id_text": args[1],
                   "sequence_type": args[2],
                   "sequence_snippet": args[3],
                   "position_be": args[4],
                   "new_base": args[5],
                   "start_insdel": args[6],
                   "end_insdel": args[7],
                   "bases_inserted": args[8]}
    

    url = "http://www.mutationtaster.org/cgi-bin/MutationTaster/MutationTaster69.cgi"
    response = get_response.get_response(url, post_values)

    return response.text
    
    #file = get_file("w")
    #file.write(response.text)
    #file.close()

    

def _parse_to_summary(unparsed:str)-> str:
    """
    This function parses whole html for just summary part.
    
    This gets the html text from the html file which "_get_all_response"
    function has writen.
    """
    # unparsed_file = get_file("r")
    import bs4

    soup = bs4.BeautifulSoup(unparsed, "html.parser")
    # unparsed_file.close()

    # table = soup.find("table").find_next_sibling()
    # row = table.find("tr").find_next_sibling()
    # summary = row.find("ul")

    summary = soup.find("ul").get_text()
    return summary
    
    
if __name__ == "__main__":
    t = ("", "ENST00000379370", "gDNA", "", "",
         "", "28669", "28672", "")
    print(get_values(t))


    
