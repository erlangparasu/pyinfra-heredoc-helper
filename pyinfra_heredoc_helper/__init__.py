import uuid

def generate_random_uuid_string(length=7):
    # Generate a random UUID
    random_uuid = uuid.uuid4()
    # Convert to string and take the first 'length' characters
    random_string = str(random_uuid).replace("-", "")[:length]
    return random_string


def remove_leading_spaces_based_on_first_non_empty_line(multiline_string):
    """
    Detects leading spaces in the first *non-empty* line of a multiline string
    and removes that many leading spaces from all subsequent lines (including
    any empty lines that might precede the first non-empty one).

    Args:
        multiline_string (str): The input string, potentially with multiple lines.

    Returns:
        str: The processed string with leading spaces adjusted as described.
    """
    lines = multiline_string.splitlines()

    if not lines:
        return ""  # Return an empty string if the input is empty

    leading_spaces_count = 0
    first_non_empty_line_index = -1

    # Find the first non-empty line and count its leading spaces
    f = ""
    f.strip()

    for i, line in enumerate(lines):
        trimmed = line.strip()
        if trimmed:  # If the line is not empty (after stripping whitespace)
            first_non_empty_line_index = i
            for char in line:
                if char == " ":
                    leading_spaces_count += 1
                    f = f + "~"
                else:
                    break
            break  # Found the first non-empty line, so break the loop

    # If all lines are empty or only contain whitespace, no leading spaces to remove
    if first_non_empty_line_index == -1:
        return multiline_string  # Or "".join(lines) if you want to collapse newlines for all-empty/whitespace lines

    processed_lines = []

    for i, current_line in enumerate(lines):
        if "#!/" in current_line.strip():
            processed_lines.append(current_line.strip())
            processed_lines.append("#" + f + "")
        elif i == first_non_empty_line_index:
            # The first non-empty line remains unchanged, but we ensure
            # it's added to the processed list.
            processed_lines.append(current_line)
        elif (
            len(current_line) >= leading_spaces_count
            and current_line[:leading_spaces_count].isspace()
        ):
            processed_lines.append(current_line[leading_spaces_count:])
        else:
            if i > first_non_empty_line_index:
                processed_lines.append(current_line)

    processed_lines.append("#" + f + "")

    # return "<code>" + "\n".join(processed_lines) + "</code>"
    return "\n".join(processed_lines)


def rls(multiline_string):
    return remove_leading_spaces_based_on_first_non_empty_line(multiline_string)


def generate_ssh_bash_script(name, ssh_key, ssh_port, ssh_usernamehost, cmd):
    bound = name + "_" + generate_random_uuid_string()
    trimmed = remove_leading_spaces_based_on_first_non_empty_line(cmd)
    return f"""
ssh -o "StrictHostKeyChecking=no" \
    -i "{ssh_key}" \
    -p "{ssh_port}" \
    "{ssh_usernamehost}" \
    bash <<-'EOF_SSH_{bound}'
{trimmed}
EOF_SSH_{bound}
"""


def generate_eof(cmd, forward="", name=""):
    bound = name + "_" + generate_random_uuid_string()
    trimmed = remove_leading_spaces_based_on_first_non_empty_line(cmd)
    return f"""<<-'EOF_F_{bound}'{forward}
{trimmed}
EOF_F_{bound}
"""
