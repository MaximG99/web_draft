from flask import Flask, render_template
from weather import weather_by_city
app =  Flask(__name__)

@app.route( '/')
 defindex():
    page_title = "Прогноз погоды"
    weather =  weather_by_city("Moscow,Russia")
    return render_template("index.html", page_title= page_title, wether_text= wether_text) 
    
    
        


if __name__ = =  "__main__": 
    app.run(debug=True)