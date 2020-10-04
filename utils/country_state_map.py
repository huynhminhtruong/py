# Current mapping
def get_country_state_map(self, request):
	countries = self.get_country_codes(request)
	states = self.get_state_codes(request)
	country_state_map = dict()
	if 'results' in countries and 'results' in states:
	    tmp = dict()
	    for country in countries['results']:
	        tmp[str(country['id'])] = country['code']
	    for state in states['results']:
	        if str(state['country']) in tmp:
	            country_code = tmp[str(state['country'])]
	            if country_code not in country_state_map:
	                country_state_map[country_code] = {
	                    "id": state['country'],
	                    "states": {}
	                }
	            if state['code'] is not None:
	                country_state_map[country_code]['states'][state['code']] = state['id']
	            country_state_map[country_code]['states'][state['name']] = state['id']
	return country_state_map

# Plan to mapping
def __to_dict(self, data):
	res = dict()
	for country in data:
	    res[country['id']] = country
	return res

def __mapping_country_code(self, state):
	print('state: {}'.format(state))
	state['country'] = self._countries[state['country']]
	return state

def get_country_state_map(self, request):
	self._countries = self.__to_dict(self.get_country_codes(request)['results'])
	states = self.get_state_codes(request)['results']
	country_state_map = list(map(self.__mapping_country_code, states))
	for _ in country_state_map:
	    print(_)
