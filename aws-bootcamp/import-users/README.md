# import-users


## Purpose
Ever have to create over 1000 IAM users and groups from a CSV?

This program creates IAM users and groups from a CSV file with a fixed format. It will also associate a policy with the users to require MFA for login. There is some limited input validation built in.

## Input format
The csv file should have the following headers: `Name,Email,Team`.

- `Name` is a full name, with multiple words, which may include whitespace and special characters.
- `Email` is a valid email address, which may contain unicode.
- `Team` is the name of a team such as `Network Admins`, which may contain spaces and special characters.

You can find an example of the input format in `data/sample-input.csv`. There is also an corresponding example output in `data/sample-report.csv` and `sample-log.json`.

## Operation
When you run `import-users --in input.csv --out report.csv --log log.json`, the program will:

- Clean up input data for use in IAM

    - Convert `Name` into a tag with the users full name.
    - Convert the user portion of the `Email` into a valid IAM user name and check that no user exists with that user name.
    **The email is the basis for the IAM username**.
    - Convert `Team` to a valid IAM group name and check that no group exists with that group name.
    - Randomly generate a password for each user.

- Create resources on AWS

    - Create IAM users and groups from data in the CSV.
    - Created users will be required to set a new password on login.
    - Created users will also be requried them to set up MFA on first login (which is accomplised by adding them to the `MFARequired` group).

- Log the results of any AWS API calls to `log.json`.
- Generate a csv report with the username, group name, and password.

## Installation
You can run this project witout installation using `uv`.

- First, [install uv](https://docs.astral.sh/uv/getting-started/installation/).
- Then, run the cli with `uv run import-users --in input.csv --out report.csv --log log.json`, substituting in the relevant filenames.

If you decide that you do want to install the program permanently, you can use `uv pip install .`. Then you can run `import-users` directly (without the `uv run` prefix.).

## Running project specific tools
This project uses `poethepoet` to run tools such as automated tests, linters, type checkers, and more. Check `pyproject.toml` for a list of tasks you can run. The general form for running tasks is `uv run poe {task_name}`.

## Automated tests
To run the tests, use `uv run poe test`, or directly using `uv run pytest`, instead. You may want to run `pytest` directly in order use features beyond a simple test run.
