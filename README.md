## License Checker for Python project
This module provides you with a wide functionality for checking license keys and their expiration dates for your program written in Python

### Installing via PyPi

    pip install license_check
### JSON format
Need host JSON file to your site or on GitHub Gists with all licenses data with format:

    {
	    "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX": {
		    "id": "1",
			"expire": "30.12.2022"
        },
        "EXAMPLE_KEY": {
	        "id": "ID ON STRING",
	        "expire": "DD.MM.YYYY"
	    }
    }
### Using in code

    >>> from license_check import check_license
    >>> url = "https://gist.githubusercontent.com/marat2509/33ff3c1eaad4a16b6981326e5d05478c/raw/licenses.key"
    >>> print(check_license(license_url_list = url, license_key = "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX"))
    <<< 1  # License key valid
	>>> print(check_license(license_url_list = url, license_key = "EXPIRED_KEY"))
	<<< -1  # License key expired
	>>> print(check_license(license_url_list = url, license_key = "UNKNOWN_KEY"))
	<<< 0  # License key not registered
### Status codes
| Code | Description           |
|------|-----------------------|
| -406 | Failed to fetch       |
| -1   | License key expired   |
| 0    | License key not found |
| 1    | License key valid     |
### Debug mode
Code:

    from license_check import check_license
    url = "https://gist.githubusercontent.com/marat2509/33ff3c1eaad4a16b6981326e5d05478c/raw/licenses.key"
    print(check_license(license_url_list = url, license_key = "WZ3UD-ADZH8-MFYJB-RUGM3-J37TX", debug = True))
Output:

    2022-06-16 23:33:53.548 | DEBUG    | license_check:check_license:10 - Starting script
    2022-06-16 23:33:53.550 | DEBUG    | license_check:check_license:11 - Fetching current date and time from timeapi.io in JSON
    2022-06-16 23:33:53.912 | INFO     | license_check:check_license:14 - Fetched JSON data, saved dict to 'today'
    2022-06-16 23:33:53.914 | DEBUG    | license_check:check_license:18 - Setting 'to_day' from dict 'today'
    2022-06-16 23:33:53.916 | INFO     | license_check:check_license:20 - Setted 'to_day' to: 16
    2022-06-16 23:33:53.918 | DEBUG    | license_check:check_license:21 - Setting 'to_month' from dict 'today'
    2022-06-16 23:33:53.920 | INFO     | license_check:check_license:23 - Setted 'to_month' to: 6
    2022-06-16 23:33:53.924 | DEBUG    | license_check:check_license:24 - Setting 'to_year' from dict 'today'
    2022-06-16 23:33:53.928 | INFO     | license_check:check_license:26 - Setted 'to_year' to: 2022
    2022-06-16 23:33:53.935 | DEBUG    | license_check:check_license:28 - Fetching JSON license list from: https://gist.githubusercontent.com/marat2509/33ff3c1eaad4a16b6981326e5d05478c/raw/licenses.key
    2022-06-16 23:33:54.276 | INFO     | license_check:check_license:31 - Fetched JSON data, saved to dict 'data'
    2022-06-16 23:33:54.278 | DEBUG    | license_check:check_license:35 - Checking license key in license list
    2022-06-16 23:33:54.280 | INFO     | license_check:check_license:38 - License key in a license list, license ID: 1
    2022-06-16 23:33:54.284 | DEBUG    | license_check:check_license:40 - Checking whether the license key expired
    2022-06-16 23:33:54.285 | INFO     | license_check:check_license:48 - License key valid! The license key valid until: 30.12.2022
    1
