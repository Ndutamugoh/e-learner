from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

# Mock profile data
profile_data = {
    'name': 'John Doe',
    'age': 16,
    'grade': '10th Grade',
    'contact': 'johndoe@example.com',
    'picture': '/static/images/profile-picture.jpg'  # Path to the profile picture
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', profile=profile_data)

@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Update profile data based on form submission
        profile_data['name'] = request.form.get('name')
        profile_data['age'] = request.form.get('age')
        profile_data['grade'] = request.form.get('grade')
        profile_data['contact'] = request.form.get('contact')
        return redirect(url_for('profile'))

    return render_template('edit_profile.html', profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True)
