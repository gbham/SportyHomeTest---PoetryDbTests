# PoetryDB API Test Cases

## Test Cases Overview

| Test Case                                          | Description                                                                                                             Expected Response Content                                                                                                                     |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `test_search_by_author_and_invalid_output_field`   | Search by author "Dickinson" with invalid output field "wrongfield"                                                    | `"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."` <br> `"status":"405"`                |
| `test_search_by_author_and_valid_and_invalid_output_fields` | Search by author "Dickinson" with valid output field "author" and invalid output field "wrongfield"                     | `"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."` <br> `"status":"405"`                |
| `test_invalid_output_format`                       | Search by author "Dickinson" with invalid output format "all.invalid"                                                  | `"status":"405"`                                                                                                                            |

