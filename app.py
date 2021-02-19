from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
    return 'Hello World! build is done???<br>이미지 변화 테스트중입니다' 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=80)
