if __name__ == '__main__':
	obj = [
		{'resource_id': 1, 'truncated_date_time': "",'last_value': None},
	 	{'resource_id': 2, 'truncated_date_time': "",'last_value': None}, 
		{'resource_id': 3, 'truncated_date_time': "",'last_value': None},
	 	{'resource_id': 4, 'truncated_date_time': "",'last_value': None}, 
		{'resource_id': 5, 'truncated_date_time': "",'last_value': 0.03}, 
		{'resource_id': 6, 'truncated_date_time': "",'last_value': 0.04}, 
		{'resource_id': 7, 'truncated_date_time': "", 'last_value': 0.05},
		{'resource_id': 8, 'truncated_date_time': "", 'last_value': None},  
		{'resource_id': 9, 'truncated_date_time': "", 'last_value': 0.06}, 
		{'resource_id': 10, 'truncated_date_time': "", 'last_value': 0.07},
		{'resource_id': 11, 'truncated_date_time': "", 'last_value': 0.08}, 
		{'resource_id': 12, 'truncated_date_time': "", 'last_value': None}
	]

	a = [1, 2, 3, 4, 5, 6, 7]
	b = list(filter(lambda x: x % 2==0, a))
	print(a[:2])

	last_values = list(filter(lambda x: x['last_value'] is not None, obj))

	for idx, item in enumerate(obj):
		if idx > 0:
			if item['last_value'] is None:
				usage = None
				print('usage None: {}'.format(usage))
			elif obj[idx-1]['last_value'] is None:
				prev_values = list(filter(lambda x: x['last_value'] is not None, obj[:idx-1]))
				# print('resource_id: {1} - prev_values: {0}'.format(prev_values[len(prev_values) - 1]['last_value'], item['resource_id']))
				usage = None if len(prev_values)==0 else item['last_value'] - prev_values[len(prev_values) - 1]['last_value']
				print('usage idx-1 None: {0} - {1} - {2}'.format(idx - 1, item['resource_id'], usage))
			else:
				usage = item['last_value'] - obj[idx-1]['last_value']
				print('usage idx-1 not None: {}'.format(usage))
	        