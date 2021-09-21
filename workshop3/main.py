import yaml

weaknessVars = ['foreman_repository_base',
		'foreman_plugin_repository_base',
		'content_rhel_url',
		'content_sattools_url',
		'test_sync_repositories_url_template',
		'vms_kss_os']
weaknessVarsData = []
playUsageData = []
lineNum = []

with open('Workshop3.values.yaml') as valuesFile:
	data_val = yaml.load(valuesFile, Loader=yaml.FullLoader)
with open('Workshop3.play1.yaml') as play1File:
	data_play1 = yaml.load(play1File, Loader=yaml.FullLoader)
with open('Workshop3.play2.yaml') as play2File:
	data_play2 = yaml.load(play2File, Loader=yaml.FullLoader)

for x in weaknessVars:
	weaknessVarsData.append(data_val[x])

with open('Workshop3.play1.yaml', 'r') as file:
	pattern = "- name: "
	for name, line in enumerate(file, 1):
		if pattern in line:
			playUsageData.append(line)

y = 0
while y < len(weaknessVars):
	with open('Workshop3.values.yaml', 'r') as file:
		pattern = weaknessVars[y]
		for num, line in enumerate(file, 1):
			if pattern in line:
				lineNum.append(num)
				print("\nSecurity weakness name: Use of HTTP without SSL/TLS")
				print("Security weakness location: Variable \'" + weaknessVars[y] + "\' in line" , num)
	y = y + 1
