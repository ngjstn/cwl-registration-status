import yaml 

class CWLscraper(object): 
    def __init__(self): 
        with open('config.yaml', 'r') as file: 
            print('Parsing config.yaml')
            props = yaml.safe_load(file)

        self.number = props['user_contact']['phone_number']
        self.carrier = props['user_contact']['carrier'] 


    def list_props(self): 
        print('number: %s' % self.number)
        print('carrier: %s' % self.carrier)


if __name__ == '__main__': 
    auto = Scraper()
    auto.list_props()