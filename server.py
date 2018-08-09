from flask import Flask, redirect, url_for, request
import base64
from filterNames import getNameFiles
from predict import predict
from predictName import predictName
from category import category
from PredictionModelNew import executeWithParameter, getPercents, getResults, refreshResults
import json
#initialize server
app = Flask(__name__)
#empty dictionary to hold the photo
data = None

#if you go to http://(ip address):(port number)/
@app.route("/", methods=["GET"])
def success():
    #if data equals none then the photo did not send
    if data == None:
        return "lol"
    #else return show the photo on the server by rendering a html tag
    else:
        return "<img src='data:image/png;base64, " + data["photo"] + "'/>"

#if you go to http://(ip address):(port number)/photo
@app.route("/photo", methods=["POST"])
def test():
    #holds the results
    results = []
    #defaults the percent value
    percent = 0.0
    #gets dictionary from filterNames
    subCategories = getNameFiles()
    #get the global variable data
    global data 
    #get json file containing the imageString from android app
    data = request.get_json(cache=True)
    #get photo from data
    photo = data["photo"]
    #open photo and decode base64 string
    with open("test.png", mode="wb") as f:
    	f.write(base64.b64decode(photo))
    #run modeil
    subCat = executeWithParameter("subcategoriesgraph.pp", "subcategorieslabels.txt", "test.png")
    #format subcategory to be upercase and get subcategory prediction
    subCat = subCat.get("prediction").title()
    #set empty variable to check if there is a valid solution
    predictionName = None
    #for each key and value in subcategories dictionary
    for key, value in subCategories.items():
        #TEST PRINT
        print(key)
        #TEST PRINT
        print(key == subCat)
        #if subcategory contains more than one name
        if key == subCat:      
            #run model
            modelPredictionName = executeWithParameter(value[0], value[1], "test.png")
            #get prediction value
            predictionName = modelPredictionName.get("prediction")    
            #get prediction accuracy
            percent = modelPredictionName.get("accuracy")  
            #TEST PRINT
            print("*********", percent)
            #format unique name
            predictionName = predictionName.title()
    #TEST PRINT
    print(subCat)   
    #if subcategory predicts a value with only one unique name
    if subCat == "Air Conditioning":
        predictionName = "HVAC Unit"
        percent = 100
    elif subCat == "Fondant Warmer":
        predictionName = "Fondat Warmer"
        percent = 100
    elif subCat == "Ice Cream Machine":
        predictionName = "Ice Cream Machine"
        percent = 100
    elif subCat == "Ice Machine":
        predictionName = "Ice Machine"
        percent = 100
    elif subCat == "Juice Dispenser":
        predictionName = "Juicer"
        percent = 100
    elif subCat == "Lighting":
        predictionName = "Air Curtain"
        percent = 100
    elif subCat == "Microwave":
        predictionName = "Microwave"
        percent = 100
    elif subCat == "Reach In Cooler":
        predictionName = "Cooler (Reach In)"
        percent = 100
    elif subCat == "Walk In Coolers":
        predictionName = "Cooler (Walk In)"
        percent = 100
    elif subCat == "Walk In Freezers":
        predictionName = "Freezer (Walk In)"
        percent = 100
    elif subCat == "Water Heaters":
        predictionName = "Hot Water Heater"
        percent = 100
    #get top 5 predictions
    results = getResults()
    #reset results
    refreshResults()
    #TEST PRINT
    str(results)
    print(results)
    #if no prediction exists 
    if predictionName == None:
        subCat = "Invalid"
    #get category name
    categoryName = category(subCat)
    # result = f'{"name":"{prediction}", "category":"Test", "subCat":"Sub_CAT", "brand":"", "model":"112131111", location:"On the left wall"}'
    #build json to be sent in response
    result = json.dumps({"name": predictionName, "category": categoryName, "subCat": subCat, "results": results, "percent": str(percent)})
    #result = json.dumps({"name": predictionName})
    #result = json.dumps({"category": categoryName})
    #close photo file
    f.close()
    #return JSON
    return result
#Run ipconfig and change the ip to you WLAN WiFi ip, runs on port 5000
#Make sure app has the same ip as server
if __name__ == "__main__":
    app.run(host="10.16.25.92")
