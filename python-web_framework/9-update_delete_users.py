# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        # code for handling POST request
    return render_template('update_user.html', user=user) 


# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
       # code for handling POST request
    return render_template('delete_user.html', user=user)
