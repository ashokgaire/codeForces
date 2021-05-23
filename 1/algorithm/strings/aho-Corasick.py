from collections import deque

Adjlist = []

def init_trie(keywords):
    ''' creates a trie of kewords , then sets fail transitions '''
    create_empty_trie()
    add_keywords(keywords)
    set_fail_transitions()


def create_empty_trie():
    """ initia;ize the root of the trie """

    Adjlist.append({'value':'', 'next_states':[], ' fail_state':0, 'output':[]})

def add_keywords(keywords):
    """ add all keywords in list of keywords """

    for keyword in keywords:
        add_keyword(keyword)

def find_next_state(current_state, value):
    for node in Adjlist[current_state]["next_states"]:
        if Adjlist[node]["value"] == value:
            return node
    return None


def add_keyword(keyword):
    """ add a keywrd to the trie and mark output at the end"""

    current_state = 0
    j = 0
    keyword = keyword.lower()

    child = find_next_state(current_state,keyword[j])
    while child != None:
        current_state = child
        j = j +1
        if j < len(keyword):
            child = find_next_state(current_state, keyword[j])
        else:
            break
    
    for i in range(j, len(keyword)):
        node = {'value':keyword[i], 'next_state':[], 'fail_state':0, 'output':[]}
        Adjlist.append(node)
        Adjlist[current_state]["next_states"].append(len(Adjlist) -1)
        current_state = len(Adjlist) - 1
    Adjlist[current_state]["output"].append(keyword)



def set_fail_transitions():
    q = deque()
    child = 0
    for node in Adjlist[0]["next_states"]:
        q.append(node)
        Adjlist[node]["fail_state"] = 0
    while q:
        r = q.popleft()
        for child in Adjlist[r]["next_states"]:
            q.append(child)
            state = Adjlist[r]["fail_state"]
            while find_next_state(state, Adjlist[child]["value"]) == None \
    and state != 0:
                state = Adjlist[state]["fail_state"]
            Adjlist[child]["fail_state"] = find_next_state(state, 
   Adjlist[child]["value"])
            if Adjlist[child]["fail_state"] is None:
                Adjlist[child]["fail_state"] = 0
            Adjlist[child]["output"] = Adjlist[child]["output"] +  Adjlist[Adjlist[child]["fail_state"]]["output"]


def get_keywords_found(line):
    """ returns true if line contains any keywords in trie """
    line = line.lower()
    current_state = 0
    keywords_found = []
   
    for i in range(len(line)):
        while find_next_state(current_state, line[i]) is None and current_state != 0:
            current_state = Adjlist[current_state]["fail_state"]
        current_state = find_next_state(current_state, line[i])
        if current_state is None:
            current_state = 0
        else:
            for j in Adjlist[current_state]["output"]:
                keywords_found.append({"index":i-len(j) + 1,"word":j})
    return keywords_found

init_trie(['cash', 'shew', 'ew'])
print(get_keywords_found("cashew"))