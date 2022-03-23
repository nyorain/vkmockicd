project(
	'vkmockicd',
	'cpp',
	version: '0.15.0',
	license: 'Apache',
	meson_version: '>=0.47.0',
	default_options: [
		'c_std=c11',
		'warning_level=1',
		'werror=false',
	],
)

src = files('mock_icd.cpp')
lib = shared_library('VkICD_mock_icd', src)

conf_data = configuration_data()

if build_machine.system() == 'windows'
	conf_data.set('libpath', '.\\\\VkICD_mock_icd.dll')
else
	conf_data.set('libpath', './libVkICD_mock_icd.so')
endif

icd_json_file = configure_file(
	input: files('mock_icd.json.in'),
	output: 'mock_icd.json',
	configuration: conf_data)

message('config file: @0@'.format(icd_json_file))

