from flask import Flask
FAI=Flask(__name__)
@FAI.route('/stringresponse')
def stringresponse():
    return('We are dealing with  first view flask')
if __name__ == '__main__':
    FAI.run(debug=True)