# custom-text-test-runner

### Description
A custom test runner for python unittest which provides the following additional features:
- custom result stream output in a more detailed, clear format with distinct sections for errors, failures, skipped test, overall suite results, and totals
- all results are output to a json file allowing the results to easily be parsed and used for post-processing purposes and integrations with other services
- automatic detection of screenshots (based on a screenshot directory argument) which are attached to the matching case result dict in the json results file
- detailed time tracking at the case, suite, and overall level
- ability to combine results from previous runs
- config file can be passed with additional information for more customization (currently can provide a device_name key in the config to specify which devices to run a selenium or appium test for example with)

### Installation
`pip install custom_text_test_runner`

### Usage
```
import unittest
from custom_text_test_runner import CustomTextTestRunner

test_modules = unittest.defaultTestLoader.discover(start_dir='path/to/testdir', pattern='test*.py', top_level_dir=None)
return_code = CustomTextTestRunner(
    verbosity=5,
    results_file_path='path/to/result.json',
    result_screenshots_dir='path/to/screenshots',
    show_previous_results=True).run(test_modules).returnCode()
```
