from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6970a3b4ac2fd340f6970f1044bfe9fb'

posts = [
    {
        "title": "My Updated Post", 
        "content": "My first updated post!\r\n\r\nThis is exciting!", 
        "date_posted": "May 29th 2021.",
        "author":"Yemi"
        }, 
    {
        "title": "A Second Post", 
        "content": "This is a post from a different user...", 
        "date_posted": "May 29th 2021.",
        "author":"Yemi"
        }, 
    {
        "title": "Top 5 Programming Lanaguages", 
        "content": "Te melius apeirian postulant cum, labitur admodum cu eos! Tollit equidem constituto ut has. Et per ponderum sadipscing, eu vero dolores recusabo nec! Eum quas epicuri at, eam albucius phaedrum ad, no eum probo fierent singulis. Dicat corrumpit definiebas id usu, in facete scripserit eam.\r\n\r\nVim ei exerci nusquam. Agam detraxit an quo? Quo et partem bonorum sensibus, mutat minimum est ad. In paulo essent signiferumque his, quaestio sadipscing theophrastus ad has. Ancillae appareat qualisque ei has, usu ne assum zril disputationi, sed at gloriatur persequeris.", 
        "date_posted": "May 29th 2021.",
        "author":"Yemi"
    }, 
    {
        "title": "Sublime Text Tips and Tricks", 
        "content": "Ea vix dico modus voluptatibus, mel iudico suavitate iracundia eu. Tincidunt voluptatibus pro eu? Nulla omittam eligendi his ne, suas putant ut pri. Ullum repudiare at duo, ut cum habeo minim laudem, dicit libris antiopam has ut! Ex movet feugait mea, eu vim impetus nostrud cotidieque.\r\n\r\nEi suas similique quo, his simul viris congue ex? Graeci possit in est, ne qui minim delectus invenire. Mei ad error homero maluisset, tacimates assentior per in, vix ut vocent accusata! Mei eu inermis pericula patrioque? Debet denique sea at, ad cibo reformidans theophrastus per, cu inermis maiestatis vim!\r\n\r\nUt odio feugiat voluptua est, euismod volutpat qualisque at sit, has ex dicit ornatus inimicus! Eu ferri laoreet vel, dicat corrumpit dissentias nec in. Illum dissentiunt eam ei, praesent voluptatum pri in? Ius in inani petentium, hinc elitr vivendum an vis, in vero dolores electram ius?", 
        "date_posted": "May 29th 2021.",
        "author":"Yemi"
    }, 
    {
        "title": "Best Python IDEs", 
        "content": "Elit contentiones nam no, sea ut consul adipiscing. Etiam velit ei usu, sonet clita nonumy eu eum. Usu ea utroque facilisi, cu mel fugit tantas legimus, te vix quem nominavi. Prima deserunt evertitur ne qui, nam reprimique appellantur ne.", 
        "date_posted": "May 29th 2021.",
        "author":"Yemi"
    }, 
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html', title='About Page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

if __name__ == '__main__':
    app.run(debug=True)