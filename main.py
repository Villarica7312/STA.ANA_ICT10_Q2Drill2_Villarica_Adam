# ---------------------------------------------------------------
# Cartoon Club Member Manager  |  2nd Quarter - Drill 2
# This program only uses set data types and set operators.
# ---------------------------------------------------------------
from pyscript import document

# --- Predefined sets: one set of cartoon club members per grade level ---
grade_7 = {"Mickey Mouse", "Donald Duck", "Bugs Bunny", "Daffy Duck"}
grade_8 = {"Tom Cat", "Jerry Mouse", "Scooby Doo", "Johnny Bravo"}
grade_9 = {"Dexter Mcpherson", "Bubbles Utonium", "Blossom Utonium", "Buttercup Utonium"}
grade_10 = {"Ben Tennyson", "Phineas Flynn", "Ferb Fletcher", "Mabel Pines"}

# --- Set that stores every member typed into the text boxes ---
# It starts empty and grows each time the Submit button is clicked.
new_members = set()

# --- Master set: the union (|) of the four grade sets and the new members ---
master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members


def show_results():
    """Shows the full member list and the total inside the output box."""

    # The sorted list is only used to display; the master set stays a set.
    # "<br>" puts every member name on its own line.
    all_members = "<br>".join(sorted(master_set))

    # Output 1: the full list of all members
    # Output 2: the total number of members (len of the master set)
    document.getElementById("output").innerHTML = f"""
        <div class="results-title">All members:</div>
        <div class="results-list">{all_members}</div>
        <div class="results-total">Total members: {len(master_set)}</div>
    """


def result_checker(event):
    """Runs when the Submit button is clicked (py-click event)."""
    global new_members, master_set

    # Read the two text boxes. strip() removes extra spaces and
    # title() capitalizes the first letter of each name.
    first = document.getElementById("first_name").value.strip().title()
    last = document.getElementById("last_name").value.strip().title()

    # Make the full name and put it inside a set.
    # The difference operator (-) removes an empty name, so a blank
    # submission adds nothing to the club.
    full_name = f"{first} {last}".strip()
    new_member = {full_name} - {""}

    # Set operator: union (|) adds the new member to the new_members set.
    new_members = new_members | new_member

    # Set operator: union (|) combines the four grade sets and the
    # new members into one master set.
    # Sets keep unique values only, so a duplicate name is ignored.
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # Update the page with the member list and the total.
    show_results()

    # Clear the text boxes so the next member can be typed in.
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


# Show the starting list as soon as the page loads.
show_results()
