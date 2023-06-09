
# We need to 'Flask' to create an app 
# 'request' to access request from view
# 'render_template' to  render a template
from flask import Flask, render_template, request
# 'traceback' for tracing error when execution
import traceback
# 'os' for functions are interacting with the operating system.
import os

# Naming the app
app = Flask(__name__)

# Route for different file page
@app.route('/files/<filename>')
def read_folder(filename="file1.txt"):
    folder_path = './Python_test_jr'
    start = request.args.get('start')
    end = request.args.get('end')
    try:
        with open(os.path.join(folder_path,filename),'r',encoding='cp437') as f:
            lines = f.readlines()
            if start and end:
                lines = lines[int(start)-1:int(end)+1]
        return render_template('index.html', content=lines)
    except Exception:
        return render_template('error.html', error=traceback.format_exc())
    
# Route for default home page
@app.route('/')
def read_files(filename="file1.txt"):
    folder_path = './Python_test_jr'
    with open(os.path.join(folder_path,filename),'r') as f:
        line = f.readlines()
    return render_template('file.html',content=line)

# Route for error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=traceback.format_exc())
    

 
# Run the app with port numbwwer
if __name__ == '__main__':
    app.run(debug=True,port=5005)