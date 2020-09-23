# Assignments

Backend_language = django,djangorestframework
database = sqlite3

setup instructions = Run pip install -r requirements.txt (Python 2), or pip3 install -r requirements.txt (Python 3)


assumptions = [
  *cleancoding for more understandable
  *using token authentication for user registration and login
  *also added jwt authentication in settings.py which is as commented(can be used if needed)
  *re-useable code for same topic of execution
  *successfully done all of the listed questions
  *for searching, added backend search filter which means user can search movie by id and also by name and genre by just typing it in the field.
]


problems = I didn't face any major problem because I have done already 3 big projects(2 academic semester projects) with djangorestframework successfully.But sometimes I have taken help from net 
            to avoid syntex error.
            
remaining problems = None



apis =[
  userLogin: 127.0.0.1:8000/user/authenticate/,
  userRegistration: 127.0.0.1:8000/user/registration/,
  viewMovieList: http://127.0.0.1:8000/movie/movielist/,
  addMovie: http://127.0.0.1:8000/movie/movielist/,
  addRating: http://127.0.0.1:8000/movie/ratinglist/,
  specificMoviewithAVGRating: http://127.0.0.1:8000/movie/movielist/2/

]
