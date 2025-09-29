from pyscript import document

def generate_message(event):
# VALUES FROM INDEX.HTML
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value

# GENERATE TEXT
    message = f"""
Order for : {name}
Address : {address}
Contact Number : {number}\n
"""

# DISPLAY NEW TEXT
    output = document.getElementById("final")
    output.innerHTML = ""
    output.innerHTML = f"<pre>{message}</pre>"