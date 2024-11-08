import ipywidgets as widgets
import random
import time
from IPython.display import display, clear_output

# Λίστα με τα χρώματα και τα αντίστοιχα ονόματά τους
colors = {
    "red": "Κόκκινο",
    "blue": "Μπλε",
    "yellow": "Κίτρινο",
    "green": "Πράσινο"
}

# Ρύθμιση χρόνων
change_interval = 2.5  # Χρόνος αλλαγής χρώματος σε δευτερόλεπτα
total_duration = 60  # Συνολική διάρκεια σε δευτερόλεπτα

# Δημιουργία του widget
color_box = widgets.Output()

# Μεταβλητές για παρακολούθηση του προηγούμενου χρώματος και επαναλήψεων
previous_color = None
repeat_count = 0
remaining_time = total_duration

# Εμφάνιση του widget
display(color_box)

# Συγχρονισμένη συνάρτηση για την εμφάνιση του τυχαίου χρώματος και του ονόματός του με αντίστροφη μέτρηση
while remaining_time > 0:
    color, color_name = random.choice(list(colors.items()))  # Επιλογή τυχαίου χρώματος και ονόματος

    # Έλεγχος αν το χρώμα είναι ίδιο με το προηγούμενο
    if color == previous_color:
        repeat_count += 1
        color_name_display = f"{color_name} " + "ξανά " * repeat_count
    else:
        repeat_count = 0
        color_name_display = color_name

    # Ενημέρωση του προηγούμενου χρώματος
    previous_color = color

    # Προβολή του χρώματος και της συνολικής αντίστροφης μέτρησης
    for seconds_left in range(int(change_interval), 0, -1):
        with color_box:
            clear_output(wait=True)
            display(widgets.HTML(f'''
                <div style="width:100%; height:200px; background-color:{color};
                            display:flex; align-items:center; justify-content:center;
                            color:white; font-size:30px; font-weight:bold; flex-direction:column;">
                    <div>{color_name_display}</div>
                    <div style="font-size:20px; margin-top:10px;">Χρόνος: {remaining_time} δευτερόλεπτα</div>
                </div>
            '''))
        time.sleep(1)
        remaining_time -= 1