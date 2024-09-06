import uvicorn
import joblib
import io
import tensorflow as tf
import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile

app = FastAPI()
joblib_file = open("potato_leaf_disease_detector.joblib", "rb")

model = joblib.load(joblib_file)

@app.post('/predict/')
async def predict_potato_health(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        try:
            image_bytes = await file.read()
            image = Image.open(io.BytesIO(image_bytes))
            image = image.resize((128, 128))
            img_array = tf.keras.preprocessing.image.img_to_array(image)
            img_array = tf.expand_dims(image, axis=0) # Add batch dimension
            prediction = model.predict(img_array)
            
            class_names = ['Early Blight', 'Healthy', 'Late Blight']

            return {"Predicted class": f"{class_names[np.argmax(prediction[0])]}"}
        
        except Exception as e:
            return {"message": f"There was an error uploading the file: {e}"}
        
        finally:
            file.file.close()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)