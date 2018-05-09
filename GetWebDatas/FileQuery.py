
class Entry():
    def __init__(self, entry):
        self.entry = entry
        self.parsed_entry = self._parse_entry()
        

    def _parse_entry(self):
        #  (site, name, (site_values...))
        parsed_entry = []
        parse_tree = self.entry.split('\n')
        parse_tree = [[a.strip() for a in i.split(":")]  for i in parse_tree]

        parsed_entry.append(parse_tree[0][1])
        parsed_entry.append(parse_tree[1][1])

        del parse_tree[:2] 
        parsed_entry.append(self._search(parsed_entry[0], parse_tree))
        
        return parsed_entry

    def _search(self, site, parse_tree):
        import FileCodeTranslator as fct
        web_input_list = fct.select_list[site]

        web_values = ['']*len(web_input_list)

        i_counter = 0
        for i in web_input_list:
            j_counter = 0
            for j in parse_tree:
                if i == j[0]:
                    web_values[i_counter] = j[1]
                    del parse_tree[j_counter]
                    break
                j_counter += 1
            i_counter += 1

        if (len(parse_tree) != 0): print('geriye eleman kaldi {}'.format(parse_tree))

        return tuple(web_values)
            


def _get_entries(path):
    """ Reads an entries from file. 
    An entry includes string data from first char till '\n' char and yields it.
    """ 
    with open(path, "r", encoding="utf-8") as file:
        entry = ""
        for line in file:   
            if not line == "\n":
                entry += line
            else:
                yield entry.strip()
                entry = ""
                

def get_records(path):
    li = []
    for i in _get_entries(path):
        li.append(Entry(i))
        if len(li) == 5:
            yield tuple(li)
            li = []
        
    yield tuple(li)
        


if __name__ == "__main__":
    for i in get_records():
        print(i.parsed_entry)
    
