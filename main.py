from flask import Flask,request
from caesar import rotate_character

app = Flask(__name__)
app.config['DEBUG'] = True

form  =  """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
             .error{{color:red;}}
        </style>
    </head>
     <body>
        <form method='post'>
        <!-- create your form here -->
           <p> <label>Rotate by:
            <input type="text" name="rot" value='0' /> </label></p>
            <p> <textarea name="text" value=''>{0}</textarea></p>
            
            <input type="submit" value="submit Query" />
        </form>

    </body>
</html>

"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    message =''
    try:
        rotate_by = int(request.form['rot'])
    except:
        #rotate_by = 0
        return "Rotate was not an integer."

    text = request.form['text']
    for char in text:
        if char.isalpha():
            message += rotate_character(char,rotate_by)
        else:
            message += char    
    
    return form.format(message)   

   
app.run()