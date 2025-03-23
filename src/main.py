from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()

MissionStatement = ""


@app.post("/UploadMissionStatement")
async def upload_mission_statement(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "File must be a PDF"}

    try:
        # Read the contents of the uploaded file
        contents = await file.read()

        # Here you can add additional processing for the PDF
        # For example, saving it to disk or processing its contents

        return {
            "filename": file.filename,
            "size": len(contents),
            "content_type": file.content_type,
            "status": "success",
        }
    except Exception as e:
        return {"error": str(e)}


@app.post("/UploadGrantApplication")
async def upload_grant_application(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "File must be a PDF"}

    try:
        # Read the contents of the uploaded file
        contents = await file.read()

        # Here you can add additional processing for the PDF
        # For example, saving it to disk or processing its contents

        return {
            "filename": file.filename,
            "size": len(contents),
            "content_type": file.content_type,
            "status": "success",
        }
    except Exception as e:
        return {"error": str(e)}
    




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
