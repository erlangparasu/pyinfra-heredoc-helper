# Functions in pyinfra-heredoc-helper

## `generate_random_uuid_string(length=7)`

Generates a random UUID string of a specified length.

**Args:**
* `length` (int, optional): The desired length of the random string. Defaults to 7.

**Returns:**
* `str`: A random string of the specified length.

## `remove_leading_spaces_based_on_first_non_empty_line(multiline_string)`

Detects leading spaces in the first *non-empty* line of a multiline string
and removes that many leading spaces from all subsequent lines (including
any empty lines that might precede the first non-empty one).

**Args:**
* `multiline_string` (str): The input string, potentially with multiple lines.

**Returns:**
* `str`: The processed string with leading spaces adjusted as described.

## `rls(multiline_string)`

Alias for `remove_leading_spaces_based_on_first_non_empty_line`.

**Args:**
* `multiline_string` (str): The input string, potentially with multiple lines.

**Returns:**
* `str`: The processed string with leading spaces adjusted as described.

## `generate_ssh_bash_script(name, ssh_key, ssh_port, ssh_usernamehost, cmd)`

Generates a bash script that executes a command over SSH.

**Args:**
* `name` (str): A name for the script, used to create a unique boundary string.
* `ssh_key` (str): Path to the SSH private key.
* `ssh_port` (str): The SSH port.
* `ssh_usernamehost` (str): The SSH username and host (e.g., `user@host`).
* `cmd` (str): The command to execute on the remote host.

**Returns:**
* `str`: The generated SSH bash script.

## `generate_eof(cmd, forward="", name="")`

Generates a heredoc string with a unique boundary.

**Args:**
* `cmd` (str): The command or content to be included in the heredoc.
* `forward` (str, optional): Additional string to include after the heredoc start. Defaults to "".
* `name` (str, optional): A name for the heredoc, used to create a unique boundary string. Defaults to "".

**Returns:**
* `str`: The generated heredoc string.
