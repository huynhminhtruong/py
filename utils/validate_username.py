import re

def username_pattern(self, value):
	allowed_characters = r'^[ A-Za-z0-9_.-]*$'
	not_consecutive_special_characters = r'^(?!.*[\_\.\-]{2}).*$'

	if len(value) < 8 or len(value) > 20:
	    raise ValidationError('Username needs be at least 8 characters and up to 20 characters')
	if re.search(allowed_characters, value) is None:
	    raise ValidationError('Allow hyphen -, underscore _ and dot . only in username')
	if re.search(not_consecutive_special_characters, value) is None:
	    raise ValidationError('Username cannot contain two consecutive special characters')

if __name__ == '__main__':
	username = ['a1_2-123@!', '!@#!$!#$', '-A.-']

	allowed_characters = r'^[ A-Za-z0-9_.-]*$'
	not_consecutive_special_characters = r'^(?!.*[\_\.\-]{2}).*$'
	combine_regex = r'^[A-Za-z0-9_.-](?!.*[\_\.\-]{2}).{8,20}$'

	for i, u in enumerate(username):
		x = re.search(allowed_characters, u)
		y = re.search(not_consecutive_special_characters, u)
		z = re.search(combine_regex, u)

		print(i, z)
		print('\n')