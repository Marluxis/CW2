from selenium import webdriver
import json

values = {}  
with open("metrics.txt", "w") as outfile: 

    chromebrowser = webdriver.Chrome("D:\Work stuff\2nd year\2nd semester\SE Metrics\PerformanceData\drivers\chromedriver.exe") 

    for metric in range(10):

        chromebrowser.get("https://en.wikipedia.org/wiki/Software_metric") 
        
        metrics = chromebrowser.execute_script("return window.performance.getEntries()") 

        for m in metrics:

            url = m["name"]

            metrics_list = values.get(url, [])

            metrics_list.append(m["duration"]) 

            values[url] = metrics_list
            
            outfile.write(f"{m['name']}, {m['duration']}\n")


with open("average_duration.csv", "w") as avg_file:    

    for key, value in values.items():  

        average_duration = sum(value) / len(values) 

        avg_file.write(f"{key}, {average_duration}\n") 




with open("final_json_file" + ".json", "w", encoding="utf-8") as json_file: 

    json.dump(metrics, json_file, ensure_ascii=False, indent=4) 

chromebrowser.quit() 