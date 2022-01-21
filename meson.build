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

icd_json_file = configure_file(
	input: files('mock_icd.json'),
	output: 'mock_icd.json',
	copy: true)

message('config file: @0@'.format(icd_json_file))

