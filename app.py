import tkinter as tk
from sports_injury_info import get_injury_info

def search_injury(): # function called when user clicks search button
    injury_name= entry.get() # gets the text entered by the user in the entry widget and assigns it to the variable injury_name
    result = get_injury_info(injury_name) # calls the get_injury_info function with the injury_name as the argument
    if isinstance(result,dict):
        result_text = f"Description: {result['Description']}\n" \
                      f"Common Sports: {', '.join(result['Common Sports'])}\n" \
                      f"Treatment: {result['Treatment']}\n" \
                      f" Recovery Exercises: {','.join(result['Recovery Exercises'])}"
    else : result_text = result

    result_label.config(text=result_text)

root = tk.Tk() #This is the main container for all the widgets in the application
root.title("Sport Injury Info")

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Search", command=search_injury)
search_button.pack()

result_label = tk.Label(root,text="", wraplength=300)
result_label.pack()

root.mainloop() # waits for events such as button clicks or key presses and updates the GUI accordingly.
                    #It keeps the application running and responsive.






