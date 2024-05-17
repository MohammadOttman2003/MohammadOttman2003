from flask import Flask, request, render_template_string
from sports_injury_info import get_injury_info

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():  # Contains the logic to display the form and process the user's input.
    result_text = ""  # This variable will hold the formatted injury information or an error message to be displayed in the HTML template.

    if request.method == 'POST':  # Determines if the form has been submitted. If true, the function processes the form data.
        injury_name = request.form['injury_name']  # Retrieves the value of the injury_name field from the submitted form data.
        result = get_injury_info(injury_name)  # Calls the get_injury_info function with injury_name as the argument and stores the result in the result variable.
        if isinstance(result, dict):
            result_text = (
                f"Description: {result['Description']}<br>"  # Starts building the result_text string by including the injury description, using <br> for line breaks.
                f"Common Sports: {', '.join(result['Common Sports'])}<br>"  # Formats the common sports list properly.
                f"Treatment: {result['Treatment']}<br>"  # Includes the treatment information.
                f"Recovery Exercises: {', '.join(result['Recovery Exercises'])}"  # Corrects the key name and string syntax.
            )
        else:
            result_text = result  # Sets result_text to the result message if no valid injury information is found.

    return render_template_string('''
    <!doctype html> 
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Sports Injury Info</title>
        </head>
        <body>
            <h1>Sports Injury Info</h1>
            <form method="post">
                <label for="injury_name">Injury Name:</label><br>
                <input type="text" id="injury_name" name="injury_name"><br><br>
                <input type="submit" value="Search">
            </form>
            <p>{{ result_text|safe }}</p>
        </body>
    </html>
    ''', result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)

