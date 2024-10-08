### import statements 
import json
import obonet
from itertools import combinations 
from Bio import Medline
import networkx as nx

# parsing a medline file 
def parse_medline(medline_file):    
    list_of_abstracts = []    
    pmid = ''
    abstract = ''  
    with open(medline_file) as medline_handle:
        records = Medline.parse(medline_handle)
        for record in records:         
            keys = record.keys()            
            if 'PMID' in keys and 'AB' in keys: 

                pmid = record['PMID']
                abstract = record['AB']

                pair = (pmid, abstract)
                list_of_abstracts.append(pair)
    return list_of_abstracts
    
# parsing a medline file 
def parse_medline_rmap(medline_file):    
    map_abstracts = {}    
    pmid = ''
    abstract = ''  
    with open(medline_file) as medline_handle:
        records = Medline.parse(medline_handle)
        for record in records:         
            keys = record.keys()            
            if 'PMID' in keys and 'AB' in keys: 

                pmid = record['PMID']
                abstract = record['AB']
                
                map_abstracts[pmid] = abstract
    return map_abstracts    
    
### parse DOID ontology
def parse_obo_onto(obo_file):    
    obonto_term = {}    
    graph = obonet.read_obo(obo_file) 
    for key, item in graph.nodes(data=True):
        
        name = ''
        # synonym = []
        # xref = []
        # isa = []
        # relationship = []

        if 'name' in item:
            name = item['name'].strip(',').strip('\n').strip('.').strip('(').strip(')').lower()    

#         if 'synonym' in item:
#             synonym = item['synonym']
            
#         if 'xref' in item:
#             obonto_term[key] = item['xref']
            
#         if 'is_a' in item:
#             isa = item['is_a']  
#             # print(isa)
#         if 'relationship' in item:
#             relationship = item['relationship']             
            # print(isa)
        
        obonto_term[key] = name # ( isa, synonym, xref, relationship)
            
    return obonto_term


# parsing a medline file 
# def parse_chatGPT_json(json_file):    
#     map_json = {}    
#     pmid = ''
#     title = ''
#     abstract = ''  
#     with open(json_file) as json_handle:
#         records = Medline.parse(json_handle)
#         for record in records:         
#             keys = record.keys()            
#             if 'PMID' in keys and 'AB' in keys: 

#                 pmid = record['PMID']
#                 title = record['Title']
#                 abstract = record['AB']
                
                
#                 map_abstracts[pmid] = abstract
#     return map_abstracts 



def read_json_file(json_file):
    
    with open(json_file, "r") as f:
        data = json.loads(f.read())
    
    return data
    


def parse_json_data(data):
        
    """Creates a map with the ID being the key and the title and abstract as values."""
    map = {}
    for item in data:
        map[item["id"]] = item["title"] + " " + item["abstract"]
    return map

def test():
    print('Hello ...')



if __name__ == "__main__":
    # obo_file = 'symptoms.obo'    
    # ontology_dict = load_obo_onto(obo_file)    
    
    # obo_file = 'doid.obo'    
    # ontology_dict = parse_obo_onto(obo_file)  
    
    
    data = read_json_file('chatgpt_articles_wids.json')    
    chatGPT_articles_map = parse_json_data(data)
    for record_id, record_text in chatGPT_articles_map.items():

        print("record_id: ", record_id, "record_text: ", record_text)
        print('\n--------')
    
    
    
    
    
    