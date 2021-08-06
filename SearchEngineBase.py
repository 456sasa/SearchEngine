class SearchEngineBase():
    def __init__(self):
        pass
    def add_corpus(self,file_path):
        with open(file_path,'r') as f:
            text = f.read()
        self.process_corpus(file_path,text)
    def process_corpus(self, id, text): 
        raise Exception('process_corpus not implemented.') 

    def search(self, query): 
        raise Exception('search not implemented.')

    
def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print(f"found {len(results)} result(s)")
        for result in results:
            print(result)