# USSD Flood Info Service

## Quick Deploy
1. Fork this repo
2. Deploy to Railway/Render/Heroku
3. Update Africa's Talking webhook URL

## Local Run
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

## USSD Code: *384*23090#

## Menu Structure:
1. View Warnings → My Location/Others
2. Report Incident → Text input
3. Preferences → Language/Message Mode/Hazard Location  
4. Feedback