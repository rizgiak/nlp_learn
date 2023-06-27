import PySimpleGUI as sg
import time

def simulate_loading(window):
    progress_bar = window['-PROGRESS-']
    progress_text = window['-PROGRESS-TEXT-']
    for i in range(1, 101):
        time.sleep(0.05)  # Simulating some work being done
        progress_bar.update(i)
        progress_text.update(f"Progress: {i}%")

layout = [
    [sg.Text("Select a folder:")],
    [sg.Input(key="-FOLDER-", disabled=True), sg.FolderBrowse()],
    [sg.Text("Options:")],
    [sg.Column(
        [
            [sg.Checkbox("Metadata", default=True, key="-CHECKBOX1-", size=(7, 1)),
             sg.Checkbox("Texts", default=True, key="-CHECKBOX2-", size=(7, 1)),
             sg.Checkbox("Images", default=True, key="-CHECKBOX3-", size=(7, 1)),
             sg.Checkbox("Tables", default=True, key="-CHECKBOX4-", size=(7, 1))]
        ],
        element_justification='center'
    )],
    [sg.Button("Submit", key='-SUBMIT-')]
]

window = sg.Window("Folder Selection", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "-SUBMIT-":
        if values["-FOLDER-"] == "":
            sg.popup(f"Select folder path!", title="Error!")
        else:
            folder_path = values["-FOLDER-"]
            checkbox_values = [
                values["-CHECKBOX1-"],
                values["-CHECKBOX2-"],
                values["-CHECKBOX3-"],
                values["-CHECKBOX4-"]
            ]

            # Hide the first window
            window.hide()

            loading_layout = [
                [sg.Text("Loading...")],
                [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
                [sg.Text("Progress: 0%", key='-PROGRESS-TEXT-')]
            ]

            loading_window = sg.Window("Loading", loading_layout, finalize=True)

            simulate_loading(loading_window)

            loading_window.close()

            sg.popup(f"Selected folder: {folder_path}\nCheckbox values: {checkbox_values}", title="Complete")

            break

window.close()
