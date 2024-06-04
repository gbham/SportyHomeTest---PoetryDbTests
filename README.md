# PoetryDB API Test Cases

## Test Cases Overview

| Test Case                                          | Description                                                                                                            | Expected Status Code | Expected Response Content                                                                                                                     |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `test_search_by_author_and_invalid_output_field`   | Search by author "Dickinson" with invalid output field "wrongfield"                                                    | 200                  | `"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."` <br> `"status":"405"`                |
| `test_search_by_author_and_valid_and_invalid_output_fields` | Search by author "Dickinson" with valid output field "author" and invalid output field "wrongfield"                     | 200                  | `"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."` <br> `"status":"405"`                |
| `test_invalid_output_format`                       | Search by author "Dickinson" with invalid output format "all.invalid"                                                  | 200                  | `"status":"405"`                                                                                                                            |

## Test Cases Explanation

1. **`test_search_by_author_and_invalid_output_field`**:
    - **Request**: Sends a GET request to the endpoint `/author/Dickinson/wrongfield` using the `APIClient`.
    - **Expected Status Code**: 200
    - **Expected Response Content**:
        - `"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."`
        - `"status":"405"`

2. **`test_search_by_author_and_valid_and_invalid_output_fields`**:
    - **Request**: Sends a GET request to the endpoint `/author/Dickinson/author,wrongfield` using the `APIClient`.
    - **Expected Status Code**: 200
    - **Expected Response Content**:
        - `"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."`
        - `"status":"405"`

3. **`test_invalid_output_format`**:
    - **Request**: Sends a GET request to the endpoint `/author/Dickinson/all.invalid` using the `APIClient`.
    - **Expected Status Code**: 200
    - **Expected Response Content**:
        - `"status":"405"`
