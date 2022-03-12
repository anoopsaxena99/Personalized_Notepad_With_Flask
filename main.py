#code for initializing website
from website import create_app
#as website is an python package when you import it 
#it automatically runs __init__.py 
app = create_app()

if __name__ == '__main__' :#only wants to run web server when main.py runs directly not need to import it
    app.run(debug=True)
    #run our web server and re-run webserver when we change 5h