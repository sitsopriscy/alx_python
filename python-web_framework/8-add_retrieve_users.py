 @app.route('/add_user', methods=['GET','POST'])
 def add_user():
     if request.method == 'POST':
         # code for handling POST request
         ...
     return render_template('add_user.html')
 
 