import shodan, io

key = #SHODAN API KEY GOES HERE

class scraper:
    def scrape(query):
        api = shodan.Shodan(key)
        try:
            results = api.search(query)
            print('Results found: {}'.format(results['total']))
            with io.open('scraper-output.txt','w',encoding='utf=8') as op:    
                for result in results['matches']:
                    op.write('IP: {} \n\n'.format(result['ip_str']))
                    op.write(result['data']+'\n\n')
        except shodan.APIError as e:
            print('Error: {}'.format(e))
