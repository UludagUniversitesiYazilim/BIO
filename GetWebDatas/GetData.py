import threading




def _get_data(site: str, data: tuple) -> str:

    """A communication function. The user can get datas
    from this function.
    
    """

    if site == 'mutationtaster':
        import MuTasterValues as MT
        return MT.get_values(data)
    elif site == 'polyphen':
        import PolyPhenValues as PP
        return PP.get_values(data)
    else:
        print("girilmedi")
        
        
class Response(threading.Thread):
    """A real result thread and class. This class includes
    a file query result that you give as filequery. And a file
    query results means:
        -> Response from remote website (polyphen, mutationtater, etc. )
        -> Name of a person
        -> Site name which you send reauest for result.
    """
    def __init__(self, filequery):
        """ Initializing from filequery"""
        
        threading.Thread.__init__(self)
        self.name = filequery[1]
        self.site = filequery[0]
        self._webquery = filequery[2]
        self.state = False
        
    @property
    def state(self):
        return self._state
    
    @property    
    def response(self):
        return self._response
        
    @response.setter
    def response(self, value):
        self._response = value
    
    @state.setter
    def state(self, state):
        self._state = state
       
    def run(self):
        """ When response comes, the class state becomes True.
        It means the Response class is ready for show :)
        """
        
        try:
            self.state = False
            self.response = _get_data(self.site, self._webquery)
            self.state = True
        except Exception as e:
            print(str(e))
            print(e.args)
            self.response = "NO_RESPONSE"
            self.state = True


def get_datas(path):
    import FileQuery
    for i in FileQuery.get_records(path):
        response = [Response(a.parsed_entry) for a in i]
        yield response
        
    


if __name__ == "__main__":
    # data = _get_data(('pp',"P41567", '', '59', 'L', 'P', ''))
    #print(data)
    
    print(next(get_datas()))
    
    # a = next(get_datas())
    
    import time
    
    beklenen = []
    for i in get_datas():
        print(i)
        """
        i.start()
        print("İsim: {}, Site: {}, verisi işleme sokuldu.".format(i.name, i.site))
        beklenen.append(i)
        time.sleep(0.5)
        
    print("\n======================= Tüm veriler gönderildi =================\n\n\n")
    
    while len(beklenen) != 0:
        for i in beklenen:
            if i.state == True:
                print("{} verisi alındı. ".format(i.name))
                print(i.response)
                print("----")
                beklenen.remove(i)"""
    
                
                
                
                
                
                
        

