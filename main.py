from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/ussd", response_class=PlainTextResponse)
async def ussd_callback(
    sessionId: str = Form(...),
    serviceCode: str = Form(...),
    phoneNumber: str = Form(...),
    text: str = Form("")
):
    """
    Handles incoming USSD requests from Africa's Talking.
    """

    # Split the text input by '*' to understand the user's path
    user_response = text.split('*')

    if text == "":
        # Main menu
        response = "CON Welcome to Flood Info Service\n"
        response += "1. View Warnings\n"
        response += "2. Report Incident\n"
        response += "3. Preferences\n"
        response += "4. Feedback"

    elif text == "1":
        response = "CON View Warnings:\n1. My Location\n2. Others"

    elif text == "1*1":
        response = "END Current Flood Warnings for Your Location:\nHeavy rains expected in your area.\nStay alert."

    elif text == "1*2":
        response = "END Other location warnings will be available soon."

    elif text == "2":
        response = "CON Report Incident:\nEnter short description of the flood or hazard."

    elif text.startswith("2*"):
        incident_description = text.split("*", 1)[1]
        # Later: Save `incident_description` to DB with phone number
        response = f"END Thank you for reporting: '{incident_description}'."

    elif text == "3":
        response = "CON Preferences:\n1. Language\n2. Message Mode\n3. Hazard Location"

    elif text == "3*1":
        response = "CON Select Language:\n1. English\n2. Swahili"

    elif text == "3*1*1":
        response = "END Language set to English."

    elif text == "3*1*2":
        response = "END Lugha imewekwa Kiswahili."

    elif text == "3*2":
        response = "CON Message Mode:\n1. Text\n2. Audio"

    elif text == "3*2*1":
        response = "END Text mode enabled."

    elif text == "3*2*2":
        response = "END Audio mode enabled."

    elif text == "3*3":
        response = "CON Select Hazard Location:\n1. Location 1\n2. Location 2"

    elif text == "3*3*1":
        response = "END Hazard Location set to Location 1."

    elif text == "3*3*2":
        response = "END Hazard Location set to Location 2."

    elif text == "4":
        response = "END Thank you for choosing our service. Your feedback helps us improve."

    else:
        response = "END Invalid choice. Please try again."

    return response


# Run locally
# uvicorn main:app --host 0.0.0.0 --port 8000